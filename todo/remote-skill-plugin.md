# TODO — plugin App Mentoring con metodo remoto

> Decisione successiva 2026-10-21: il primo prodotto è **MentorIA MC2**,
> skills-only e senza autenticazione esterna. Vedere `skills-only-plugin.md`.
> Questo documento conserva il piano dell'eventuale integrazione remota;
> OAuth/catalogo non sono prerequisiti del primo pacchetto.

> Stato consegna: 🔴 P0 da fare; P1 attende R1 Rails — 2026-10-14.

Nome provvisorio; solo struttura documentale, nessun package installabile.

## Intento e fonti

Due skill leggere Investigazione e Decisione per passare da risultato di
business a scelta motivata e progetto minimo di app. Il metodo completo è
canonico su Grimory, con accesso verificato dal server.
La chat «Definire la prima skill» descrive il percorso ma non fornisce il metodo
professionale completo. Non riempire il gap con un metodo AI attribuito
all'autore. Nessun corpus marketing importato o rinominato.

## Contratto C1 candidato (copia Rails)

Tool read-only `skills_list`, `skill_get`, `skill_resource_get`, owner
`grimory_native`, bounded context `skills`, scope nuovo `grimory.skills.read`.
Schemi chiusi a ogni livello, snake_case e descrizioni property semantiche.
Actor/business derivati dal token, mai input.

- skills_list input opzionali: package_key string 1..100, query string 1..200,
  cursor opaco 1..2048, limit integer 1..50 default 20. Query solo
  nome/descrizione; ordine stabile (package_key, skill_key). Output
  `{items:[Summary],next_cursor:string|null,correlation_id:string}`.
  Summary = package_key string 1..100, skill_key string 1..150, name string
  1..200, description_short string 1..500, author_name string 1..200, version
  semver major.minor.patch, locale string 1..32, content_digest
  `sha256:<64 hex>`. Solo package pubblicati/accessibili/attivati.
- skill_get input skill_key string 1..150 obbligatoria, version semver
  opzionale (omessa = corrente pubblicata; indicata = esatta, no fallback).
  Output Summary più instructions_markdown UTF-8 non vuoto <=65536 byte,
  resources array 0..20 e correlation_id string. Resource descriptor =
  resource_id string opaca 1..128, name 1..200, description_short 1..500,
  media_type enum text/markdown|text/plain|application/json, byte_size integer
  1..65536, content_digest `sha256:<64 hex>`.
- skill_resource_get input obbligatori skill_key 1..150, version semver
  esatta, resource_id 1..128 dal descriptor. Output skill_key, version,
  resource_id, name, media_type, content_utf8 UTF-8 non vuoto <=65536 byte,
  byte_size, content_digest, correlation_id, stessi tipi precedenti.
  Risorsa vincolata alla revisione autorizzata, niente URL/path client o script.
- Ogni campo output è obbligatorio; nullable solo next_cursor. Success in
  structuredContent e breve content. Errori applicativi isError:true con
  structuredContent `{error:{code:string,message:string},correlation_id:string}`.
  Codici invalid_payload, invalid_cursor, not_found, rate_limited.
  Inesistente/foreign/non pubblicata/disabilitata/accesso negato = not_found.
  Auth 401 con challenge; scope insufficiente result content-free con
  _meta["mcp/www_authenticate"], metadata resource e scope esatto.
- Ogni call rivalida identità/business/client/resource/scope, diritto corrente
  e attivazione. Cursor vincolato a identità/business/filtri/ordine. Pin versione
  non aggira scadenza/revoca. Audit content-free correlato.

Trasporto candidato /mcp/skills, HTTPS core.grimory.ai, **non esistente**;
R0 deve congelare resource, metadata e login/consenso prima del runtime.

## P0 — metodo e ingresso

- [ ] Raccogliere il processo reale dell'autore, esempi e scheda progetto;
  separare fonti, preferenze e decisioni di implementazione. Leggere le fonti
  applicabili integralmente e mostrare una preview organica per conferma.
- [ ] Investigazione: prima risultato/quantità/tempo, poi business/pubblico,
  ostacoli, strumenti e risorse. Chiedere solo informazioni mancanti.
- [ ] Decisione: confronto ragionato, opzione senza app/rinvio, MVP/prova,
  dati/integrazioni, criterio di risultato. No target, ROI, prezzi o preventivi
  inventati. Nessuna preferenza obbligatoria per sviluppo affidato all'autore.
- [ ] Congelare skill_key/versioni e risorse effettive con Rails; il metodo
  confermato deve essere pubblicato esplicitamente, non via dual write.

## P1 — solo dopo R1 Rails

- [ ] Creare root plugin.json/mcp.json e skills/app-investigation/SKILL.md,
  skills/app-decision/SKILL.md; manifest portabili con metadati reali e URL
  consegnata da Rails, OAuth senza credenziali nel package.
- [ ] Le skill selezionano il metodo, chiamano skill_get, fissano versione e
  digest, recuperano solo risorse necessarie. skills_list serve discovery,
  non caricamento dell'intero corpus a ogni turno.
- [ ] Assenza tool/accesso: dichiarare limite e fermare il percorso specifico;
  non sostituire il metodo proprietario con istruzioni inventate.
- [ ] Validare skill e package; eval con obiettivo vago, contesto sufficiente,
  app non conveniente, dati contraddittori, accesso negato, versione cambiata,
  risorsa non autorizzata e richiesta di azione esterna.
- [ ] Provare installazione privata e sessione nuova nel client target;
  tools/list/list/get/resource e audit via OAuth reale dopo release autorizzata.
  Test Codex non dimostra automaticamente comportamento ChatGPT web.

Definition of Done: metodo confermato con provenance, wrapper verificati,
package validato, auth reale e output della scheda progetto osservati;
altrimenti consegna parziale con gate mancanti espliciti. Main integrata e
pushata solo quando esiste un repo canonico e la consegna runtime è verificata.
Il coder aggiorna questo file; non scrive nel todo generale.
