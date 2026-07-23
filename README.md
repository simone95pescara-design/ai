# AI Method Knowledge Base

Questo repository contiene la **specifica ufficiale** del metodo.

Non è un deposito di appunti, idee grezze o materiale esplorativo. Un contenuto entra nel repository solo quando ha raggiunto un livello di maturità sufficiente per diventare parte stabile e verificabile del modello.

## Struttura

```text
ontology/   Concetti normativi del modello
patterns/   Configurazioni ricorrenti costruite sull'ontologia
examples/   Applicazioni illustrative e non normative
glossary/   Definizioni terminologiche sintetiche
```

## Principi di governo

1. `ontology/` è normativa: definisce i concetti ammessi e le loro relazioni.
2. `patterns/` dipende dall'ontologia e non può contraddirla.
3. `examples/` chiarisce il metodo ma non introduce regole.
4. `glossary/` sintetizza termini già definiti altrove.
5. Il materiale ancora in esplorazione resta fuori dalla specifica ufficiale.
6. Ogni scheda ontologica deve rispettare il contratto definito in [`ontology/SCHEMA.md`](ontology/SCHEMA.md).

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
- assenza di questioni semantiche aperte.

## Primo nucleo ontologico

La prima entità definita è [`STATE`](ontology/stato.md), perché trigger, transizioni e azioni dipendono dalla nozione di stato.