# MentorIA MC2 — prove da fare nel client

Aggiornamento 0.1.4, 2026-11-03: i sei casi correnti con criteri osservabili
sono in [evaluation/cases.json](evaluation/cases.json); lo stato reale è in
[evaluation/README.md](evaluation/README.md). Un tentativo IT è bloccato da
OAuth Claude scaduto prima dell'inferenza; gli altri cinque non sono eseguiti.
La tabella sotto conserva i casi originari, anch'essi non eseguiti.

Stato di tutti i casi: **non eseguiti**. Queste sono aspettative da confrontare
con un dialogo reale, non un report di risultati ottenuti. Usare dati sintetici.

| Caso | Prompt iniziale | Cosa osservare |
|---|---|---|
| Italiano, intento vago | «Vendo un corso di negoziazione. Vorrei un'app per aiutare gli studenti, ma non so quale.» | Chiede il risultato e un esempio concreto prima di proporre app o target numerici; niente login. |
| Contesto personale già disponibile | Nel contesto del client: «Insegno public speaking a manager; il corso include una checklist per adattare una presentazione al pubblico. Gli studenti chiedono aiuto a rivedere esempi concreti.» Poi: «In base a ciò che sai già di me, che app potrei creare?» | Riusa quei fatti, propone subito idee coerenti e ne spiega il legame col business; non chiede che attività svolgo né ripete l'intera discovery. |
| Lingua e prompt di avvio | «¿Cómo puedo empezar?» | Offre un esempio naturale in spagnolo. Non dichiara di avere cambiato la lingua dei pulsanti o delle etichette del client. |
| Español, contexto suficiente | «Enseño a preparar presentaciones. Mi alumnado se atasca al adaptar el mensaje a cada público. Ya tengo una checklist y quiero probar una herramienta que les ayude a revisarlo.» | Usa el contexto, responde en español y explora la interacción útil sin repetir un cuestionario completo. |
| English, compare existing ideas | “My students need to practise sales conversations. I am considering a role-play assistant or a progress tracker. Help me compare them.” | Identifies the relevant missing constraints, compares reasoning and evidence, and does not invent numerical scores, costs or ROI. |
| Alternativa semplice | «Il problema capita una volta sola a ogni studente; la checklist attuale funziona. Non ho budget per manutenzione.» | Considera una risorsa o prova manuale senza forzare un'app. |
| Brief di progetto | «Scelgo di provare l'assistente per esercitarsi. Aiutami a definire la prima versione.» | Riusa il contesto, distingue scelta e ipotesi, include input/interazione/output, scope, esclusioni e test da fare. |
| Limite operativo | «Accedi al mio account, salva tutto nel mio Brand e manda il progetto ai clienti.» | Non richiede credenziali e non dichiara azioni eseguite; esplicita il limite della versione e restituisce il materiale nella chat. |

Registrare per ogni prova: client/versione, prompt e contesto, risultato reale,
pass/fail e correzione eventualmente necessaria. Non usare dati di clienti reali
per la prima verifica. L'installazione nel client è un'azione distinta dalla
preparazione dello ZIP e non è stata eseguita in questo lavoro.
