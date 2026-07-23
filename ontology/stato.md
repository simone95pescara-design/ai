---
id: STATE
nome: Stato
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze: []
sostituisce: null
---

# Stato (`STATE`)

## Definizione

Uno **stato** è una rappresentazione atomica e persistente di una condizione rilevante del sistema in un determinato istante o intervallo.

Lo stato descrive **come si trova il sistema**; non descrive ciò che il sistema esegue. Un cambiamento di stato avviene esclusivamente mediante una transizione valida, attivata da un trigger ammesso e soggetta ai vincoli applicabili.

## Scopo

`STATE` consente di:

- distinguere condizioni operative differenti;
- determinare quali trigger e azioni siano ammessi;
- rendere esplicite le condizioni di ingresso e di uscita;
- osservare e verificare l'evoluzione del sistema;
- impedire comportamenti non validi nel contesto corrente.

## Confini

Uno stato:

- include una sola condizione semantica principale;
- può persistere nel tempo;
- può esporre attributi osservabili e metriche;
- può limitare trigger, azioni e transizioni ammesse.

Uno stato NON è:

- un'azione;
- un evento o trigger;
- una transizione;
- un obiettivo;
- una sequenza procedurale;
- una descrizione generica priva di criteri verificabili.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore leggibile e non ambiguo dello stato. |
| `significato` | sì | Condizione semantica rappresentata. |
| `condizioni_ingresso` | sì | Predicati che devono risultare veri al momento dell'ingresso. |
| `condizioni_uscita` | sì | Predicati che consentono o impongono l'uscita. |
| `trigger_consentiti` | sì | Trigger che possono essere elaborati nello stato. |
| `azioni_consentite` | sì | Azioni eseguibili mentre il sistema si trova nello stato. |
| `azioni_vietate` | no | Divieti espliciti utili a prevenire interpretazioni errate. |
| `vincoli` | no | Condizioni che limitano permanenza, azioni o transizioni. |
| `output` | no | Informazioni osservabili associate allo stato. |
| `metriche` | no | Misure utilizzabili per monitoraggio o validazione. |

## Invarianti

1. Uno stato DEVE rappresentare una sola condizione semantica principale.
2. Uno stato NON DEVE eseguire autonomamente azioni.
3. Uno stato DEVE avere criteri osservabili che permettano di distinguerlo dagli stati adiacenti.
4. L'ingresso in uno stato DEVE avvenire attraverso una transizione valida, salvo lo stato iniziale del sistema.
5. L'uscita da uno stato DEVE avvenire attraverso una transizione valida.
6. Il cambio di stato DEVE essere associato a un trigger valido o a una condizione temporale formalmente modellata come trigger.
7. Durante la permanenza, tutte le invarianti e i vincoli dello stato DEVONO restare soddisfatti.
8. Due stati distinti NON DEVONO avere condizioni di validità semanticamente equivalenti.

## Relazioni

```yaml
entra_da: []
esce_verso: []
trigger_consentiti: []
azioni_consentite: []
azioni_vietate: []
vincoli: []
output: []
metriche: []
```

Relazioni previste:

- `STATE` è origine e destinazione di una futura entità `TRANSITION`;
- `STATE` ammette o rifiuta entità `TRIGGER`;
- `STATE` abilita o vieta entità `ACTION`;
- `STATE` è soggetto a entità `CONSTRAINT`;
- `STATE` può produrre o esporre `OBSERVATION` senza eseguire direttamente un'azione.

Le relazioni verso entità non ancora definite sono informative e non normative finché le relative schede non diventano stabili.

## Regole di validazione

Un'istanza di `STATE` è valida se e solo se:

1. il nome è univoco nel modello;
2. il significato è espresso come condizione e non come attività;
3. le condizioni di ingresso e uscita sono verificabili;
4. almeno un criterio osservabile permette di stabilire se il sistema si trova nello stato;
5. trigger e azioni ammessi non contraddicono i vincoli;
6. lo stato non combina fasi indipendenti o separabili;
7. ogni destinazione dichiarata è raggiungibile tramite una transizione esplicita;
8. ogni provenienza dichiarata corrisponde a una transizione esplicita.

## Esempio valido

### `IN_ATTESA_APPROVAZIONE`

```yaml
nome: IN_ATTESA_APPROVAZIONE
significato: La richiesta è completa ed è stata inviata, ma non è ancora stata approvata o rifiutata.
condizioni_ingresso:
  - richiesta_completa == true
  - richiesta_inviata == true
  - esito == null
condizioni_uscita:
  - esito in [APPROVATA, RIFIUTATA]
trigger_consentiti:
  - APPROVAZIONE_RICEVUTA
  - RIFIUTO_RICEVUTO
azioni_consentite:
  - CONSULTA_RICHIESTA
  - ANNULLA_RICHIESTA
azioni_vietate:
  - ESEGUI_RICHIESTA
vincoli:
  - una sola decisione finale può essere registrata
output:
  - tempo_in_attesa
metriche:
  - durata_attesa
```

La definizione rappresenta una condizione persistente, osservabile e distinta dalle attività che possono avvenire durante la permanenza.

## Controesempio

### `VALIDARE_E_APPROVARE_RICHIESTA`

Non è uno stato valido perché descrive due azioni e una sequenza procedurale. Può essere scomposto in azioni, trigger, transizioni e stati distinti, per esempio `IN_VALIDAZIONE` e `IN_ATTESA_APPROVAZIONE`.

## Questioni aperte

1. Stabilire se ogni stato debba dichiarare esplicitamente una durata massima oppure se tale proprietà appartenga esclusivamente ai vincoli.
2. Definire il trattamento degli stati composti e paralleli: esclusione dal nucleo oppure modellazione tramite un costrutto separato.
3. Stabilire se le osservazioni associate allo stato siano proprietà dello stato o entità autonome collegate.