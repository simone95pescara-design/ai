# Stato operativo del sistema di trading

Questo file registra esclusivamente fatti, decisioni approvate e avanzamento.

## Fatti

- Non esiste ancora un sistema di trading operativo.
- Non sono state scelte strategia, fonte dati, broker, mercato, linguaggio o modalità di esecuzione.
- Il primo dominio indicato dall'utente è `data`, ma non è ancora definito alcun comportamento software.
- La prima implementazione ha introdotto dall'alto struttura, modello OHLCV, test e CI senza requisiti autorizzati.
- Il problema osservato non è soltanto tecnico: mancava un controllo che rendesse vietate le decisioni implicite dell'esecutore.

## Decisioni approvate

- Nessun codice viene introdotto finché input, output, vincoli e criterio di verifica non sono espliciti.
- Nessuna modifica strutturale viene applicata senza autorizzazione umana che nomini gli artefatti ammessi.
- In assenza di autorizzazione esplicita, l'esecutore resta in modalità di analisi e proposta.
- Ambiguità, silenzio e richieste generiche non costituiscono autorizzazione.
- La directory `tests/`, quando esisterà, sarà riservata esclusivamente a test automatici eseguibili.
- Non vengono introdotti agenti, orchestratori, workflow applicativi o strumenti di qualità finché un caso autorizzato non ne dimostra la necessità.
- Nessun componente può inviare ordini reali o gestire capitale in questa fase.

## Fase corrente

`controllo-autorita-prima-del-software`

## Avanzamento

- artefatti software prematuri: rimossi nella branch correttiva;
- documento Markdown sotto `tests/`: rimosso;
- richiesta iniziale: registrata come caso, non come test;
- contratto operativo: rafforzato con divieti e controllo di ammissibilità;
- primo comportamento del dominio data: non ancora definito;
- CI e strumenti: non autorizzati.

## Condizione di uscita

La fase termina soltanto quando esiste una richiesta concreta che supera il controllo di ammissibilità senza decisioni dedotte dall'esecutore.