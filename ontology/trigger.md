---
id: TRIGGER
nome: Trigger
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - STATE
sostituisce: null
---

# Trigger (`TRIGGER`)

## Definizione

Un **trigger** è la rappresentazione di un fatto rilevante, osservabile e temporalmente identificabile che rende valutabile una o più transizioni del sistema.

Il trigger segnala che qualcosa è accaduto o che una condizione formalmente modellata si è verificata. Non esegue azioni, non modifica direttamente lo stato e non garantisce che una transizione avvenga.

## Scopo

`TRIGGER` consente di:

- identificare ciò che avvia la valutazione di una transizione;
- separare il verificarsi di un fatto dalla decisione sugli effetti conseguenti;
- stabilire quali eventi siano rilevanti in ciascuno stato;
- rendere tracciabile la causa immediata di un possibile cambiamento di stato;
- distinguere eventi esterni, interni e temporali.

## Confini

Un trigger:

- rappresenta un fatto già avvenuto o una condizione divenuta vera;
- è associato a un istante o a un intervallo temporalmente determinabile;
- può trasportare dati contestuali;
- può essere accettato, ignorato o rifiutato in funzione dello stato e dei vincoli;
- può rendere valutabili più transizioni alternative.

Un trigger NON è:

- un'azione;
- una transizione;
- uno stato;
- una decisione;
- un obiettivo;
- una condizione permanente priva di un momento di attivazione identificabile;
- una garanzia che il sistema cambi stato.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore leggibile e univoco del trigger. |
| `significato` | sì | Fatto rappresentato dal trigger. |
| `origine` | sì | Soggetto o meccanismo che genera il trigger. |
| `tempo_occorrenza` | sì | Istante o intervallo in cui il fatto si è verificato. |
| `payload` | no | Dati contestuali associati all'occorrenza. |
| `stati_ammessi` | sì | Stati nei quali il trigger può essere elaborato. |
| `precondizioni` | no | Condizioni necessarie affinché l'occorrenza sia considerata valida. |
| `chiave_idempotenza` | no | Identificatore usato per riconoscere occorrenze duplicate. |
| `scadenza` | no | Limite temporale oltre il quale il trigger non può più essere elaborato. |

## Invarianti

1. Un trigger DEVE rappresentare un fatto semanticamente definito e verificabile.
2. Ogni occorrenza di trigger DEVE essere temporalmente identificabile.
3. Un trigger NON DEVE modificare direttamente lo stato del sistema.
4. Un trigger NON DEVE eseguire autonomamente azioni.
5. Un trigger NON DEVE incorporare la decisione su quale transizione applicare.
6. La ricezione di un trigger NON DEVE implicare automaticamente una transizione.
7. Un trigger DEVE poter essere distinto da altre tipologie di trigger tramite nome e significato.
8. I dati contenuti nel payload NON DEVONO alterare il significato ontologico del trigger.
9. Un'occorrenza duplicata DEVE essere gestita in modo deterministico quando l'idempotenza è richiesta dal modello.

## Relazioni

```yaml
origine: null
stati_ammessi: []
transizioni_valutabili: []
precondizioni: []
payload: {}
```

Relazioni previste:

- `TRIGGER` può essere ammesso o rifiutato da uno o più `STATE`;
- `TRIGGER` rende valutabili una o più future entità `TRANSITION`;
- `TRIGGER` può essere prodotto dall'esito di una futura entità `ACTION`;
- `TRIGGER` può essere rilevato attraverso una futura entità `OBSERVATION`;
- `TRIGGER` può essere soggetto a future entità `CONSTRAINT`.

Le relazioni verso entità non ancora definite sono informative e non normative finché le relative schede non diventano stabili.

## Regole di validazione

Un'istanza di `TRIGGER` è valida se e solo se:

1. il nome è univoco nel modello;
2. il significato descrive un fatto e non un'attività o uno stato persistente;
3. l'origine è identificabile;
4. il tempo di occorrenza è disponibile o determinabile;
5. gli stati nei quali può essere elaborato sono dichiarati;
6. le eventuali precondizioni sono verificabili;
7. il payload contiene esclusivamente dati contestuali coerenti con il significato del trigger;
8. il trigger non contiene istruzioni operative;
9. ogni transizione associata valuta autonomamente condizioni e vincoli prima dell'esecuzione;
10. la politica per duplicati, ritardi e scadenza è deterministica quando tali casi sono possibili.

## Esempio valido

### `APPROVAZIONE_RICEVUTA`

```yaml
nome: APPROVAZIONE_RICEVUTA
significato: È stata registrata una decisione valida di approvazione per una richiesta identificata.
origine: SERVIZIO_APPROVAZIONI
tempo_occorrenza: 2026-07-23T20:00:00+02:00
payload:
  richiesta_id: R-1042
  decisore_id: U-17
  decisione_id: D-882
stati_ammessi:
  - IN_ATTESA_APPROVAZIONE
precondizioni:
  - richiesta_id esiste
  - decisione_id è autentica
chiave_idempotenza: D-882
scadenza: null
```

Il trigger descrive un fatto già avvenuto. La sua elaborazione può rendere valutabile una transizione verso uno stato approvato, ma non produce autonomamente tale cambiamento.

## Controesempio

### `APPROVA_LA_RICHIESTA`

Non è un trigger valido perché esprime un comando operativo. Deve essere modellato come `ACTION`; l'eventuale completamento dell'azione può produrre un trigger distinto, per esempio `APPROVAZIONE_REGISTRATA`.

## Questioni aperte

1. Stabilire se i trigger basati su condizioni debbano essere modellati come rilevazioni puntuali prodotte da `OBSERVATION` oppure come sottotipo autonomo.
2. Definire una tassonomia normativa minima tra trigger esterni, interni e temporali.
3. Stabilire se idempotenza e scadenza debbano essere attributi del trigger o vincoli applicati alla sua elaborazione.
4. Definire il trattamento formale di trigger fuori ordine e trigger ricevuti in ritardo.