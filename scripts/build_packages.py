#!/usr/bin/env python3
"""Build local release archives; never install, publish, or create a repository."""

import hashlib
import json
import re
import shutil
import struct
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'packages/mentoria-mc2'
GEMINI = ROOT / 'exports/gemini/mentoria-mc2'
DIST = ROOT / 'dist'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def files(folder):
    result = {}
    for p in sorted(folder.rglob('*')):
        assert not p.is_symlink(), f'Symlink not permitted: {p}'
        if p.is_file():
            relative = p.relative_to(folder).as_posix()
            assert p.name != '.DS_Store' and '__MACOSX' not in p.parts
            assert p.suffix != '.zip' and not p.name.startswith('.env')
            result[relative] = p.read_bytes()
    return result


def check_links(folder):
    for p in folder.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            if target.startswith(('https://', '#')):
                continue
            resolved = (p.parent / target.split('#')[0]).resolve()
            assert resolved.is_relative_to(folder.resolve()), (p, target)
            assert resolved.is_file(), (p, target)


def archive(folder, destination, prefix=''):
    content = files(folder)
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in content.items():
            info = zipfile.ZipInfo(prefix + name, date_time=(2026, 11, 3, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with zipfile.ZipFile(destination) as z:
        assert z.testzip() is None
        assert sorted(z.namelist()) == sorted(prefix + name for name in content)
        for name, data in content.items():
            assert z.read(prefix + name) == data
    sha = digest(destination.read_bytes())
    destination.with_suffix(destination.suffix + '.sha256').write_text(
        sha + '  ' + destination.name + '\n')
    return {'archive': destination.name, 'sha256': sha,
            'bytes': destination.stat().st_size, 'inventory': list(content)}


def main():
    manifest = json.loads((PACKAGE / 'plugin.json').read_text())
    version = manifest['version']
    assert re.fullmatch(r'\d+\.\d+\.\d+', version)
    assert manifest['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
    openai = manifest['extensions']['com.openai']
    ui = openai['interface']
    assert len(ui['displayName']) <= 30 and len(ui['shortDescription']) <= 30
    assert len(ui['longDescription']) <= 4000
    assert ui['category'] == 'Business & Operations'
    assert len(ui['defaultPrompt']) <= 3
    assert len(set(ui['defaultPrompt'])) == len(ui['defaultPrompt'])
    assert all(0 < len(p) <= 128 and '\n' not in p for p in ui['defaultPrompt'])
    for translation in openai['publication']['translations'].values():
        assert len(translation['subtitle']) <= 30
        assert len(translation['description']) <= 4000
    for name in ['plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json']:
        m = json.loads((PACKAGE / name).read_text())
        assert m['version'] == version and m['name'] == manifest['name']
        assert m['description'] == manifest['description']
        assert len(m['description']) <= 500
        assert m['author'] == manifest['author']
        assert not m.get('apps') and not m.get('extensions', {}).get('com.openai', {}).get('apps')
    codex = json.loads((PACKAGE / '.codex-plugin/plugin.json').read_text())
    assert codex['interface'] == ui
    assert codex['extensions']['com.openai'] == {
        'review': openai['review'], 'publication': openai['publication']}
    assert not (PACKAGE / '.app.json').exists()
    assert not any((PACKAGE / f).exists() for f in ['mcp.json', '.mcp.json', 'hooks'])
    png = (PACKAGE / 'assets/mc2-logo.png').read_bytes()
    assert png[:8] == b'\x89PNG\r\n\x1a\n'
    width, height = struct.unpack('>II', png[16:24])
    assert width == height and width >= 256 and len(png) <= 5 * 1024 * 1024
    check_links(PACKAGE)

    # Export only link adaptations; keep the actual method in the two skills.
    investigation = (PACKAGE / 'skills/app-investigation/SKILL.md').read_text().split('---', 2)[2].lstrip()
    investigation = investigation.replace('references/starter-prompts.md', 'starter-prompts.md')
    investigation = investigation.replace('../../references/personal-help.md', 'personal-help.md')
    investigation = investigation.replace(
        'The companion `app-decision` skill can help\nwhen available; its presence is not required to complete this investigation.',
        'Continue with the [Decision workflow](decision.md) when useful; it is\n'
        'another phase of this skill, not a separate installed dependency.')
    decision = (PACKAGE / 'skills/app-decision/SKILL.md').read_text().split('---', 2)[2].lstrip()
    decision = decision.replace('references/project-brief.md', 'project-brief.md')
    decision = decision.replace('../../references/personal-help.md', 'personal-help.md')
    (GEMINI / 'references/investigation.md').write_text(investigation)
    (GEMINI / 'references/decision.md').write_text(decision)
    for source, target in [
        ('skills/app-investigation/references/starter-prompts.md', 'references/starter-prompts.md'),
        ('skills/app-decision/references/project-brief.md', 'references/project-brief.md'),
        ('references/personal-help.md', 'references/personal-help.md'),
        ('assets/mc2-logo.png', 'assets/mc2-logo.png')]:
        shutil.copyfile(PACKAGE / source, GEMINI / target)
    about = GEMINI / 'references/about.md'
    about.write_text(re.sub(r'Version: \d+\.\d+\.\d+', 'Version: ' + version, about.read_text()))
    check_links(GEMINI)
    DIST.mkdir(exist_ok=True)
    plugin = archive(PACKAGE, DIST / f'mentoria-mc2-{version}.zip', 'mentoria-mc2/')
    gemini = archive(GEMINI, DIST / f'mentoria-mc2-gemini-{version}.zip')
    with zipfile.ZipFile(DIST / gemini['archive']) as z:
        assert 'SKILL.md' in z.namelist()
        assert not any(name.startswith('.') for name in z.namelist())
    old = DIST / 'mentoria-mc2-0.1.3.zip'
    if old.exists():
        with zipfile.ZipFile(old) as z:
            assert z.read('mentoria-mc2/assets/mc2-logo.png') == png
            for relative in ['skills/app-investigation/references/starter-prompts.md',
                             'skills/app-decision/references/project-brief.md']:
                assert z.read('mentoria-mc2/' + relative) == (PACKAGE / relative).read_bytes()
    report = {
        'date': '2026-11-03', 'version': version,
        'plugin': plugin, 'gemini': gemini,
        'logo': {'width': width, 'height': height, 'sha256': digest(png)},
        'description_characters': len(manifest['description']),
        'source_sha256': {name: digest(data) for name, data in files(PACKAGE).items()},
        'checks': {'manifest_consistency_and_lengths': 'pass', 'contained_references': 'pass',
                   'archive_crc_inventory_and_bytes': 'pass', 'previous_logo_and_brief_preserved': 'pass' if old.exists() else 'not run: 0.1.3 archive not available',
                   'no_mcp_app_binding_or_runtime_hook': 'pass'},
        'not_claimed': ['host behavioral validation', 'portal validation', 'license approval',
                        'developer verification', 'installation', 'submission', 'publication']}
    (ROOT / 'docs/package-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'plugin': plugin, 'gemini': gemini}, indent=2))


if __name__ == '__main__':
    main()
