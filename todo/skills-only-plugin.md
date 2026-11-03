# MentorIA MC2 — prima versione autonoma

## Repository scelto — 2026-11-03 · 0.1.5

L'utente conferma https://github.com/mcumer/mentoria-mc2.git e autorizza
versionare i file e procedere alle candidature OpenAI/Anthropic. Checkout
canonico mentoria-mc2, branch main, plugin path packages/mentoria-mc2.
La 0.1.5 aggiunge il repository ai manifest; le skill 0.1.4 sono invariate.

I vincoli precedenti SOLO FILE e repository ancora da scegliere sotto sono
storico. Non autorizzano comunque a inventare licenze, paesi o attestazioni.
Stato delle candidature e passaggio corrente: docs/readiness.md.

## Stato corrente — 2026-11-03 · candidata 0.1.4

Richiesta successiva: completare i passaggi preparatori possibili, usando questa
cartella e senza creare nuovi repository. Il proprietario sceglierà il repo
per la candidatura Claude in un passaggio successivo.

- [x] Percorso di aiuto personale facoltativo e su richiesta in entrambe le
  skill; configurazione commerciale separata dal metodo generico.
- [x] Riepilogo modificabile e minimizzato, link reali ES/IT/EN, copia/incolla
  e invio esplicito sul sito. Nessun dato o riepilogo nella URL.
- [x] Manifest 0.1.4 e schede EN/IT/ES aggiornati; logo e identità preservati.
- [x] Moduli reali e privacy letti via HTTPS; nessun nuovo invio email.
- [x] Archivi ricostruiti e controllati, script riusabile di build e report.
- [x] Skill Creator per due skill ed export Gemini; validazione Claude strict.
- [x] Documentazione di handoff verso i portali e il futuro repo, senza URL
  fittizi, marketplace, git init, commit o operazioni online sull'account.
- [ ] Verifica comportamentale: primo caso BLOCKED per OAuth Claude scaduto
  prima dell'inferenza; cinque casi NOT RUN per la stessa dipendenza.
- [ ] Licenza e paesi da scegliere; domande poste, nessun valore inventato.
- [ ] Repository, identità verificata, assistenza/condizioni e controlli dei
  portali da completare prima di poter dichiarare la candidatura pronta.
- [ ] Installazione persistente, upload, submission e pubblicazione: non eseguiti.

Stato preciso in [readiness](../docs/readiness.md), prossimi passi in
[publication-next-steps](../docs/publication-next-steps.md). Le sezioni che
seguono conservano lo storico delle versioni precedenti.

Decisione e autorizzazione: chat corrente, 2026-10-21. L'utente sceglie il nome,
descrizione inglese, traduzioni italiano/spagnolo, logo MC2, Powered by Grimory
e conferma di sviluppare il percorso per scegliere l'app dal piano esistente.

## Perimetro

Due skill complete nel pacchetto. Nessun MCP, OAuth, endpoint, credenziale,
integrazione Grimory/SnakeMember, raccolta contatti, salvataggio Knowledge,
Front, Admin o sito. Fonte dei dati: contesto utente/business già reso disponibile dalla piattaforma, conversazione e materiale fornito.
La firma di marca non rappresenta un collegamento al backend.

## Fonti effettivamente lette

- `todo/remote-skill-plugin.md`, integralmente: Investigazione e Decisione,
  criteri, scheda progetto, alternative e limiti. Le dipendenze remote sono
  sostituite dalla decisione esplicita corrente.
- Chat «Definire la prima skill», letta con read_thread il 2026-10-21:
  la scelta conclusiva ammette il primo test con skill complete nel plugin.
- Chat «Estrategia de marca personal», preview fornita dall'utente: pubblico,
  tre offerte e mentoría gratuita per individuare l'app dal proprio metodo.
- `mikelmc2-mentoring/context/mentoring.md`: campo metodo ancora da definire.
- Inventario dei prototipi, symlink e skill canoniche del metodo marketing:
  workshop business esistente; nessuna skill già implementata equivalente
  alle due skill app. Nessuna skill di marketing importata o modificata.
- Autorizzazione corrente: «Al percorso per scegliere l’app: sviluppalo dal
  piano esistente». È autorizzazione alla prima implementazione, non prova
  retroattiva di una metodologia professionale già validata.

## Consegna

- [x] Nome, autore commerciale MC2 e firma approvati; publisher verificato
  ancora distinto dall'autore dichiarato nel package.
