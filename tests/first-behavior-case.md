# Primo caso di verifica

## Problema osservato

Il README e i documenti attivi contenevano descrizioni concorrenti dello stato, delle regole operative, delle ipotesi e dei criteri. Di conseguenza, più file potevano essere interpretati come fonti autoritative sulla stessa responsabilità.

## Evidenza iniziale

Nel primo tentativo di rifondazione:

- il README dichiarava lo stato corrente;
- il README prescriveva l'ordine operativo;
- il README conteneva regole di ammissione;
- `state.md`, `task-contract.md` e `transformation-contract.md` ripetevano ipotesi, divieti e criteri.

## Trasformazione verificata

```text
fonti autoritative concorrenti
→ una sola fonte autoritativa per responsabilità
```

## Intervento eseguito

- `README.md` è stato ridotto a indice non autoritativo;
- `state.md` è stato limitato a stato operativo, fatti, decisioni e avanzamento;
- `task-contract.md` è stato limitato all'autorità operativa;
- `transformation-contract.md` è stato limitato alla trasformazione candidata;
- questo file conserva il problema osservato, le evidenze e il criterio di verifica.

## Criteri di verifica

Il caso supera la verifica quando:

1. nessun contenuto normativo è definito nel README;
2. ogni responsabilità dispone di una sola fonte autoritativa;
3. gli altri documenti rinviano alla fonte senza duplicarne le prescrizioni;
4. un conflitto può essere risolto identificando la responsabilità coinvolta;
5. non sono stati introdotti nuovi file per duplicare contenuti esistenti.

## Risultato

`eseguito-con-correzione`

La prima revisione ha fallito perché il README e gli altri documenti mantenevano autorità sovrapposte. La correzione successiva ha separato le responsabilità. La verifica finale del repository resta necessaria prima di dichiarare il caso concluso.

## Decisione provvisoria

Mantenere l'ipotesi secondo cui ogni responsabilità deve avere una sola fonte autoritativa, subordinatamente alla verifica finale del diff e del contenuto risultante.