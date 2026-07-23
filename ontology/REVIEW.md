# Revisione incrociata del nucleo ontologico

Questo documento registra l'audit normativo del nucleo rispetto a [`SCHEMA.md`](SCHEMA.md), [`METAMODEL.md`](METAMODEL.md), [`RELATIONS.md`](RELATIONS.md) e [`LIFECYCLE.md`](LIFECYCLE.md).

## Stato

- fase: revisione incrociata
- esito: non ancora congelabile
- promozioni a `stable`: nessuna

## Criteri applicati

Ogni scheda viene verificata rispetto a:

1. responsabilità semantica unica;
2. distinzione tra dipendenza costitutiva e semplice relazione;
3. assenza di cicli costitutivi;
4. uso esclusivo di relazioni tipizzate;
5. verificabilità di attributi, invarianti e regole di validazione;
6. coerenza tra definizione, esempio e controesempio;
7. conformità dello stato documentale.

## Risultati trasversali

### R1 — Dipendenze sovradichiarate

Diverse schede dichiarano come `dipendenze` concetti che sono soltanto oggetti di relazione. Il metadato DEVE esprimere una necessità semantica costitutiva, non tutti i concetti citati.

Correzione richiesta:

- ridurre le dipendenze al minimo necessario per comprendere autonomamente il concetto;
- rappresentare gli altri collegamenti nella sezione `Relazioni`;
- verificare il grafo risultante come DAG.

### R2 — Relazioni non normalizzate

Le sezioni `Relazioni` contengono verbi generici o non definiti, tra cui `ammette`, `rifiuta`, `autorizza`, `collega`, `è soggetto a` e `rende valutabile`.

Correzione richiesta:

- usare le relazioni normative di [`RELATIONS.md`](RELATIONS.md), in particolare `abilita`, `limita`, `trasforma`, `produce`, `esegue`, `supporta`, `seleziona`, `soddisfa`, `viola`, `contribuisce_a`, `mitiga` e `compensa`;
- aggiungere una nuova relazione al vocabolario solo quando nessuna relazione esistente esprime correttamente il significato.

### R3 — Riferimenti storici non più validi

Alcune schede qualificano ancora altri concetti come “futuri” o dichiarano le relative relazioni informative e non normative. Tutti i concetti del nucleo sono ora presenti.

Correzione richiesta:

- eliminare il linguaggio temporaneo;
- rendere normative le relazioni conformi;
- mantenere `draft` finché le questioni aperte non sono risolte.

### R4 — Ambiguità tra attributi locali e `CONSTRAINT`

Precondizioni, guardie, invarianti e vincoli sono usati come categorie parzialmente sovrapposte.

Decisione architetturale richiesta:

- mantenere invarianti, precondizioni e guardie come predicati locali specializzati;
- usare `CONSTRAINT` per regole riusabili o trasversali;
- vietare la duplicazione della stessa regola senza motivazione esplicita.

### R5 — Effetti e causalità

Il nucleo separa correttamente `DECISION`, `ACTION` e `TRANSITION`, ma deve normalizzare il modo in cui una decisione o un'azione produce fatti elaborabili.

Regola proposta:

- `DECISION` e `ACTION` possono `produrre` un `TRIGGER` soltanto quando il trigger rappresenta un fatto avvenuto;
- soltanto `TRIGGER` `abilita` `TRANSITION`;
- soltanto `TRANSITION` `trasforma` `STATE`.

## Revisione delle schede

### `STATE`

Esito: conforme nella responsabilità primaria; revisione necessaria.

Problemi:

- la sezione `Relazioni` usa termini non normalizzati;
- `trigger_consentiti`, `azioni_consentite` e `azioni_vietate` mescolano attributi di configurazione e relazioni ontologiche;
- il riferimento a osservazioni “non ancora definite” è obsoleto.

Correzioni:

- esprimere `TRANSITION trasforma STATE` come relazione primaria;
- modellare l'ammissibilità tramite `CONSTRAINT limita TRIGGER|ACTION|TRANSITION` oppure tramite predicati locali espliciti;
- chiarire che lo stato non produce autonomamente osservazioni.

### `TRIGGER`

Esito: definizione e invarianti sostanzialmente conformi; relazioni da normalizzare.

Problemi:

- `rende valutabile` DEVE diventare `abilita`;
- “rilevato attraverso `OBSERVATION`” non specifica direzione e semantica;
- la dipendenza da `STATE` deve essere motivata come costitutiva oppure rimossa.

Correzioni:

- `TRIGGER abilita TRANSITION`;
- `ACTION produce TRIGGER` e `DECISION produce TRIGGER` quando rappresentano fatti completati;
- una `OBSERVATION` può `deriva_da` o `supporta` l'accertamento del fatto, senza coincidere con il trigger.

### `TRANSITION`

Esito: responsabilità primaria conforme; dipendenze e relazioni da consolidare.

Problemi:

- `collega` e `autorizza` non appartengono al vocabolario;
- i vincoli sono normativamente richiesti ma `CONSTRAINT` non è dichiarato come dipendenza;
- le azioni associate introducono un possibile accoppiamento procedurale.