- [x] Manifest portabile e overlay Codex/Claude allineati.
- [x] Catalogo inglese e traduzioni it-IT/es-ES con sottotitoli entro 30 caratteri.
- [x] Logo MC2 originale copiato senza modifiche, PNG 2048×2048, provenance.
- [x] Skill app-investigation e app-decision autosufficienti; progetto minimo
  e opzioni no-app/rinvio; istruzioni nella lingua della persona.
- [x] Validazione ufficiale Skill Creator su entrambe le skill.
- [x] `claude plugin validate` positivo sul manifest compatibile.
- [x] ZIP corrente `dist/mentoria-mc2-0.1.3.zip` creato e riletto integralmente:
  11 file, CRC e contenuti identici ai sorgenti, JSON/YAML e riferimenti validi,
  logo originale verificato tramite hash, nessun server/secret/path locale.
  Report: `docs/package-verification.json`. SHA-256 anche accanto allo ZIP.
- [ ] Prova comportamentale nel client target: non eseguita.
- [ ] Revisione editoriale sul metodo dell'autore con caso reale: non eseguita.
- [ ] Installazione, salvataggio nell'account e pubblicazione: non richiesti,
  non eseguiti. Nessun link pubblico inventato.

La fonte di verità del pacchetto è `packages/mentoria-mc2/`, non lo ZIP né la
cache di un client. Un cambio al sorgente richiede nuova verifica e ricostruzione
dell'archivio. Pubblicazione successiva: vedere `docs/readiness.md`.

## Aggiornamento 0.1.1 — 2026-10-21

Richiesta utente: riusare esplicitamente ciò che il client conosce già della persona e del business; non ripetere la discovery e proporre app pertinenti se il contesto basta. Nomi app-investigation/app-decision confermati.

Due skill aggiornate; prompt di ingresso orientato al contesto esistente, esempi EN/IT/ES inclusi e collegati dalle istruzioni. Non aggiunti campi di localizzazione non documentati ai manifest. Validatori delle due skill e manifest Claude nuovamente positivi; JSON/YAML, inventario ZIP, riferimenti e hash originali verdi. 0.1.0 preservata; report corrente 0.1.1. Prove comportamentali aggiuntive definite ma non eseguite; nessuna installazione o pubblicazione.

## Correzione riferimenti 0.1.2 — 2026-10-22

Manifest e README locali corretti: autore/developerName Grimory.ai; websiteURL e homepage https://mikelmc2.com; riferimenti MC2/Grimory espliciti nelle tre descrizioni. ZIP completo 11 file e archivio metadata-only ricostruiti, CRC/contenuti/hash verificati e manifest Claude valido. Tutti i file delle skill e i prompt sono identici alla 0.1.1.

Errore operativo dichiarato all’utente: è stata aggiornata anche la copia privata online sul plugin esistente, release pluginrel_6ad9e1c8ecbc81918c4360f1e44de8d6, senza creare un plugin o installarlo. L’utente ha precisato SOLO FILE. Nessuna ulteriore azione online o tentativo di ripristino non richiesto. Per il seguito, soltanto sorgenti e ZIP. La scheda pubblica e l’identità verificata del publisher non sono state modificate tramite impostazioni account.

## Fix importatore Claude 0.1.3 — 2026-10-22

Errore reale da screenshot: Plugin description must be at most 500 characters. Corrette le description dei tre manifest a 312 caratteri, lasciando la longDescription OpenAI di 713 caratteri e tutte le traduzioni estese. Versioni allineate a 0.1.3, autore Grimory.ai e sito mikelmc2.com preservati. ZIP completo 11 file riletto; limite 500 verificato dentro l’archivio, manifest Claude validato localmente. Skill, risorse, logo, README e prompt identici alla 0.1.2. Nessun browser, upload, installazione o aggiornamento account. La validazione claude.ai resta da riprovare da parte dell’utente.

## Export Gemini Apps 0.1.3 — 2026-10-22

Verificate le guide ufficiali Google per Gemini Apps: l'importatore mostrato
richiede una skill con SKILL.md nella cartella principale, non un bundle plugin.
Creato `dist/mentoria-mc2-gemini-0.1.3.zip`, entrypoint unico mentoria-mc2 che
riusa Investigazione e Decisione come due fasi, con risorse incluse. Sette file,
YAML/nome/limiti/link/CRC/contenuti verificati e validator Skill Creator positivo.
Plugin canonico e ZIP OpenAI/Claude invariati. Provenance, adattamenti dei link
e hash registrati in `docs/gemini-export-verification.json`.

Nessun upload/installazione/creazione account o skill online. La prova
dell'importatore Gemini resta da eseguire dall'utente. Export locale distinto
dalla pubblicazione in un catalogo o dalla condivisione. La modifica riguarda
istruzioni e confezionamento, senza codice runtime o configurazione eseguibile.
