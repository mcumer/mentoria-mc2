# MentorIA MC2

Version 0.1.8 · AI mentoring by Michele Cumer (Mikel / MC2).

Find the app in your method.

Mentoría and services: [mikelmc2.com](https://mikelmc2.com).

Developed by **Grimory.ai**. Powered by Grimory.

This first package contains two conversational skills:

- **app-investigation:** clarify the user, problem, desired result and app
  opportunities around a course or method.
- **app-decision:** compare alternatives and prepare a focused first-version
  project brief, including a simpler solution or postponement when appropriate.

Ask “Based on what I shared in this chat, which app could I create around my
method?” You can also bring an existing app idea to compare. The skills use
relevant text from this chat and ask only for details that affect the result.

The dialogue, examples and project brief follow the language you use, including
Italian, Spanish or English. [Starter prompts in all three languages](skills/app-investigation/references/starter-prompts.md)
are included. Host UI labels and starter buttons have a single configured text;
the package does not claim automatic UI localization for those fields.

No Grimory or SnakeMember connection, external account login, API key or MCP
server is included. Your AI platform's own account, availability and data rules
still apply. This package provides planning guidance and does not build apps,
validate market demand, collect leads, send information to a vendor or save
Brand, Audience or Avatar profiles in an external service.

## Privacy

The [MentorIA MC2 privacy notice](https://github.com/mcumer/mentoria-mc2/blob/main/packages/mentoria-mc2/PRIVACY.md) explains what the skills use in the current chat and what happens when you
send a request through the optional website form.

## Optional personal help

The AI mentoring is complete on its own. If you ask for personal review,
mentoring or implementation help, it can prepare a short, editable summary and
point you to the separate contact form: [Italiano](https://mikelmc2.com/mentoria/it/contact),
[Español](https://mikelmc2.com/mentoria/es/contact), or
[English](https://mikelmc2.com/mentoria/en/contact).

Review the summary, copy and paste it into the form, and enter your name and
email there. Nothing is transferred automatically from the AI conversation.
Share only the relevant information you choose, without private customer or
student records. The website registers the explicit request in the matching
language list through SnakeMember and sends Mikel a notification, under the
privacy notice displayed on that form. The plugin itself does not perform
that registration or send the notification.

Requesting contact does not automatically include a free review, book a
session or purchase a service. Scope, availability and any price are agreed
separately. You can continue with the AI mentoring without requesting contact.

## Loading and publication status

For a temporary Claude Code session, extract the ZIP and load its plugin folder
with `claude --plugin-dir /path/to/mentoria-mc2`. This loads the files for that
session; it does not publish them. Invoke `/mentoria-mc2:app-investigation` or
`/mentoria-mc2:app-decision` as appropriate. Other hosts use their supported
plugin-import flow; the Gemini skill requires its separate export.

Sources: [mcumer/mentoria-mc2](https://github.com/mcumer/mentoria-mc2).
A source repository is separate from an approved public catalog listing.
The [MentorIA MC2 Free Use License](LICENSE) allows free personal and
professional use. Modification, resale, and redistribution of the plugin
files require separate permission.

The workflow is an initial implementation of the agreed investigation and
decision plan. It is not a verified reproduction of the creator's entire
professional mentoring practice. It needs real use and editorial review.

The English listing includes Italian and Spanish translations in the OpenAI
publication metadata. The package also includes a Claude Code compatibility
manifest using the same skill files. No installation or public-directory
approval is implied by this archive.
