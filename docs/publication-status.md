# MentorIA MC2 — passaggio ai portali, 2026-11-03

Repository canonico pubblico: https://github.com/mcumer/mentoria-mc2.
Prima consegna su main: `83ed57360fb10c4b76fbd622874d6cc5909b2287` (0.1.5).
Plugin path Anthropic: `packages/mentoria-mc2`, branch `main`.
Candidata aggiornata: **0.1.6**, stesso metodo e logo originali.

## OpenAI

L'account è accessibile nell'organizzazione Personal; nella pagina Plugins non
risultano candidature. Il tentativo di aprire il caricamento ha mostrato:
“You need a verified developer identity before you can create or upload a plugin.”
La scheda è stata portata a Organization settings → General → Verifications,
dove sono disponibili Individual e Business. Nessuna identità è stata
selezionata o verificata dall'agente; nessun ZIP è stato caricato.

Il proprietario deve completare il percorso con l'identità che vuole associare
alla pubblicazione. Le attestazioni e gli eventuali dati identificativi non
vanno ricavati dai metadati del plugin o inviati da questo repository.

## Anthropic

Account Claude Pro accessibile. Prima dell'attività: zero invii. Preparata una
bozza locale nella scheda del developer portal con repository, plugin path e
branch sopra. Convalida reale sul commit `83ed573`: 7 controlli, 6 superati.

- **Blocking — License missing:** il plugin non ha LICENSE né campo license.
  Il portale accetta anche una licenza alla root del repository. Serve la
  scelta dell'autore; la domanda è stata posta, senza risposta ancora acquisita.
- **Policy hold — author.name:** Grimory.ai segnalato come somigliante a un
  connector esistente “primary-ai”. Non è un rifiuto definitivo e non è stato
  aggirato rinominando l'autore. Mantenere il nome richiesto e sottoporre
  l'attribuzione reale alla review umana con il sito MC2/Grimory.
- **Warning — No icon:** corretta nella candidata 0.1.6 copiando il PNG MC2
  originale in `.claude-plugin/icon.png`, percorso convenzionale indicato dal
  portale. Il campo `icon` non è stato aggiunto: la CLI installata lo considera
  sconosciuto. Il percorso convenzionale mantiene `validate --strict` verde.
- Note: manifest Agent Plugins correttamente rilevato e ignorato dal loader
  Claude; il loader usa `.claude-plugin/plugin.json`. Immagine originale valida.

Riconvalidare main dopo ogni nuovo commit prima di proseguire. Il report del
portale è riferito a un commit preciso. Non sono state completate dichiarazioni
sui dati, accettazioni legali o invio finale in review; nessun plugin installato.

## Scelte ancora richieste

- Licenza: proprietaria con uso gratuito oppure MIT; nessuna scelta implicita.
- Paesi: tutti quelli consentiti oppure allowlist scelta; nessun targeting
  dedotto dalle lingue.
- Identità verificata OpenAI e successivi accordi/attestazioni del proprietario.

I casi conversazionali restano da eseguire con login CLI valido: la precedente
prova si è fermata prima dell'inferenza per OAuth scaduto. Le sessioni browser
attive non costituiscono una verifica del token della CLI.

Questa è una preparazione di candidatura con un blocco concreto; non è
pubblicazione su ChatGPT, Claude, Cowork o Claude Code. Nessun link pubblico
di installazione è stato inventato. Il sito non è stato modificato o deployato.
