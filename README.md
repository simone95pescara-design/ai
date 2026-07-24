# AI Work Protocol

Questo repository sviluppa e verifica un protocollo di lavoro per esecutori umani o artificiali.

Il protocollo non assume in anticipo un'ontologia, un'architettura o un insieme definitivo di categorie. Ogni elemento entra nel repository solo quando risponde a un problema osservato e dispone di un criterio di verifica.

## Stato attuale

Il repository è in fase di rifondazione sperimentale.

Il nucleo attivo contiene soltanto:

- lo stato operativo corrente;
- il contratto dell'attività corrente;
- l'ipotesi di trasformazione corrente;
- un caso di verifica comportamentale.

Il prototipo precedente è stato rimosso dalla branch di rifondazione. Rimane disponibile esclusivamente nella cronologia Git.

## Come lavorare sul repository

Prima di operare, un esecutore deve leggere nell'ordine:

1. [`current/state.md`](current/state.md);
2. [`current/task-contract.md`](current/task-contract.md);
3. [`current/transformation-contract.md`](current/transformation-contract.md);
4. il caso di verifica applicabile in [`tests/`](tests/).

L'esecutore deve distinguere fatti, decisioni, ipotesi e proposte; dichiarare le assunzioni residue; rispettare i limiti di autorità; definire la trasformazione richiesta prima di proporre una soluzione; verificare l'output prima di considerare conclusa l'attività.

## Regola di ammissione

Un nuovo file o una nuova regola sono ammessi solo quando:

1. rispondono a un'esigenza osservata;
2. hanno una responsabilità unica;
3. non duplicano un'altra fonte;
4. dichiarano il proprio stato epistemico;
5. possono essere verificati mediante un caso concreto.

Le strutture presenti non sono definitive. La loro permanenza dipende dai risultati degli esperimenti.
