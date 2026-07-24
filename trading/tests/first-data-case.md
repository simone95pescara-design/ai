# Primo caso verticale: dato OHLCV

## Problema osservato

Il dominio `data` è troppo ampio per essere progettato correttamente in anticipo. Serve un primo comportamento concreto che faccia emergere requisiti reali senza inventare l'intera architettura.

## Input

Una singola osservazione con:

- timestamp;
- open;
- high;
- low;
- close;
- volume.

## Trasformazione

```text
valori OHLCV non formalizzati
→ oggetto immutabile accettato o rifiutato da invarianti esplicite
```

## Criteri di accettazione

- un'osservazione valida viene costruita;
- un timestamp senza fuso viene rifiutato;
- un massimo inferiore a open o close viene rifiutato;
- il codice supera `black --check src tests`;
- il codice supera `ruff check src tests`;
- il codice supera `mypy` in modalità strict;
- i test superano `pytest`.

## Evidenza prevista

L'evidenza è il risultato del job GitHub Actions `quality` associato alla pull request.

## Decisione successiva

Solo dopo l'esito della CI si decide se:

- mantenere il modello;
- correggere invarianti o configurazione;
- rifiutare questa rappresentazione;
- autorizzare il caso successivo, probabilmente una collezione ordinata di osservazioni oppure un adapter per una fonte specifica.

## Stato

`in-attesa-di-ci`
