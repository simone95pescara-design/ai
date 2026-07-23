# Relazioni ontologiche

Questo documento definisce il vocabolario normativo delle relazioni ammesse tra i concetti dell'ontologia.

## Regole generali

- Ogni relazione DEVE essere direzionale, tipizzata e semanticamente verificabile.
- Il soggetto e l'oggetto della relazione DEVONO essere identificabili.
- Una relazione NON DEVE implicare effetti ulteriori rispetto a quelli dichiarati.
- Quando esiste una relazione specifica, NON DOVREBBE essere sostituita da termini generici come `usa`, `coinvolge` o `collega`.

## Vocabolario

### `produce`

Il soggetto genera un'entità distinta come risultato osservabile.

Esempio: una `ACTION` produce un `TRIGGER`.

### `abilita`

Il soggetto rende possibile la valutazione o l'esecuzione dell'oggetto senza garantirne l'esito.

Esempio: un `TRIGGER` abilita una `TRANSITION`.

### `trasforma`

Il soggetto realizza il passaggio tra una condizione sorgente e una condizione destinazione.

Questa relazione è riservata a `TRANSITION` rispetto a `STATE`.

### `esegue`

Un attore o esecutore realizza operativamente una `ACTION`.

### `limita`

Il soggetto restringe l'insieme delle configurazioni, decisioni o comportamenti ammissibili dell'oggetto.

Esempio: un `CONSTRAINT` limita una `DECISION`.

### `soddisfa`

Il soggetto realizza o dimostra la condizione verificabile definita dall'oggetto.

Esempio: uno `STATE` soddisfa un `OBJECTIVE`.

### `viola`

Il soggetto rende falso un criterio obbligatorio definito dall'oggetto.

Esempio: una `ACTION` viola un `CONSTRAINT`.

### `osserva`

Il soggetto rileva una proprietà, un evento o una condizione dell'oggetto senza modificarlo.

### `deriva_da`

Il soggetto è ottenuto mediante trasformazione, aggregazione o inferenza esplicita a partire dall'oggetto.

Questa relazione DEVE dichiarare la regola di derivazione quando non è immediata.

### `supporta`

Il soggetto aumenta la giustificazione di un'affermazione, osservazione, decisione o valutazione senza renderla automaticamente vera.

Esempio: una `EVIDENCE` supporta una `DECISION`.

### `contraddice`

Il soggetto è incompatibile con il contenuto o la conclusione dell'oggetto secondo un criterio dichiarato.

### `giustifica`

Il soggetto fornisce una motivazione esplicita sufficiente, secondo il modello, per l'oggetto.

`giustifica` è più forte di `supporta` e DEVE essere usata solo quando il criterio di sufficienza è dichiarato.

### `seleziona`

Il soggetto sceglie l'oggetto tra alternative esplicitamente considerate.

Esempio: una `DECISION` seleziona una `ACTION`.

### `contribuisce_a`

Il soggetto produce un effetto parziale e non sufficiente verso la soddisfazione dell'oggetto.

Esempio: una `ACTION` contribuisce a un `OBJECTIVE`.

### `espone_a`

Il soggetto rende l'oggetto vulnerabile a un `RISK` o ne aumenta l'esposizione.

### `mitiga`

Il soggetto riduce probabilità, impatto o esposizione associati a un `RISK`.

### `compensa`

Il soggetto contrasta gli effetti di un'operazione precedente senza cancellarne necessariamente l'accadimento storico.

## Relazioni da evitare

Le seguenti espressioni NON DOVREBBERO comparire come relazioni normative senza una definizione locale più precisa:

- `usa`;
- `gestisce`;
- `coinvolge`;
- `riguarda`;
- `dipende da`, quando si intende una relazione operativa e non il metadato ontologico `dipendenze`;
- `è collegato a`.

## Validazione

Una relazione è conforme quando:

1. appartiene al vocabolario normativo oppure è definita esplicitamente nella scheda;
2. ha soggetto, oggetto e direzione chiari;
3. non duplica una relazione più specifica;
4. non introduce causalità implicita;
5. può essere verificata su un'istanza del modello.