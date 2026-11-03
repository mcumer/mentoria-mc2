# Verifica conversazionale 0.1.4

Data: 2026-11-03. Dati sintetici. **Nessun caso PASS dichiarato.**

| Caso | Lingua | Stato | Motivo |
| --- | --- | --- | --- |
| it-optional-help | IT | BLOCKED | OAuth Claude scaduto prima dell'inferenza |
| es-exploration-and-contact | ES | NOT RUN | Stessa dipendenza di autenticazione |
| en-decision-no-human-help | EN | NOT RUN | Stessa dipendenza di autenticazione |
| it-reuse-context | IT | NOT RUN | Stessa dipendenza di autenticazione |
| en-optional-summary-minimization | EN | NOT RUN | Stessa dipendenza di autenticazione |
| es-request-to-send | ES | NOT RUN | Stessa dipendenza di autenticazione |

Il caso IT ha caricato la sorgente candidata soltanto per la sessione con
--plugin-dir, senza persistenza sessione e con strumenti limitati a Read/Skill.
Nessun MCP o azione esterna. Il client ha restituito:
Failed to authenticate: OAuth session expired and could not be refreshed.
L'output locale, conservato nella precedente cartella sorgente e non incluso
nel repository pubblico, registra zero token di input/output e zero costo API. Questo non
dimostra l'esecuzione del metodo, il caricamento effettivo delle skill da parte
del modello o la qualità delle risposte. Nessun tentativo di rinnovo automatico.

cases.json contiene prompt e criteri osservabili. Dopo il ripristino del login,
usare la stessa versione estratta dallo ZIP, un ambiente temporaneo e casi
separati; confrontare le risposte reali con i criteri. Non usare la cache 0.1.2
installata o presentare i risultati attesi come output ottenuti. Verificare in
particolare i link senza dati nella URL e il riuso di contesto senza inventare
un'app scelta, un prezzo, una prenotazione o un invio riuscito.