Correzioni:

- `TRIGGER abilita TRANSITION`;
- `TRANSITION trasforma STATE` sorgente in `STATE` destinazione;
- `CONSTRAINT limita TRANSITION`;
- le azioni conseguenti DEVONO essere modellate separatamente e attivate da fatti osservabili, non incorporate come parte atomica del cambio di stato.

### `ACTION`

Esito: separazione da stato e transizione conforme; relazioni da normalizzare.

Problemi:

- `autorizzata`, `ammessa` e `vietata` non sono relazioni normative;
- i riferimenti a concetti “futuri” sono obsoleti;
- la dipendenza da `TRANSITION` appare relazionale, non necessariamente costitutiva.

Correzioni:

- un esecutore `esegue ACTION`;
- `ACTION produce TRIGGER` e può `produrre OBSERVATION` o `EVIDENCE` quando l'output ne soddisfa i requisiti;
- `CONSTRAINT limita ACTION`;
- `ACTION compensa ACTION` solo quando la compensazione è esplicitamente dichiarata.

### `CONSTRAINT`

Esito: responsabilità dichiarativa conforme; dipendenze e tassonomie ancora aperte.

Problemi:

- le dipendenze da tutte le entità vincolabili sono sovradichiarate;
- alcune formulazioni usano relazioni diverse da `limita` e `viola`;
- severità, conflitti e indisponibilità dei dati non sono ancora normati.

Correzioni:

- valutare `dipendenze: []` come configurazione di base;
- usare `CONSTRAINT limita <entità>`;
- usare `<entità> viola CONSTRAINT` quando il predicato obbligatorio risulta falso;
- definire tassonomia minima di severità prima della promozione.

### `OBJECTIVE`

Esito preliminare: mantenere distinto da stato, azione e decisione.

Verifiche obbligatorie:

- condizione di soddisfazione osservabile;
- `STATE soddisfa OBJECTIVE` oppure `ACTION contribuisce_a OBJECTIVE`;
- assenza di prescrizioni sul percorso;
- dipendenze ridotte alle sole necessità costitutive.

### `OBSERVATION`

Esito preliminare: mantenere distinta da fatto ontologico, interpretazione ed evidenza.

Verifiche obbligatorie:

- sorgente e riferimento temporale obbligatori;
- contenuto rilevato separato dalla regola di interpretazione;
- `OBSERVATION deriva_da` una sorgente o misura identificabile;
- nessuna modifica di stato o decisione implicita.

### `EVIDENCE`

Esito preliminare: supporto epistemico, non verità automatica.

Verifiche obbligatorie:

- provenienza, integrità e oggetto supportato;
- uso di `supporta`, `contraddice` o `giustifica` con criterio di sufficienza;
- distinzione da `OBSERVATION`;
- dipendenze non circolari rispetto a `DECISION`.

### `DECISION`

Esito preliminare: scelta separata dall'esecuzione.

Verifiche obbligatorie:

- decisore, alternative ed esito;
- `DECISION seleziona ACTION` o altra alternativa tipizzata;
- eventuale `DECISION produce TRIGGER` soltanto dopo la registrazione del fatto decisionale;
- nessuna modifica diretta di `STATE`.

### `RISK`

Esito preliminare: possibilità distinta dall'evento verificato.

Verifiche obbligatorie:

- evento potenziale, conseguenza, oggetto esposto, probabilità e impatto;
- `ACTION`, `CONSTRAINT` o controllo `mitiga RISK`;
- separazione tra rischio, violazione, osservazione ed evidenza;
- criteri di valutazione dichiarati.

## Grafo costitutivo proposto

Il seguente grafo minimo è la base della successiva normalizzazione:

```text
STATE
TRIGGER
CONSTRAINT
OBJECTIVE
OBSERVATION

STATE + TRIGGER + CONSTRAINT -> TRANSITION
STATE + CONSTRAINT           -> ACTION
OBSERVATION                  -> EVIDENCE
OBSERVATION + EVIDENCE
+ OBJECTIVE + CONSTRAINT
+ RISK                       -> DECISION
OBJECTIVE + OBSERVATION      -> RISK
```

Il grafo è una proposta di revisione e NON modifica ancora i metadati delle singole schede.

## Blocchi alla promozione

Nessuna scheda DEVE essere promossa a `stable` finché non sono completati:

1. normalizzazione delle relazioni;
2. riduzione e motivazione delle dipendenze;
3. eliminazione dei riferimenti temporanei a concetti futuri;
4. decisione sulla semantica di guardie, precondizioni e vincoli;
5. risoluzione delle questioni aperte bloccanti;
6. verifica completa delle cinque schede epistemiche e decisionali.

## Prossima modifica normativa

La successiva fase DEVE applicare le correzioni alle singole schede in questo ordine:

1. `CONSTRAINT`;
2. `STATE`;
3. `TRIGGER`;
4. `TRANSITION`;
5. `ACTION`;
6. `OBJECTIVE`;
7. `OBSERVATION`;
8. `EVIDENCE`;
9. `RISK`;
10. `DECISION`.

L'ordine parte dai concetti con minori dipendenze e minimizza le riscritture successive.