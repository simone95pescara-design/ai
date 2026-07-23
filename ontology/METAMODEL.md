# Metamodello ontologico

Questo documento definisce le regole globali che governano tutte le schede in `ontology/`. Le singole schede NON DEVONO contraddire queste regole.

## 1. Identità dei concetti

- Ogni concetto DEVE avere un `id` univoco, stabile e scritto in maiuscolo.
- Un `id` NON DEVE essere riutilizzato per un significato incompatibile.
- Ogni concetto DEVE avere una responsabilità semantica primaria distinguibile dalle altre entità.

## 2. Separazione delle responsabilità

- `STATE` rappresenta una condizione persistente.
- `TRIGGER` rappresenta un fatto osservabile che abilita una valutazione.
- `TRANSITION` è l'unico costrutto che PUÒ modificare lo stato.
- `ACTION` rappresenta un effetto operativo e NON DEVE modificare direttamente lo stato.
- `CONSTRAINT` limita ciò che è ammissibile e NON DEVE eseguire comportamento.
- `OBJECTIVE` descrive un risultato desiderato verificabile e NON DEVE prescrivere il percorso per raggiungerlo.
- `OBSERVATION` rappresenta una rilevazione e NON DEVE coincidere con la sua interpretazione.
- `EVIDENCE` supporta un'affermazione, un'osservazione o una decisione e NON DEVE sostituirsi al decisore.
- `DECISION` seleziona un'alternativa e NON DEVE coincidere con l'esecuzione dell'azione selezionata.
- `RISK` rappresenta una possibilità di conseguenza indesiderata e NON DEVE essere trattato come evento già avvenuto.

## 3. Causalità esplicita

- Ogni cambiamento di stato DEVE essere riconducibile a una `TRANSITION` identificabile.
- Ogni `TRANSITION` DEVE dichiarare almeno uno stato sorgente, uno stato destinazione e le condizioni di abilitazione.
- Gli effetti operativi DEVONO essere rappresentati come `ACTION` distinte dalle transizioni.
- Le decisioni che influenzano il comportamento del sistema DOVREBBERO essere tracciabili tramite relazioni tipizzate.
- Nessuna entità PUÒ introdurre effetti impliciti non rappresentati nel modello.

## 4. Dipendenze

- Le dipendenze dichiarate nei metadati DEVONO riferirsi esclusivamente a ID ontologici esistenti.
- Una dipendenza indica necessità semantica, non semplice collegamento occasionale.
- Le dipendenze DOVREBBERO formare un grafo aciclico.
- Un ciclo è ammesso solo se documentato come relazione reciproca non costitutiva e NON DEVE impedire la comprensione autonoma delle entità coinvolte.

## 5. Verificabilità

- Ogni attributo obbligatorio DEVE essere verificabile.
- Ogni invariante DEVE poter essere valutato come soddisfatto o violato.
- Ogni `OBJECTIVE` DEVE definire una condizione di soddisfazione osservabile.
- Ogni `CONSTRAINT` DEVE definire un predicato o criterio di conformità valutabile.
- Ogni `OBSERVATION` DEVE avere una sorgente e un riferimento temporale.
- Ogni `EVIDENCE` DEVE dichiarare ciò che supporta e la propria provenienza.
- Ogni `DECISION` DEVE dichiarare decisore, alternative considerate ed esito.
- Ogni `RISK` DEVE dichiarare almeno evento potenziale, conseguenza e oggetto esposto.

## 6. Relazioni

- Le relazioni tra concetti DEVONO usare il vocabolario definito in [`RELATIONS.md`](RELATIONS.md).
- Ogni relazione DEVE avere direzione e significato non ambiguo.
- Relazioni generiche come `usa`, `coinvolge` o `dipende da` NON DOVREBBERO essere impiegate quando esiste una relazione più precisa.

## 7. Conformità documentale

- Ogni scheda ontologica DEVE rispettare [`SCHEMA.md`](SCHEMA.md).
- Lo stato e l'evoluzione delle schede DEVONO rispettare [`LIFECYCLE.md`](LIFECYCLE.md).
- Gli esempi NON DEVONO introdurre regole assenti dalle sezioni normative.
- Le questioni aperte sono ammesse esclusivamente nelle schede `draft`.

## 8. Validazione del nucleo

Il nucleo ontologico è coerente quando:

1. ogni concetto ha responsabilità distinta;
2. le dipendenze sono motivate e prive di cicli costitutivi;
3. tutte le relazioni sono tipizzate;
4. ogni cambiamento di stato passa da `TRANSITION`;
5. decisione, esecuzione ed evoluzione dello stato restano separati;
6. osservazioni, evidenze, obiettivi, vincoli e rischi sono verificabili;
7. nessuna scheda contraddice un'invariante globale.