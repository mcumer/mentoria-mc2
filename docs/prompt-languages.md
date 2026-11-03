# Lingue dei prompt e personalizzazione — 0.1.1

Decisione 2026-10-21: mantenere `app-investigation` e `app-decision`. App indica
l'applicazione che la persona vuole creare; i nomi non sono placeholder.

## Che cosa si può configurare

Nel formato OpenAI documentato, i prompt del plugin sono una stringa o fino
a tre stringhe in `interface.defaultPrompt`. Il prompt della singola skill
è una stringa in `agents/openai.yaml` → `interface.default_prompt`.
Si possono scrivere questi testi nella lingua desiderata, ma non è documentata
una mappa per locale per prompt iniziali o per titoli/descrizioni delle skill.

La mappa `publication.translations` supporta soltanto `subtitle` e `description`.
Secondo la documentazione corrente, viene conservata nell'upload ma non modifica
ancora il testo visibile del catalogo. Non aggiungere chiavi di traduzione
inventate al manifest e non dichiarare un cambio automatico dei pulsanti.

Il pacchetto mantiene una sola configurazione base inglese. Contiene esempi
EN/IT/ES in `skills/app-investigation/references/starter-prompts.md`, collegati
dalla skill e dal README. Si usano nel dialogo e come testo copiabile; non sono
una sostituzione automatica dei pulsanti dell'host. La conversazione, le domande,
le proposte e il brief seguono la lingua della persona.

## Personalizzazione

Le due skill riusano esplicitamente ricordi, istruzioni utente, contesto del
progetto e informazioni precedenti che la piattaforma rende già disponibili.
Investigazione esplicita brevemente i fatti business rilevanti e, se sufficienti,
propone subito app adatte al caso. Chiede soltanto i gap che cambiano la scelta;
non avvia un questionario o pretende dati già presenti. Eventuali conflitti
materiali restano visibili, senza fingere accesso a informazioni non esposte.

Questa modifica non aggiunge MCP, login, recupero dal backend o persistenza.
Non dà accesso automatico a tutta la cronologia dell'account. Non copia memorie
o dati personali in questo repository: l'input arriva dal contesto del client.

## Fonti verificate

- [OpenAI — prompt e campi della scheda](https://developers.openai.com/plugins/deploy/submission#listing-metadata).
- [OpenAI — traduzioni previste](https://developers.openai.com/plugins/deploy/submission#translate-listing-text).
- [OpenAI — metadati della skill](https://developers.openai.com/plugins/deploy/submission-errors#skill-agent-metadata-errors).
