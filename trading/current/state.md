# Stato operativo del sistema di trading

Questo file registra esclusivamente fatti, decisioni approvate e avanzamento.

## Fatti

- Non esiste ancora un sistema di trading operativo.
- Non sono stati scelti strategia, fonte dati, broker, mercato, linguaggio o modalità di esecuzione.
- Il primo dominio indicato è `data`.
- Non è ancora stato definito il primo comportamento software da implementare.
- La prima proposta ha introdotto prematuramente un modello `Candle`, test Python e CI senza requisiti sufficienti.

## Decisioni approvate

- Il sistema verrà sviluppato tramite trasformazioni esplicite e verificabili.
- Nessun artefatto software viene introdotto prima della definizione di un comportamento osservabile autorizzato.
- Documenti di analisi e casi osservati non vengono collocati nella directory dei test automatici.
- Non vengono introdotti agenti AI, orchestratori o workflow applicativi finché un caso concreto non ne dimostra la necessità.
- Nessun componente può inviare ordini reali o gestire capitale in questa fase.

## Fase corrente

`definizione-primo-comportamento-data`

## Avanzamento

- richiesta iniziale: registrata in [`../cases/first-request.md`](../cases/first-request.md);
- primo comportamento software: non definito;
- linguaggio e toolchain: non decisi;
- CI: non autorizzata;
- implementazione: non iniziata.

## Condizione di uscita

La fase termina quando è stato definito e autorizzato un primo comportamento osservabile del dominio data, con input, output, vincoli e criterio di verifica espliciti.
