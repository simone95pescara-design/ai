---
id: DECISION
nome: Decisione
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - OBSERVATION
  - OBJECTIVE
  - CONSTRAINT
  - ACTION
  - TRIGGER
sostituisce: null
---

# Decisione (`DECISION`)

## Definizione

Una **decisione** è la selezione esplicita e tracciabile di una tra più alternative ammissibili da parte di un decisore identificabile.

`DECISION` rappresenta la scelta effettuata. Non coincide con l'esecuzione di un'azione, non è un trigger e non modifica direttamente lo stato.

## Scopo

`DECISION` consente di rendere espliciti decisore, alternative, criteri e motivazione; collegare osservazioni, obiettivi e vincoli a una scelta; distinguere scelta, esecuzione ed effetto; rendere verificabile il processo decisionale.

## Confini

Una decisione:

- considera almeno due alternative distinguibili, salvo decisione obbligata dichiarata;
- identifica il decisore;
- dichiara gli input rilevanti;
- seleziona una sola alternativa o un insieme ammesso;
- può produrre un fatto osservabile utilizzabile come trigger.

Una decisione NON è un'azione, una transizione, un obiettivo, un vincolo, un'osservazione o una valutazione priva di scelta.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore univoco. |
| `decisore` | sì | Soggetto o componente responsabile. |
| `alternative` | sì | Opzioni considerate. |
| `alternativa_selezionata` | sì | Esito della scelta. |
| `criteri` | sì | Regole utilizzate per confrontare le alternative. |
| `input` | sì | Osservazioni, dati o evidenze considerate. |
| `obiettivi` | no | Obiettivi rilevanti. |
| `vincoli` | sì | Vincoli applicabili. |
| `motivazione` | sì | Giustificazione tracciabile della scelta. |
| `tempo_decisione` | sì | Istante della decisione. |
| `trigger_prodotti` | no | Fatti emessi in seguito alla registrazione. |

## Invarianti

1. Una decisione DEVE avere un decisore identificabile.
2. Le alternative considerate DEVONO essere dichiarate.
3. L'alternativa selezionata DEVE appartenere all'insieme delle alternative ammissibili.
4. Una decisione DEVE rispettare tutti i `CONSTRAINT` applicabili.
5. Una decisione NON DEVE eseguire direttamente una `ACTION`.
6. Una decisione NON DEVE modificare direttamente uno `STATE`.
7. Gli input determinanti DEVONO essere tracciabili.
8. La motivazione DEVE essere coerente con criteri, input e obiettivi dichiarati.
9. Un eventuale trigger prodotto DEVE rappresentare il fatto che la decisione è stata registrata, non un comando implicito.

## Relazioni

```yaml
decisore: null
osservazioni: []
evidenze: []
obiettivi: []
vincoli: []
azioni_autorizzabili: []
trigger_prodotti: []
```

- `DECISION` può utilizzare `OBSERVATION`;
- può valutare alternative rispetto a `OBJECTIVE` e `CONSTRAINT`;
- può autorizzare, raccomandare o vietare future `ACTION` senza eseguirle;
- può produrre `TRIGGER` relativi alla decisione registrata;
- può essere supportata da future `EVIDENCE` e considerare futuri `RISK`.

## Regole di validazione

Un'istanza è valida se e solo se il decisore è identificato; le alternative sono distinguibili; la scelta è ammissibile; criteri, input e motivazione sono tracciabili; i vincoli sono rispettati; tempo ed esito sono registrati; scelta, esecuzione e cambio di stato restano separati.

## Esempio valido

### `DECIDI_APPROVAZIONE_RICHIESTA`

```yaml
nome: DECIDI_APPROVAZIONE_RICHIESTA
decisore: RESPONSABILE_AREA
alternative:
  - APPROVARE
  - RIFIUTARE
  - RICHIEDERE_INTEGRAZIONE
alternativa_selezionata: APPROVARE
criteri:
  - completezza_documentale
  - conformita_requisiti
input:
  - OSSERVAZIONE_DOCUMENTI_COMPLETI
obiettivi:
  - RIDURRE_TEMPO_RISPOSTA
vincoli:
  - separazione_dei_ruoli
motivazione: requisiti soddisfatti e documentazione completa
tempo_decisione: 2026-07-23T22:55:00Z
trigger_prodotti:
  - RICHIESTA_APPROVATA
```

## Controesempio

### `APPROVA_E_INVIA_EMAIL`

Non è una decisione valida perché combina scelta, cambio di stato ed esecuzione operativa.

## Questioni aperte

1. Definire la semantica delle decisioni collettive.
2. Stabilire se raccomandazione e autorizzazione siano sottotipi distinti.
3. Definire requisiti minimi di spiegabilità per decisori automatici.
4. Stabilire la gestione delle decisioni revocate o superate.
