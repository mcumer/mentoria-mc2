# MentorIA MC2 — stato e limiti della prima versione

## Che cosa contiene

Plugin composto da due skill conversazionali, senza server. Il nome è
MentorIA MC2 e la firma è Powered by Grimory. `app-investigation` esplora il
problema e le opportunità; `app-decision` confronta le alternative e produce
la scheda del progetto minimo. Il metodo è la prima implementazione del piano
autorizzata il 2026-10-21, da provare e revisionare con l'autore.

La piattaforma AI può richiedere il proprio account. Il plugin non richiede
un account Grimory o SnakeMember, non accede a Brand/Audience/Avatar, non
registra il contatto e non conserva il risultato nel backend. Il contenuto
della conversazione resta soggetto alle regole della piattaforma ospitante:
assenza di OAuth del plugin non significa anonimato o assenza di trattamento.

Un eventuale link consegnato dopo l'iscrizione alla lista è distribuzione
commerciale separata; questo pacchetto non verifica l'iscrizione e non impedisce
la condivisione del link o del contenuto. Nessun percorso lista è stato creato.

## Struttura e manutenzione

`packages/mentoria-mc2/plugin.json` è il manifest portabile canonico.
`.codex-plugin/plugin.json` e `.claude-plugin/plugin.json` adattano lo stesso
contenuto; non duplicano le skill. `skills/` contiene le due skill e il template
del brief; `assets/mc2-logo.png` è l'originale del sito riutilizzato.

Descrizioni, prompt e istruzioni non presuppongono un sito o un tool non
disponibile. Nessun endpoint, bearer, dipendenza MCP o script runtime è incluso.
Non sono state modificate configurazioni personali, marketplace o altri plugin.

## Verifiche

- JSON/YAML e limiti di testo, unicità e riferimenti contenuti: controllo statico.
- Entrambe le skill: validator ufficiale Skill Creator positivo.
- Manifest Claude Code: validazione nativa positiva.
- File PNG: formato reale, dimensioni 2048×2048, dimensione entro 5 MiB,
  confronto SHA-256 con l'originale. Logo osservato visivamente.
- Archivio `dist/mentoria-mc2-0.1.1.zip`: riletto integralmente, 11 file,
  CRC/inventario/contenuti identici ai sorgenti. Report e SHA-256 disponibili.
  Nessuna prova statica equivale a installazione, import dal portale o prova
  comportamentale. Casi da provare in `try-it.md`.

## Prima della pubblicazione pubblica

Restano da determinare l'identità verificata del publisher e i paesi di
distribuzione. MC2 è l'autore commerciale dichiarato, non una verifica legale.
Nessun elenco di paesi è inventato o impostato automaticamente come globale.
Confermare le dichiarazioni commerciali richieste dal portale: questa prima
prova è stata descritta come gratuita e il package non gestisce acquisti.

Preparare e verificare pagina prodotto, assistenza, privacy e condizioni per
il percorso pubblico scelto. Gli URL non sono inseriti perché nessuna pagina
specifica del prodotto è stata verificata. Non copiare automaticamente quelli
di un altro prodotto. Il manifest skills-only può essere valido anche senza
tutti gli URL; ciò non dimostra che la presentazione pubblica sia completa.

Provare le due skill nel client target con un caso sintetico e poi con un caso
reale appropriato. Non dichiarare eseguiti i prompt di review solo perché
presenti nei metadati. Essendo skills-only, non sono applicabili i casi MCP,
il video obbligatorio per MCP o credenziali di reviewer di un servizio esterno.

La preparazione del pacchetto non crea un plugin privato nell'account e non
costituisce invio in revisione o pubblicazione.

## Lingue e fonti tecniche

Il manifest ha la scheda base inglese e traduzioni it-IT/es-ES. Secondo la
documentazione corrente, le traduzioni vengono validate e conservate ma non
cambiano ancora il testo mostrato nel catalogo OpenAI. Questa limitazione è
distinta dalla lingua in cui le skill possono conversare.

- [OpenAI: pubblicazione e traduzioni](https://developers.openai.com/plugins/deploy/submission#translate-listing-text).
- [OpenAI: metadati della scheda](https://developers.openai.com/plugins/deploy/submission#listing-metadata).
- [Claude Code: manifest e layout](https://code.claude.com/docs/en/plugins-reference).

Aggiornamento 0.1.1: uso esplicito del contesto personale/business già reso disponibile dalla piattaforma, proposte immediate quando sufficiente ed esempi di avvio EN/IT/ES. Nessuna promessa di localizzazione automatica dei pulsanti; vedere `prompt-languages.md`. Lo ZIP 0.1.0 originale è conservato e il suo hash è stato riconfermato.

## Metadati 0.1.2 — SOLO FILE

Pacchetto locale corrente: `dist/mentoria-mc2-0.1.2.zip`. Nei tre manifest: autore Grimory.ai, homepage https://mikelmc2.com. Nel manifest OpenAI: developerName Grimory.ai e websiteURL https://mikelmc2.com. Le descrizioni EN/IT/ES e README includono i riferimenti richiesti. Il sito MC2 è stato verificato tramite HTTP 200 e lettura del contenuto, redirect a /foco; nessun nuovo sito o pagina è stato creato.

Verificato che skill, risorse, logo e prompt siano invariati rispetto alla 0.1.1; ZIP 11 file riletto e manifest Claude valido. Le copie precedenti sono preservate. L’utente richiede esclusivamente file locali: nessuna installazione, pubblicazione o ulteriore modifica online. L’aggiornamento privato online eseguito prima della correzione è registrato nel todo come errore operativo.

## Fix limite Claude 0.1.3

Archivio corrente `dist/mentoria-mc2-0.1.3.zip`. Description comune dei manifest: 312 caratteri su un massimo di 500 richiesto dall’importatore claude.ai. La longDescription OpenAI di 713 caratteri e le traduzioni estese restano invariate. Controlli locali e ZIP verdi; non eseguita una nuova prova sul sito, nessun upload o installazione.

## Formato Gemini Apps

Per la schermata di caricamento skill Gemini usare l'archivio dedicato
`dist/mentoria-mc2-gemini-0.1.3.zip`: una skill mentoria-mc2 con SKILL.md alla
radice e le due fasi nei riferimenti. Il bundle OpenAI/Claude resta invariato.
Sette file verificati localmente, nessuna prova online. Requisiti ufficiali,
struttura e istruzioni in `gemini-packaging.md`.
