---
id: CONSTRAINT
nome: Vincolo
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - STATE
  - TRIGGER
  - TRANSITION
  - ACTION
sostituisce: null
---

# Vincolo (`CONSTRAINT`)

## Definizione

Un **vincolo** è una regola dichiarativa, verificabile e applicabile a una o più entità del modello, che limita, vieta o condiziona la loro validità, ammissibilità o esecuzione.

Il vincolo descrive **ciò che deve o non deve essere vero**. Non rappresenta un comportamento, non esegue azioni e non modifica direttamente lo stato del sistema.

## Scopo

`CONSTRAINT` consente di:

- formalizzare limiti trasversali applicabili a più entità;
- distinguere le condizioni normative dalle precondizioni locali;
- impedire stati, trigger, transizioni o azioni non ammissibili;
- rendere verificabili regole temporali, quantitative, autorizzative o di coerenza;
- associare una conseguenza esplicita alla violazione di una regola.

## Confini

Un vincolo:

- esprime una singola regola normativa principale;
- ha un ambito di applicazione dichiarato;
- è valutabile tramite un predicato o criterio verificabile;
- può essere sempre applicabile oppure attivo solo in determinate condizioni;
- può vietare, imporre o limitare una configurazione o un comportamento;
- può dichiarare severità e conseguenze della violazione.

Un vincolo NON è:

- uno stato;
- un trigger;
- una transizione;
- un'azione;
- una decisione;
- un obiettivo;
- una preferenza non vincolante;
- una descrizione generica priva di criteri di verifica.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore leggibile e univoco del vincolo. |
| `significato` | sì | Regola normativa rappresentata. |
| `ambito` | sì | Entità, istanze o contesti ai quali il vincolo si applica. |
| `predicato` | sì | Condizione verificabile che determina il rispetto del vincolo. |
| `tipo` | sì | Natura del vincolo, per esempio divieto, obbligo o limite. |
| `attivazione` | no | Condizioni nelle quali il vincolo diventa applicabile. |
| `severita` | sì | Rilevanza normativa della violazione. |
| `conseguenza_violazione` | sì | Effetto modellistico della violazione. |
| `priorita` | no | Ordine di applicazione rispetto a vincoli concorrenti. |
| `evidenza_richiesta` | no | Informazioni necessarie per dimostrare conformità o violazione. |

## Invarianti

1. Un vincolo DEVE esprimere una sola regola normativa principale.
2. Un vincolo DEVE avere un ambito di applicazione esplicito.
3. Un vincolo DEVE essere valutabile mediante criteri osservabili o calcolabili.
4. Un vincolo NON DEVE eseguire azioni.
5. Un vincolo NON DEVE modificare direttamente lo stato del sistema.
6. Un vincolo NON DEVE incorporare implicitamente una transizione o una decisione.
7. La conseguenza della violazione DEVE essere dichiarata e deterministica.
8. Vincoli applicabili allo stesso ambito NON DEVONO produrre contraddizioni irrisolte.
9. Un vincolo attivo DEVE essere valutato nel momento pertinente prima che l'entità vincolata produca effetti irreversibili.
10. La severità NON DEVE alterare il significato del predicato, ma solo il trattamento della sua violazione.

## Relazioni

```yaml
ambito:
  stati: []
  trigger: []
  transizioni: []
  azioni: []
predicato: null
attivazione: []
conseguenza_violazione: null
evidenza_richiesta: []
```

Relazioni previste:

- `CONSTRAINT` può limitare una o più entità `STATE`;
- `CONSTRAINT` può determinare se un `TRIGGER` sia elaborabile;
- `CONSTRAINT` può impedire o condizionare una `TRANSITION`;
- `CONSTRAINT` può vietare, autorizzare condizionatamente o limitare una `ACTION`;
- `CONSTRAINT` può richiedere future entità `OBSERVATION` o `EVIDENCE` per la propria valutazione;
- `CONSTRAINT` può essere collegato a future entità `RISK` quando la violazione espone il sistema a un rischio identificato.

Le relazioni verso entità non ancora definite sono informative e non normative finché le relative schede non diventano stabili.

## Regole di validazione

Un'istanza di `CONSTRAINT` è valida se e solo se:

1. il nome è univoco nel modello;
2. il significato è formulato come regola e non come attività o stato;
3. l'ambito identifica entità o contesti esistenti;
4. il predicato produce un risultato verificabile;
5. il tipo è coerente con la formulazione normativa;
6. le condizioni di attivazione, se presenti, sono verificabili;
7. la severità appartiene a una tassonomia dichiarata;
8. la conseguenza della violazione è esplicita e applicabile;
9. eventuali conflitti con altri vincoli hanno una regola di risoluzione;
10. il vincolo può essere valutato prima del punto in cui la violazione diverrebbe irreversibile, salvo impossibilità esplicitamente documentata;
11. le evidenze richieste sono ottenibili o la loro indisponibilità è gestita esplicitamente;
12. il vincolo non duplica una precondizione locale senza una motivazione trasversale.

## Esempio valido

### `UNA_SOLA_DECISIONE_FINALE`

```yaml
nome: UNA_SOLA_DECISIONE_FINALE
significato: Per ogni richiesta può essere registrata al massimo una decisione finale valida.
ambito:
  stati:
    - IN_ATTESA_APPROVAZIONE
    - APPROVATA
    - RIFIUTATA
  trigger:
    - APPROVAZIONE_RICEVUTA
    - RIFIUTO_RICEVUTO
  transizioni:
    - APPROVA_RICHIESTA
    - RIFIUTA_RICHIESTA
predicato: conteggio_decisioni_finali_valide(richiesta_id) <= 1
tipo: limite
attivazione:
  - richiesta_id esiste
severita: bloccante
conseguenza_violazione: rifiuta il trigger e non eseguire alcuna transizione
evidenza_richiesta:
  - registro_decisioni
  - richiesta_id
```

Il vincolo è trasversale, verificabile e impedisce che trigger o transizioni concorrenti producano più decisioni finali per la stessa richiesta.

## Controesempio

### `GESTISCI_CORRETTAMENTE_LE_DECISIONI`

Non è un vincolo valido perché esprime un'intenzione generica senza ambito, predicato, severità o conseguenza verificabile. Deve essere sostituito da una o più regole specifiche e misurabili.

## Questioni aperte

1. Definire una tassonomia normativa minima dei tipi di vincolo: obbligo, divieto, limite, autorizzazione e coerenza.
2. Stabilire la tassonomia standard delle severità e le relative conseguenze predefinite.
3. Definire la risoluzione di conflitti tra vincoli di pari priorità.
4. Stabilire se precondizioni, guardie e invarianti siano specializzazioni di `CONSTRAINT` oppure costrutti distinti.
5. Definire il trattamento dei vincoli non valutabili per indisponibilità o incertezza dei dati.
