---
id: OBSERVATION
nome: Osservazione
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - STATE
  - TRIGGER
  - CONSTRAINT
sostituisce: null
---

# Osservazione (`OBSERVATION`)

## Definizione

Un'**osservazione** è una registrazione temporaneamente identificabile di un fatto, valore o fenomeno rilevato da una sorgente dichiarata.

`OBSERVATION` rappresenta ciò che è stato rilevato. Non interpreta autonomamente il significato del dato, non costituisce una decisione e non modifica direttamente lo stato.

## Scopo

`OBSERVATION` consente di separare il dato rilevato dalla sua interpretazione, dichiarare provenienza e tempo di rilevazione, valutare qualità e affidabilità e fornire input verificabili a trigger, decisioni e valutazioni.

## Confini

Un'osservazione:

- riguarda un oggetto o fenomeno identificabile;
- è prodotta da una sorgente identificabile;
- registra valore, unità e tempo quando applicabili;
- può essere incompleta, incerta o contraddetta;
- può contribuire alla generazione di un trigger.

Un'osservazione NON è uno stato, un trigger, una decisione, un'azione, un'inferenza o una prova sufficiente per definizione.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore univoco. |
| `oggetto` | sì | Entità o fenomeno osservato. |
| `valore` | sì | Contenuto rilevato. |
| `sorgente` | sì | Origine della rilevazione. |
| `tempo_rilevazione` | sì | Istante o intervallo del rilevamento. |
| `unita` | no | Unità di misura applicabile. |
| `metodo` | no | Procedura o strumento di rilevazione. |
| `qualita` | no | Indicatori di completezza, precisione o affidabilità. |
| `contesto` | no | Condizioni rilevanti della rilevazione. |
| `vincoli` | no | Vincoli applicabili alla raccolta o all'uso. |

## Invarianti

1. Un'osservazione DEVE dichiarare una sorgente e un riferimento temporale.
2. Il valore registrato DEVE essere distinguibile dalla sua interpretazione.
3. Un'osservazione NON DEVE modificare direttamente uno `STATE`.
4. Un'osservazione NON DEVE essere trattata automaticamente come `TRIGGER`.
5. Incertezza, assenza o errore noti DEVONO essere rappresentati esplicitamente.
6. Le unità di misura DEVONO essere dichiarate quando il valore è quantitativo.
7. La provenienza NON DEVE essere alterata retroattivamente senza tracciamento.
8. L'uso dell'osservazione DEVE rispettare i `CONSTRAINT` applicabili.

## Relazioni

```yaml
sorgente: null
oggetto: null
trigger_derivati: []
vincoli: []
evidenze: []
```

- `OBSERVATION` può descrivere proprietà rilevanti di uno `STATE`;
- può contribuire alla produzione di un `TRIGGER` mediante una regola separata;
- può essere soggetta a `CONSTRAINT`;
- può supportare future `DECISION` ed essere corroborata da future `EVIDENCE`.

## Regole di validazione

Un'istanza è valida se e solo se nome, oggetto, sorgente e tempo sono identificati; il valore è rappresentato senza confonderlo con un giudizio; unità e qualità sono dichiarate quando rilevanti; eventuali trasformazioni sono tracciabili; l'uso previsto rispetta i vincoli applicabili.

## Esempio valido

### `TEMPERATURA_MAGAZZINO_01`

```yaml
nome: TEMPERATURA_MAGAZZINO_01
oggetto: MAGAZZINO_01
valore: 8.4
unita: °C
sorgente: SENSORE_T17
tempo_rilevazione: 2026-07-23T22:50:00Z
metodo: termometro digitale
qualita:
  calibrazione_valida: true
```

## Controesempio

### `MAGAZZINO_PERICOLOSO`

Non è un'osservazione valida perché incorpora un'interpretazione normativa senza dichiarare il valore rilevato, la sorgente e la regola che giustifica il giudizio.

## Questioni aperte

1. Definire una tassonomia comune degli indicatori di qualità.
2. Stabilire la semantica delle osservazioni aggregate e derivate.
3. Definire la gestione normativa di osservazioni contraddittorie.
4. Stabilire requisiti minimi di immutabilità e tracciabilità.
