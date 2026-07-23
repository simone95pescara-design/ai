# AI Method Knowledge Base

Questo repository contiene la **specifica ufficiale** del metodo.

Non è un deposito di appunti, idee grezze o materiale esplorativo. Un contenuto entra nel repository solo quando ha raggiunto un livello di maturità sufficiente per diventare parte stabile e verificabile del modello.

## Struttura

```text
ontology/       Concetti normativi del modello
specification/  Regole normative che governano l'ontologia
reviews/        Audit e verifiche della specifica
patterns/       Configurazioni ricorrenti costruite sull'ontologia
examples/       Applicazioni illustrative e non normative
glossary/       Definizioni terminologiche sintetiche
```

Tutti i nomi dei file usano il minuscolo. Gli identificatori ontologici interni, come `STATE` e `TRANSITION`, restano invece in maiuscolo.

## Principi di governo

1. `ontology/` contiene esclusivamente i concetti del dominio.
2. `specification/` definisce schema, metamodello, relazioni e ciclo di vita.
3. `reviews/` contiene audit e artefatti di verifica, non norme ontologiche.
4. `patterns/` dipende dall'ontologia e non può contraddirla.
5. `examples/` chiarisce il metodo ma non introduce regole.
6. `glossary/` sintetizza termini già definiti altrove.
7. Il materiale ancora in esplorazione resta fuori dalla specifica ufficiale.

## Documenti normativi trasversali

| Documento | Funzione |
|---|---|
| [`schema.md`](specification/schema.md) | Struttura obbligatoria delle schede ontologiche |
| [`metamodello.md`](specification/metamodello.md) | Invarianti globali e separazione delle responsabilità |
| [`relazioni.md`](specification/relazioni.md) | Vocabolario tipizzato delle relazioni ammesse |
| [`lifecycle.md`](specification/lifecycle.md) | Introduzione, revisione, promozione, versionamento e deprecazione |

L'audit corrente è registrato in [`reviews/ontology-review.md`](reviews/ontology-review.md).

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

L'audit ha rilevato come blocchi principali:

1. dipendenze costitutive sovradichiarate;
2. relazioni non normalizzate rispetto a `relazioni.md`;
3. riferimenti obsoleti a concetti indicati come futuri;
4. sovrapposizione parziale tra invarianti, precondizioni, guardie e `CONSTRAINT`;
5. necessità di consolidare la catena causale `DECISION|ACTION → TRIGGER → TRANSITION → STATE`.

Nessuna entità può essere promossa a `stable` prima dell'applicazione delle correzioni registrate nell'audit.
