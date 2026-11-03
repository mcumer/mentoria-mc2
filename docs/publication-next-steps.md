# MentorIA MC2 — passaggio al repository e ai cataloghi

Preparato il 2026-11-03. Versione candidata **0.1.6**. Questo è un handoff,
non una dichiarazione di approvazione o una richiesta già inviata.

## Prima scelta ancora necessaria

Repository confermato: [mcumer/mentoria-mc2](https://github.com/mcumer/mentoria-mc2).
Checkout canonico: mentoria-mc2. Il plugin conserva il path
**packages/mentoria-mc2**; nessun altro repository o marketplace necessario.
La 0.1.5 aggiunge il riferimento reale ai tre manifest senza cambiare le skill.

Servono inoltre la licenza scelta dall'autore e la disponibilità per paese.
Sono decisioni separate dall'essere gratuito per chi usa la mentoría. Un repo
pubblico rende leggibili i file; non implica automaticamente licenza MIT.
La candidatura Anthropic richiede un file LICENSE o un campo license: il
pacchetto attuale non inventa uno di questi valori.

## OpenAI · ChatGPT e Codex

- [ZIP locale 0.1.4](../dist/mentoria-mc2-0.1.6.zip).
- Contiene manifest radice portabile, overlay Codex/Claude, logo e due skill.
  Nessuna app privata, MCP, credenziale o script runtime.
- Nei [Plugins](https://platform.openai.com/plugins) scegliere organizzazione,
  progetto e identità verificata corretti; non creare un duplicato se esiste
  già una candidatura dello stesso plugin. Le vecchie copie personali non
  provano che esista una candidatura pubblica: controllare il portale.
- Caricare la candidata come bozza solo nel successivo passaggio autorizzato;
  verificare nomi, versione, lingue, paesi, privacy e rilievi automatici.
- Gli accordi e le attestazioni legali sono del proprietario autorizzato.
  Non indicare un'app MCP o credenziali di reviewer inesistenti.
- Il plugin fornisce mentoría AI gratuita e un rimando facoltativo alla richiesta
  personale sul sito. Nessun acquisto, pagamento o prenotazione nel pacchetto.
  Verificare come dichiarare questo comportamento nel portale; l'assenza di
  pagamento nella chat non certifica da sola l'ammissibilità commerciale.
- Dopo review e approvazione, pubblicare esplicitamente. L'upload non basta.

Il nome developer pubblico segue l'identità verificata selezionata: il valore
Grimory.ai nei file non sostituisce quella verifica. Non sono richiesti casi
di test MCP o demo MCP per una versione con sole skill. Se in futuro servisse
un MCP, rivalutare la distribuzione: le istruzioni correnti non supportano
l'aggiunta di un MCP a un plugin già pubblicato come skills-only.

## Anthropic · Claude, Cowork e Claude Code

- Collegare a Claude l'account GitHub con permesso di push sul repo scelto.
  Nessuna credenziale GitHub nel pacchetto.
- Repository: **https://github.com/mcumer/mentoria-mc2**.
  Plugin path: **packages/mentoria-mc2**. Branch canonica: **main**.
- Aggiungere la licenza scelta, il repository effettivo e incrementare la
  versione se il contenuto di una release già distribuita cambia.
- Concludere la verifica conversazionale con una sessione autenticata e un
  caricamento temporaneo della versione candidata; niente installazioni
  automatiche negli account personali.
- Nel [portale](https://claude.ai/directory/manage), selezionare Plugin bundle,
  indicare repository e plugin path, validare il commit preciso e risolvere
  gli errori. Il repository può restare privato in review, ma deve essere
  pubblico prima che la scheda vada online.
- Verificare piano/ruolo dell'account, descrizione dal README, contatto del
  proprietario, trattamento dati e attestazioni; inviare solo nello scope
  autorizzato. Review e pubblicazione sono passaggi distinti.

Il catalogo Anthropic distribuisce il plugin a Claude.ai/Cowork e tramite la
sincronizzazione account a Claude Code. Un marketplace Git proprio è un canale
alternativo, non un requisito da aggiungere adesso. Nessun marketplace fittizio
è stato preparato o collegato.

## Dopo la pubblicazione

Verificare i link pubblici reali da un altro account e il percorso nelle tre
lingue. Solo allora aggiornare src/lib/mentoria/platform-config.ts nel repo
**mikelmc2-web**, mantenendo lo stile di Vanessa e adeguando il tipo directUrl
oggi fissato a null. Conservare una modalità di importazione come alternativa
solo dove supportata. Non sostituire gli attuali link con URL ipotetici.

Questo task usa il repository scelto. Non modifica sito, liste, backend o email.

## Fonti primarie consultate

- [OpenAI · Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission).
- [Anthropic · Submit your plugin](https://claude.com/docs/plugins/submit).
- [Anthropic · Pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist).
- [Claude Code · Publish and distribute](https://code.claude.com/docs/en/plugins/publish).
