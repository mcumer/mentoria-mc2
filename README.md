# MentorIA MC2 — sorgenti e preparazione pubblicazione

Mentoría con AI di Michele Cumer, sviluppata da Grimory.ai. Powered by Grimory.
Versione candidata **0.1.5**, preparata il 2026-11-03.

La fonte canonica è `packages/mentoria-mc2/`: due skill per esplorare un'app
attorno a un metodo e definire una prima versione. Il risultato AI è autonomo;
un riepilogo e il modulo di contatto personale sono disponibili solo su richiesta.
Il plugin non esegue invii e non contiene MCP o autenticazione esterna.

## Cartelle

- `packages/mentoria-mc2/`: plugin portabile con compatibilità Claude e Codex;
  questa è la cartella da indicare al futuro portale Anthropic.
- `exports/gemini/mentoria-mc2/`: adattamento locale a una sola skill; non è
  una pubblicazione nel catalogo Google.
- `dist/`: ZIP generati e checksum; le versioni precedenti sono conservate.
- `scripts/build_packages.py`: ricostruzione e controllo deterministico degli
  archivi, senza installazioni o servizi esterni.
- `docs/`: scheda nelle tre lingue, controlli e passaggi rimasti.

Ricostruzione: `python3 scripts/build_packages.py`.
Il report macchina è `docs/package-verification.json`; lo stato operativo è
[docs/readiness.md](docs/readiness.md).

## Repository e pubblicazione

Repository scelto dall'utente: [mcumer/mentoria-mc2](https://github.com/mcumer/mentoria-mc2).
Questo checkout è la fonte canonica. La vecchia cartella locale
`grimory-app-mentoring` conserva lo storico e non va sviluppata in parallelo.

Per Anthropic, indicare il repository sopra e il plugin path
**packages/mentoria-mc2**. Il manifest Claude è in quella cartella.
Gli archivi si ricostruiscono localmente con lo script; dist è ignorata da Git.

La versione 0.1.5 aggiorna i riferimenti al repository senza modificare il
metodo 0.1.4. Licenza, paesi, identità verificata e verifiche dei portali
restano passaggi distinti. Il caricamento dei sorgenti non implica una
pubblicazione nei cataloghi. Stato: [docs/readiness.md](docs/readiness.md).
