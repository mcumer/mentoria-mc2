# MentorIA MC2 — formato di caricamento per Gemini Apps

Aggiornamento locale 2026-11-03: disponibile anche
`dist/mentoria-mc2-gemini-0.1.4.zip`, con otto file e la risorsa facoltativa
personal-help, derivata dallo stesso metodo canonico della candidata 0.1.4.
Report corrente: `package-verification.json`; il report dedicato 0.1.3 resta
storico. Non è stata verificata una nuova importazione online o una candidatura
Google: il resto di questo documento conserva i requisiti consultati il
2026-10-22 e non certifica aggiornamenti successivi del servizio.

Verifica: 2026-10-22. Target: schermata «Upload a skill / Sube una habilidad»
di Gemini Apps, come nello screenshot dell'utente. Non Gemini CLI o Enterprise.

## Diagnosi

Lo ZIP multipiattaforma 0.1.3 è un plugin: ha `plugin.json` e due directory
`skills/<nome>/SKILL.md`. Non contiene un `SKILL.md` alla radice. L'importatore
mostrato richiede invece una singola skill con il proprio entrypoint nella
cartella principale. Il messaggio osservato non segnala che manchino le skill:
segnala che non si trovano al livello richiesto per quel tipo di caricamento.

## Requisiti verificati nelle fonti ufficiali

- È possibile caricare un file SKILL.md, una cartella o un file ZIP che
  contenga SKILL.md nella cartella principale.
- Il nome interno deve essere tutto minuscolo, con parole separate da trattini.
- Le risorse necessarie vanno caricate insieme alla skill. Per sostituirle,
  si ricarica l'intera skill con i suoi file.
- I formati usati nel nostro export, Markdown e PNG, sono ammessi.
- Il totale non deve superare 100 MB. Evitare file nascosti come .DS_Store.
- Script che effettuano richieste esterne non sono ammessi; il nostro export
  non contiene script né connessioni esterne.
- Google permette di combinare skill, ma un bundle plugin con più entrypoint
  annidati non è il formato descritto per questo importatore.

Fonti lette direttamente:

- [Create & manage skills for Gemini Apps](https://support.google.com/gemini/answer/17094296?hl=en).
- [About the transition from Gems to skills](https://support.google.com/gemini/answer/18560919?hl=en).

## Export dedicato

Archivio: `dist/mentoria-mc2-gemini-0.1.3.zip`.
Cartella sorgente dell'export: `exports/gemini/mentoria-mc2/`.
Nome interno della skill: `mentoria-mc2`.

Contenuto ZIP, senza una cartella esterna aggiuntiva:

```text
SKILL.md
references/
  investigation.md
  decision.md
  project-brief.md
  starter-prompts.md
  about.md
assets/
  mc2-logo.png
```

Questa è una singola skill MentorIA MC2 che include entrambe le fasi. L'entrypoint
seleziona il percorso pertinente alla richiesta; non richiede una seconda
installazione. Le istruzioni Investigazione e Decisione derivano direttamente
dalle due skill canoniche 0.1.3: rimossi i frontmatter delle singole skill dai
documenti di riferimento e adattati soltanto i link interni e il passaggio alla
fase Decisione. Brief, prompt nelle tre lingue e logo sono copie byte-identiche.
Nessuna nuova metodologia business o integrazione è stata aggiunta.

La fonte canonica del metodo rimane `packages/mentoria-mc2/skills/`. Non modificare
solo l'export e non aggiungere il suo entrypoint al plugin OpenAI/Claude: sono
adattamenti di distribuzione separati. I relativi hash di provenance sono in
`gemini-export-verification.json`.

Il documento about conserva sito mikelmc2.com, sviluppatore Grimory.ai e firma
Powered by Grimory. La documentazione consultata non garantisce campi UI per
logo/sviluppatore/sito equivalenti a quelli dei cataloghi di plugin: non
promettere che i metadati OpenAI vengano trasferiti nell'interfaccia Gemini.

## Verifica eseguita e uso

Confermati direttamente nello ZIP: un solo SKILL.md alla radice, YAML valido,
nome kebab-case, sette file, tutti i riferimenti locali presenti, nessun path
esterno, symlink o file nascosto, dimensione entro il limite, CRC e contenuti
identici ai file esportati. Validator Skill Creator positivo. I file canonici
del plugin originale e gli archivi precedenti sono rimasti invariati.

Per riprovare nella schermata mostrata, selezionare lo ZIP **Gemini** dedicato;
verificare l'anteprima della skill e poi creare la skill nel proprio account.
Se si usa invece il caricamento di una cartella, scegliere la cartella
`exports/gemini/mentoria-mc2`, che coincide con il nome interno.

Nessun upload, creazione, installazione o prova di conversazione è stato
eseguito in questo lavoro. Il controllo locale del formato non equivale a
validazione dell'importatore remoto. Il percorso documentato riguarda la
creazione/importazione di una skill; non prova una pubblicazione in un catalogo
pubblico o una specifica modalità di condivisione.
