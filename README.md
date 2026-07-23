# AI Method Knowledge Base

Questo repository contiene la **specifica ufficiale** del metodo.

Non è un deposito di appunti, idee grezze o materiale esplorativo. Un contenuto entra nel repository solo quando ha raggiunto un livello di maturità sufficiente per diventare parte stabile e verificabile del modello.

## Struttura

```text
ontology/   Concetti normativi e regole di governo del modello
patterns/   Configurazioni ricorrenti costruite sull'ontologia
examples/   Applicazioni illustrative e non normative
glossary/   Definizioni terminologiche sintetiche
```

## Principi di governo

1. `ontology/` è normativa: definisce i concetti ammessi, le loro relazioni e le regole globali del modello.
2. `patterns/` dipende dall'ontologia e non può contraddirla.
3. `examples/` chiarisce il metodo ma non introduce regole.
4. `glossary/` sintetizza termini già definiti altrove.
5. Il materiale ancora in esplorazione resta fuori dalla specifica ufficiale.
6. Ogni scheda ontologica deve rispettare il contratto definito in [`ontology/SCHEMA.md`](ontology/SCHEMA.md).
7. Tutte le schede devono rispettare il [`metamodello`](ontology/METAMODEL.md), il [vocabolario delle relazioni](ontology/RELATIONS.md) e il [ciclo di vita della specifica](ontology/LIFECYCLE.md).

## Documenti normativi trasversali

| Documento | Funzione |
|---|---|
| [`SCHEMA.md`](ontology/SCHEMA.md) | Struttura obbligatoria delle schede ontologiche |
| [`METAMODEL.md`](ontology/METAMODEL.md) | Invarianti globali e separazione delle responsabilità |
| [`RELATIONS.md`](ontology/RELATIONS.md) | Vocabolario tipizzato delle relazioni ammesse |
| [`LIFECYCLE.md`](ontology/LIFECYCLE.md) | Introduzione, revisione, promozione, versionamento e deprecazione |
| [`REVIEW.md`](ontology/REVIEW.md) | Audit incrociato, anomalie rilevate e ordine delle correzioni normative |

## Ciclo di maturità

Ogni concetto attraversa questi stati documentali:

- `draft`: definizione in consolidamento, non ancora normativa;
- `stable`: definizione approvata e normativa;
- `deprecated`: definizione mantenuta per compatibilità, ma non utilizzabile per nuovi modelli.

Il passaggio a `stable` richiede:

- definizione non ambigua;
- confini espliciti rispetto ai concetti vicini;
- attributi e invarianti verificabili;
- relazioni coerenti con le altre schede;
- almeno un esempio valido e un controesempio;
- assenza di questioni semantiche aperte;
- conformità ai documenti normativi trasversali.

## Nucleo ontologico

| ID | Concetto | Stato | Dipendenze |
|---|---|---|---|
| [`STATE`](ontology/stato.md) | Stato | `draft` | — |
| [`TRIGGER`](ontology/trigger.md) | Trigger | `draft` | `STATE` |
| [`TRANSITION`](ontology/transizione.md) | Transizione | `draft` | `STATE`, `TRIGGER` |
| [`ACTION`](ontology/azione.md) | Azione | `draft` | `STATE`, `TRIGGER`, `TRANSITION` |
| [`CONSTRAINT`](ontology/vincolo.md) | Vincolo | `draft` | `STATE`, `TRIGGER`, `TRANSITION`, `ACTION` |
| [`OBJECTIVE`](ontology/obiettivo.md) | Obiettivo | `draft` | `STATE`, `ACTION`, `CONSTRAINT` |
| [`OBSERVATION`](ontology/osservazione.md) | Osservazione | `draft` | `STATE`, `TRIGGER`, `CONSTRAINT` |
| [`DECISION`](ontology/decisione.md) | Decisione | `draft` | `OBSERVATION`, `OBJECTIVE`, `CONSTRAINT`, `ACTION`, `TRIGGER` |
| [`EVIDENCE`](ontology/evidenza.md) | Evidenza | `draft` | `OBSERVATION`, `DECISION`, `CONSTRAINT` |
| [`RISK`](ontology/rischio.md) | Rischio | `draft` | `OBJECTIVE`, `CONSTRAINT`, `OBSERVATION`, `EVIDENCE`, `DECISION` |

Il nucleo distingue condizione persistente, fatto attivante, cambiamento di stato, effetto operativo, limite normativo, risultato desiderato, rilevazione, scelta, supporto epistemico e possibilità di conseguenze indesiderate.

## Catena concettuale

```text
OBSERVATION ──► EVIDENCE ──► DECISION ──► TRIGGER ──► TRANSITION ──► STATE
       │              │             │                                      │
       └──────────────┴─────────────┘                                      ├── abilita ACTION
                                                                           └── contribuisce a OBJECTIVE

CONSTRAINT limita tutte le entità applicabili.
RISK valuta possibili conseguenze rispetto a OBJECTIVE e interessi protetti.
```

## Stato della revisione

La revisione incrociata è formalmente registrata in [`ontology/REVIEW.md`](ontology/REVIEW.md).

L'audit ha rilevato come blocchi principali:

1. dipendenze costitutive sovradichiarate;
2. relazioni non normalizzate rispetto a `RELATIONS.md`;
3. riferimenti obsoleti a concetti indicati come futuri;
4. sovrapposizione parziale tra invarianti, precondizioni, guardie e `CONSTRAINT`;
5. necessità di consolidare la catena causale `DECISION|ACTION → TRIGGER → TRANSITION → STATE`.

Nessuna entità può essere promossa a `stable` prima dell'applicazione delle correzioni registrate nell'audit.