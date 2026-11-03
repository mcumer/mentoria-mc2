# MentorIA MC2 — candidata repository 0.1.6

Aggiornato: **2026-11-03**. Stato: candidata locale verificata nel formato,
**non pronta da dichiarare pubblicata o approvata**. Repository scelto: https://github.com/mcumer/mentoria-mc2.
La precedente preparazione 0.1.4 è storica; la 0.1.5 aggiunge il riferimento
reale al repository e mantiene invariato il metodo. Nessun marketplace o
installazione personale.

## Completato

- Due skill canoniche nella lingua della persona, con contesto già disponibile,
  confronto delle alternative e brief di una prima versione.
- Percorso personale facoltativo in entrambe le skill. Il risultato AI è
  completo senza di esso; si attiva quando la persona chiede aiuto personale.
- Risorsa prodotto condivisa `references/personal-help.md`: riepilogo
  modificabile, minimizzazione, link ES/IT/EN, copia/incolla e invio esplicito.
  Nessuna email richiesta nella chat, nessun invio automatico, promessa di
  gratuità, agenda, prezzo o disponibilità.
- Nome MentorIA MC2, autore commerciale Michele Cumer, sviluppatore richiesto
  Grimory.ai, logo originale e Powered by Grimory preservati.
- Manifest portabile e overlay Claude/Codex allineati alla 0.1.6, description
  entro 500 caratteri. Scheda inglese con descrizioni italiano/spagnolo.
- Pagina prodotto, tre moduli e privacy pubblica del modulo letti via HTTPS
  il 2026-11-03. Nessun nuovo invio di prova: si verifica il contenuto pubblico,
  non si ripete la verifica di recapito già conclusa il 30 ottobre.
- ZIP OpenAI/Claude e Gemini ricostruiti, CRC, contenuti, inventario, link,
  limiti, logo e checksum verificati. Archivi precedenti conservati.
- Validatori Skill Creator positivi per le due skill e l'export Gemini;
  `claude plugin validate --strict` positivo sul sorgente.

Report: `package-verification.json`, `contact-url-verification.json`,
`listing-url-verification.json`, `privacy-url-verification.json`.
I tentativi `/privacy` e `/terms` restituiscono 404: non sono stati usati nei
manifest. La privacy reale è `/privacidad#mentoria-contact`.

## Prova comportamentale e limite reale

Sei casi sintetici in `evaluation/cases.json`, con risultati attesi relativi a
lingua, riuso del contesto, alternative semplici, aiuto facoltativo, dati di
terzi e assenza di invii/prenotazioni inventate.

Tentata una conversazione IT con la 0.1.4 caricata solo per la sessione CLI,
senza installazione, MCP, invio al modulo o persistenza della chat. Claude ha
restituito **OAuth session expired and could not be refreshed**, prima di
qualunque inferenza: zero token di input/output, nessun risultato della skill.
La prova è quindi **bloccata**, non PASS. Gli altri cinque casi non sono stati
eseguiti, evitando tentativi ripetuti con la stessa autenticazione scaduta.
Evidenza sintetica in `evaluation/README.md`; output CLI originale conservato
nella precedente cartella locale e non incluso nel repository pubblico.
Non sono state avviate autenticazioni o cambiate impostazioni dell'account.

## Rimane prima dei cataloghi

1. Scegliere licenza e paesi. La domanda è stata posta; senza risposta i
   campi restano assenti. Non equivale a una licenza MIT o a targeting globale.
2. Versionare i file nel repository indicato e usare il plugin path
   `packages/mentoria-mc2`. La visibilità deve essere pubblica prima del go-live
   Anthropic; verificare la visibilità effettiva, senza cambiarla di nascosto.
3. Ripetere i casi comportamentali con autenticazione valida e verificare i
   componenti effettivamente caricati nei client target.
4. Confermare l'identità verificata del pubblicatore, i permessi del portale,
   le dichiarazioni commerciali e la disponibilità territoriale. Il nome nel
   manifest non sostituisce la verifica dell'identità.
5. Completare assistenza e condizioni applicabili al plugin; nessun URL o
   impegno legale inventato. Privacy già pubblicata per il percorso web;
   il trattamento della conversazione è quello della piattaforma ospitante.
6. Eseguire i controlli dei portali, risolvere i rilievi, ottenere approvazione
   e pubblicare. Solo dopo aggiornare i link del sito con le schede effettive.

Per OpenAI skills-only, i quattro URL non sono tutti un gate della validazione
metadati; per un'eventuale app MCP in review lo sono. Restano informazioni
editoriali da completare per presentare il servizio correttamente. Non servono
casi MCP, video dimostrativo obbligatorio MCP o credenziali di un servizio che
questo plugin non possiede. Anthropic richiede README e licenza per il catalogo.

## Canali e versioni

La fonte è la cartella locale, non la cache installata. Il sito distribuisce
ancora i materiali 0.1.3: non è stato modificato né deployato in questo task.
La 0.1.6 è in `dist/` e si consegna per la candidatura, non per aggiornare
silenziosamente un plugin nell'account. Google resta la seconda fase; avere
un export locale non dimostra pubblicazione né compatibilità online attuale.

Le traduzioni OpenAI sono conservate nel pacchetto; secondo la documentazione
le traduzioni importate non cambiano ancora il testo mostrato nel catalogo.
Il dialogo multilingue resta distinto dalle etichette dell'interfaccia host.

Passi esatti: [publication-next-steps.md](publication-next-steps.md).
Storico precedente: [readiness-through-0.1.3.md](readiness-through-0.1.3.md).

## Esito effettivo dei portali · 2026-11-03

Repository e sorgenti già pushati su main. OpenAI richiede la verifica
Individual/Business dell'identità prima di consentire l'upload; nessun upload
eseguito. Anthropic ha validato il commit iniziale 83ed573: blocco licenza,
policy hold sull'autore Grimory.ai e warning icona. L'icona è corretta nella
0.1.6 con il file standard; la licenza richiede la scelta del proprietario.
Dettaglio, scope e stato: [publication-status.md](publication-status.md).
