# Stato operativo del sistema di trading

Questo file registra esclusivamente fatti, decisioni approvate e avanzamento.

## Fatti

- Non esiste ancora un sistema di trading operativo.
- Non sono state scelte strategia, fonte dati, broker, mercato o modalità di esecuzione.
- Il primo dominio richiesto è `data`.
- Il primo bisogno tecnico osservato è garantire comportamento software uniforme e verificabile.

## Decisioni approvate

- Il sistema viene sviluppato per casi verticali minimi verificabili.
- Il primo artefatto software è un modello OHLCV con invarianti esplicite.
- La qualità automatica usa Black, Ruff, mypy e pytest in GitHub Actions.
- Non vengono introdotti agenti AI, orchestratori o workflow applicativi finché un caso concreto non ne dimostra la necessità.
- Nessun componente può inviare ordini reali o gestire capitale in questa fase.

## Fase corrente

`fondazione-data`

## Avanzamento

- configurazione Python: proposta nella branch corrente;
- CI: proposta nella branch corrente;
- modello `Candle`: implementato;
- test degli invarianti: implementati;
- acquisizione dati esterni: non iniziata;
- strategia e backtest: fuori ambito.

## Condizione di uscita

La fase termina quando la CI supera tutti i controlli e il caso verticale data viene accettato o corretto sulla base dell'evidenza.
