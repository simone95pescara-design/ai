# Trasformazione corrente

## Stato epistemico

`ipotesi-in-verifica`

## Formulazione

```text
assenza di un dato di mercato formalizzato
→ rappresentazione OHLCV con invarianti verificabili automaticamente
```

## Stato iniziale

Il sistema non possiede ancora un contratto software che stabilisca cosa renda valida una singola osservazione OHLCV.

## Stato finale desiderato

Esiste un tipo `Candle` immutabile che:

- usa timestamp UTC consapevoli del fuso;
- rappresenta prezzi e volume con `Decimal`;
- rifiuta intervalli di prezzo incoerenti;
- rifiuta volumi negativi;
- è coperto da test automatici;
- supera formato, lint e controllo statico dei tipi.

## Fuori ambito

- download da provider esterni;
- persistenza;
- aggregazione dei timeframe;
- gestione di dataset completi;
- segnali, strategie, backtest, rischio ed esecuzione;
- agenti AI e orchestrazione.

## Limite

Questo contratto non definisce l'intero dominio data. Definisce soltanto il primo comportamento software osservabile necessario per farlo emergere progressivamente.
