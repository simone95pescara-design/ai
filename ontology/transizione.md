---
id: TRANSITION
nome: Transizione
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - STATE
  - TRIGGER
sostituisce: null
---

# Transizione (`TRANSITION`)

## Definizione

Una **transizione** è la regola deterministica che, a partire da uno stato sorgente e da un trigger valido, valuta guardie e vincoli e, quando tutte le condizioni sono soddisfatte, modifica lo stato del sistema verso uno stato destinazione.

La transizione è l'unico costrutto autorizzato a cambiare lo stato. Il trigger ne avvia la valutazione, ma non ne garantisce l'esecuzione.

## Scopo

`TRANSITION` consente di:

- formalizzare i cambiamenti ammessi tra stati;
- separare il verificarsi di un fatto dalla valutazione dei suoi effetti;
- rendere esplicite guardie, vincoli e destinazione;
- garantire che ogni cambio di stato sia tracciabile e verificabile;
- gestire in modo deterministico transizioni concorrenti o alternative.

## Confini

Una transizione:

- collega esattamente uno stato sorgente a uno stato destinazione;
- è resa valutabile da almeno un trigger;
- può contenere guardie e riferimenti a vincoli;
- può produrre un esito osservabile;
- può autorizzare azioni associate senza coincidere con esse.

Una transizione NON è:

- un trigger;
- un'azione;
- uno stato;
- una decisione non formalizzata;
- una sequenza procedurale;
- un cambiamento implicito privo di sorgente, destinazione e causa.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore leggibile e univoco della transizione. |
| `stato_sorgente` | sì | Stato nel quale la transizione può essere valutata. |
| `stato_destinazione` | sì | Stato assunto dopo l'esecuzione riuscita. |
| `trigger` | sì | Trigger che rende valutabile la transizione. |
| `guardie` | no | Predicati che devono risultare veri al momento della valutazione. |
| `vincoli` | no | Regole ulteriori che limitano l'esecuzione. |
| `priorita` | no | Ordine deterministico tra transizioni concorrenti. |
| `azioni_associate` | no | Azioni autorizzate prima, durante o dopo il cambio di stato. |
| `esito` | no | Informazione osservabile prodotta dalla valutazione o esecuzione. |

## Invarianti

1. Una transizione DEVE dichiarare uno e un solo stato sorgente.
2. Una transizione DEVE dichiarare uno e un solo stato destinazione.
3. Lo stato sorgente DEVE coincidere con lo stato corrente al momento della valutazione.
4. Il trigger ricevuto DEVE corrispondere a uno dei trigger dichiarati dalla transizione.
5. Tutte le guardie e i vincoli applicabili DEVONO risultare soddisfatti prima del cambio di stato.
6. Una transizione NON DEVE modificare lo stato se la valutazione fallisce.
7. Il cambio di stato DEVE essere atomico rispetto al modello.
8. L'esecuzione DEVE produrre un risultato deterministico a parità di stato, trigger, dati e vincoli.
9. Due transizioni concorrenti NON DEVONO produrre ambiguità non risolta.
10. Le azioni associate NON DEVONO sostituire la semantica della transizione.

## Relazioni

```yaml
stato_sorgente: null
stato_destinazione: null
trigger: null
guardie: []
vincoli: []
azioni_associate: []
esito: null
```

Relazioni previste:

- `TRANSITION` collega due entità `STATE`;
- `TRANSITION` è resa valutabile da una entità `TRIGGER`;
- `TRANSITION` può essere limitata da future entità `CONSTRAINT`;
- `TRANSITION` può autorizzare future entità `ACTION`;
- `TRANSITION` può produrre una futura entità `OBSERVATION` o `EVIDENCE`.

Le relazioni verso entità non ancora definite sono informative e non normative finché le relative schede non diventano stabili.

## Regole di validazione

Un'istanza di `TRANSITION` è valida se e solo se:

1. il nome è univoco nel modello;
2. sorgente e destinazione sono stati esistenti e distinti, salvo transizioni interne esplicitamente ammesse;
3. il trigger è definito e ammesso nello stato sorgente;
4. ogni guardia è espressa come predicato verificabile;
5. ogni vincolo richiamato è applicabile alla transizione;
6. l'esito della valutazione è deterministico;
7. in caso di più transizioni abilitate, esiste una regola esplicita di esclusione, priorità o risoluzione;
8. il fallimento non produce modifiche parziali allo stato;
9. ogni azione associata dichiara il proprio momento di esecuzione e la politica in caso di errore;
10. il passaggio risultante è coerente con `esce_verso` dello stato sorgente e `entra_da` dello stato destinazione.

## Esempio valido

### `APPROVA_RICHIESTA`

```yaml
nome: APPROVA_RICHIESTA
stato_sorgente: IN_ATTESA_APPROVAZIONE
stato_destinazione: APPROVATA
trigger: APPROVAZIONE_RICEVUTA
guardie:
  - payload.richiesta_id == richiesta_corrente.id
  - payload.decisione_id non è già stata elaborata
vincoli:
  - la richiesta non è annullata
priorita: 100
azioni_associate:
  - momento: dopo_transizione
    azione: NOTIFICA_APPROVAZIONE
esito: RICHIESTA_APPROVATA
```

La transizione cambia lo stato solo quando sorgente, trigger, guardie e vincoli risultano validi. La notifica è un'azione associata e non costituisce il cambio di stato.

## Controesempio

### `SE_APPROVATA_ESEGUI_E_NOTIFICA`

Non è una transizione valida perché combina una condizione vaga, più azioni e una sequenza procedurale senza dichiarare stato sorgente, stato destinazione, trigger e guardie verificabili.

## Questioni aperte

1. Stabilire se le transizioni interne, che non cambiano lo stato, appartengano al nucleo o debbano essere modellate come costrutto separato.
2. Definire la semantica normativa delle azioni eseguite prima e dopo il cambio di stato, inclusi rollback e compensazione.
3. Stabilire il modello di concorrenza e la regola predefinita per più transizioni contemporaneamente abilitate.
4. Definire se la priorità sia attributo della transizione o una politica esterna di risoluzione.