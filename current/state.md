# Stato operativo

Questo file registra esclusivamente fatti, decisioni approvate e avanzamento dell'esperimento corrente.

## Fatti

- Il repository precedente era un prototipo centrato su un'ontologia non ancora giustificata da casi d'uso.
- È stata approvata una rifondazione senza compatibilità con quella struttura.
- Il materiale precedente resta disponibile nella cronologia Git.
- Il primo problema osservato è la presenza di più fonti autoritative concorrenti sullo stesso stato, sulle stesse regole e sugli stessi criteri.
- Il problema è stato osservato nel README e nei documenti attivi durante la prima rifondazione.

## Decisioni approvate

- Ogni responsabilità deve avere una sola fonte autoritativa.
- Il README non è una fonte autoritativa e serve esclusivamente alla navigazione.
- Le modifiche al repository richiedono autorizzazione esplicita.
- Fatti, decisioni, ipotesi e proposte devono restare distinguibili.

## Esperimento corrente

- fase: `eliminazione-autorita-concorrenti`
- contratto operativo: [`task-contract.md`](task-contract.md)
- trasformazione sottoposta a prova: [`transformation-contract.md`](transformation-contract.md)
- caso di verifica: [`../tests/first-behavior-case.md`](../tests/first-behavior-case.md)
- esito: `eseguito-con-correzione`

## Condizione di uscita

La fase termina quando il repository è stato verificato e ogni contenuto normativo, operativo o di stato dispone di una sola fonte autoritativa identificabile.