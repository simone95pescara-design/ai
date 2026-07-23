# Ciclo di vita della specifica

Questo documento definisce il processo normativo con cui le schede ontologiche vengono introdotte, revisionate, approvate, modificate e ritirate.

## 1. Stati ammessi

### `draft`

Una scheda in consolidamento.

- PUÒ contenere questioni aperte.
- PUÒ cambiare significato tra versioni minor.
- NON DEVE essere considerata normativa per implementazioni che richiedono stabilità.

### `stable`

Una scheda approvata e normativa.

- DEVE soddisfare tutti i criteri di [`SCHEMA.md`](SCHEMA.md).
- NON DEVE contenere questioni aperte.
- DEVE indicare `data_approvazione`.
- Le sue dipendenze DOVREBBERO essere `stable`, salvo eccezione documentata.

### `deprecated`

Una scheda ancora documentata ma non ammessa per nuovi modelli.

- DEVE indicare il motivo della deprecazione.
- DEVE indicare la sostituzione, quando esiste.
- DEVE mantenere sufficiente contenuto per interpretare modelli storici.
- NON DEVE essere eliminata finché esistono riferimenti normativi o modelli supportati che la utilizzano.

## 2. Introduzione di una scheda

Una nuova scheda DEVE:

1. usare un ID non assegnato;
2. dichiarare stato `draft` e versione iniziale;
3. rispettare la struttura obbligatoria;
4. motivare le dipendenze;
5. distinguersi dai concetti esistenti;
6. includere almeno un esempio e un controesempio;
7. essere aggiunta all'indice del repository.

## 3. Revisione incrociata

Prima della promozione a `stable`, ogni scheda DEVE essere verificata rispetto a:

- separazione delle responsabilità;
- coerenza con [`METAMODEL.md`](METAMODEL.md);
- uso delle relazioni definite in [`RELATIONS.md`](RELATIONS.md);
- assenza di dipendenze circolari costitutive;
- compatibilità con invarianti e regole di validazione delle dipendenze;
- verificabilità degli attributi;
- capacità di esempio e controesempio di discriminare il concetto.

## 4. Promozione a `stable`

La promozione richiede:

1. nessuna questione aperta;
2. definizione non ambigua;
3. confini completi;
4. invarianti verificabili;
5. relazioni tipizzate;
6. dipendenze risolte;
7. esempio valido e controesempio adeguati;
8. incremento di versione coerente;
9. valorizzazione di `data_approvazione`;
10. aggiornamento dell'indice e della documentazione trasversale.

La promozione DOVREBBE essere effettuata con una modifica dedicata e facilmente identificabile nella cronologia.

## 5. Versionamento

- `PATCH`: correzioni editoriali o chiarimenti senza modifica del significato normativo.
- `MINOR`: estensioni retrocompatibili, nuovi attributi opzionali o nuove relazioni ammesse.
- `MAJOR`: cambiamenti incompatibili a definizione, invarianti, attributi obbligatori o semantica delle relazioni.

Una modifica incompatibile a una scheda `stable` DEVE incrementare la versione major oppure introdurre una nuova scheda con sostituzione formale.

## 6. Modifica di una scheda stabile

Ogni modifica DEVE dichiarare:

- motivazione;
- impatto semantico;
- compatibilità con versioni precedenti;
- effetto sulle dipendenze;
- eventuale migrazione richiesta.

Una scheda `stable` NON DEVE tornare implicitamente a `draft`. Una revisione incompatibile DEVE seguire il processo di versionamento previsto.

## 7. Deprecazione

La deprecazione DEVE:

1. cambiare `stato_specifica` in `deprecated`;
2. valorizzare `data_approvazione` con la data della decisione di deprecazione;
3. indicare `sostituisce` o una sezione equivalente quando esiste un successore;
4. spiegare i rischi del mantenimento e il percorso di migrazione;
5. aggiornare tutte le tabelle e i riferimenti trasversali.

## 8. Freeze del nucleo

Il nucleo può essere dichiarato congelato quando:

- tutte le schede previste sono presenti;
- la revisione incrociata è completata;
- le dipendenze sono coerenti;
- le relazioni sono normalizzate;
- non restano contraddizioni note.

Il freeze NON equivale automaticamente alla promozione di tutte le schede a `stable`; indica che l'aggiunta di nuovi concetti richiede una motivazione architetturale esplicita.

## 9. Criterio di completamento

Una revisione del nucleo è completata solo quando ogni problema rilevato è:

- risolto;
- registrato come questione aperta in una scheda `draft`; oppure
- accettato esplicitamente come eccezione motivata.