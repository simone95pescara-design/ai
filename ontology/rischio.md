---
id: RISK
nome: Rischio
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - OBJECTIVE
  - CONSTRAINT
  - OBSERVATION
  - EVIDENCE
  - DECISION
sostituisce: null
---

# Rischio (`RISK`)

## Definizione

Un **rischio** è la rappresentazione strutturata della possibilità che un evento o una condizione produca conseguenze indesiderate rispetto a uno o più obiettivi, vincoli o interessi protetti.

`RISK` descrive una possibilità valutata, non un fatto già avvenuto. Non costituisce un trigger, non seleziona autonomamente azioni e non modifica direttamente lo stato.

## Scopo

`RISK` consente di dichiarare minacce e conseguenze; valutare probabilità, impatto e incertezza; collegare osservazioni ed evidenze alle decisioni; distinguere rischio, incidente e vincolo; rendere esplicite strategie di trattamento e accettazione.

## Confini

Un rischio:

- identifica una causa o condizione di rischio;
- descrive uno scenario potenziale;
- dichiara conseguenze e soggetti o obiettivi esposti;
- può essere valutato qualitativamente o quantitativamente;
- può essere accettato, mitigato, trasferito o evitato mediante decisioni separate.

Un rischio NON è un evento già avvenuto, un danno osservato, una decisione, un'azione, un vincolo o una certezza.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore univoco. |
| `scenario` | sì | Evento o condizione potenziale. |
| `cause` | sì | Fattori che possono generare lo scenario. |
| `conseguenze` | sì | Effetti indesiderati attesi. |
| `elementi_esposti` | sì | Obiettivi, risorse o soggetti coinvolti. |
| `probabilita` | sì | Stima della possibilità di accadimento. |
| `impatto` | sì | Gravità delle conseguenze. |
| `incertezza` | sì | Limiti conoscitivi della valutazione. |
| `orizzonte_temporale` | no | Periodo di validità della valutazione. |
| `osservazioni` | no | Osservazioni rilevanti. |
| `evidenze` | no | Evidenze che supportano la valutazione. |
| `trattamenti_possibili` | no | Strategie considerate, non automaticamente eseguite. |
| `vincoli` | no | Limiti applicabili al trattamento o all'accettazione. |

## Invarianti

1. Un rischio DEVE descrivere uno scenario potenziale e non un fatto già accaduto.
2. Cause, conseguenze ed elementi esposti DEVONO essere identificati.
3. Probabilità e impatto DEVONO essere valutati separatamente.
4. L'incertezza della valutazione DEVE essere esplicitata.
5. Un rischio NON DEVE selezionare o eseguire direttamente una `ACTION`.
6. L'accettazione o il trattamento DEVONO risultare da una `DECISION` separata.
7. Le valutazioni DEVONO essere aggiornabili senza cancellare la storia precedente.
8. Osservazioni ed evidenze determinanti DEVONO essere tracciabili.
9. Un rischio NON DEVE modificare direttamente uno `STATE`.
10. Qualsiasi trattamento DEVE rispettare i `CONSTRAINT` applicabili.

## Relazioni

```yaml
obiettivi_esposti: []
vincoli_rilevanti: []
osservazioni: []
evidenze: []
decisioni_di_trattamento: []
azioni_di_mitigazione: []
```

- `RISK` può ostacolare uno o più `OBJECTIVE`;
- può derivare da `OBSERVATION` ed essere supportato da `EVIDENCE`;
- può essere considerato da una `DECISION`;
- può essere limitato o governato da `CONSTRAINT`;
- eventuali azioni di mitigazione restano entità `ACTION` separate.

## Regole di validazione

Un'istanza è valida se e solo se scenario, cause, conseguenze ed elementi esposti sono espliciti; probabilità, impatto e incertezza usano scale dichiarate; osservazioni ed evidenze sono tracciabili; l'orizzonte temporale è definito quando necessario; trattamento e accettazione non sono incorporati implicitamente nella definizione.

## Esempio valido

### `RITARDO_RISPOSTA_CLIENTE`

```yaml
nome: RITARDO_RISPOSTA_CLIENTE
scenario: una richiesta normale resta senza risposta oltre 48 ore
cause:
  - sovraccarico_operativo
  - assegnazione_mancante
conseguenze:
  - mancato_raggiungimento_obiettivo_tempo_risposta
  - riduzione_soddisfazione_cliente
elementi_esposti:
  - RIDURRE_TEMPO_RISPOSTA
probabilita: media
impatto: alto
incertezza: media
orizzonte_temporale: prossimi 30 giorni
osservazioni:
  - CODA_RICHIESTE_CORRENTE
evidenze:
  - TREND_RITARDI_ULTIMI_90_GIORNI
trattamenti_possibili:
  - riallocazione_carico
  - escalation_automatica
```

## Controesempio

### `RIALLOCA_SUBITO_TUTTE_LE_RICHIESTE`

Non è un rischio valido perché prescrive un'azione. Lo scenario e le conseguenze devono essere modellati separatamente dalla decisione e dal trattamento.

## Questioni aperte

1. Definire scale normative comuni per probabilità, impatto e incertezza.
2. Stabilire la relazione tra rischio inerente, residuo e accettato.
3. Definire come modellare dipendenze e aggregazioni tra rischi.
4. Stabilire quando una variazione della valutazione debba produrre un trigger.
