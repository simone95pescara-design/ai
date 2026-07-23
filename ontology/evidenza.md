---
id: EVIDENCE
nome: Evidenza
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - OBSERVATION
  - DECISION
  - CONSTRAINT
sostituisce: null
---

# Evidenza (`EVIDENCE`)

## Definizione

Un'**evidenza** è un elemento informativo tracciabile utilizzato per sostenere o confutare un'affermazione, una valutazione o una decisione.

`EVIDENCE` rappresenta il supporto epistemico disponibile. Non coincide necessariamente con un'osservazione, non garantisce verità assoluta e non produce autonomamente decisioni o cambiamenti di stato.

## Scopo

`EVIDENCE` consente di collegare affermazioni e decisioni a basi verificabili; distinguere dati, provenienza e forza del supporto; gestire evidenze convergenti o conflittuali; rendere auditabile la giustificazione del modello.

## Confini

Un'evidenza:

- ha una provenienza identificabile;
- supporta o confuta una proposizione esplicita;
- può derivare da osservazioni, documenti, test o registrazioni;
- possiede criteri dichiarati di rilevanza e affidabilità;
- può essere incompleta, contestata o superata.

Un'evidenza NON è una decisione, una conclusione automatica, un obiettivo, un vincolo, un trigger o un dato privo di relazione con una proposizione.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore univoco. |
| `proposizione` | sì | Affermazione supportata o confutata. |
| `direzione` | sì | `supporta` oppure `confuta`. |
| `fonte` | sì | Origine dell'elemento informativo. |
| `contenuto` | sì | Dato, documento o risultato rilevante. |
| `tempo_acquisizione` | sì | Momento in cui l'evidenza è stata acquisita. |
| `affidabilita` | sì | Valutazione motivata della fonte o del metodo. |
| `rilevanza` | sì | Relazione con la proposizione. |
| `integrita` | no | Garanzie di completezza e non alterazione. |
| `validita_temporale` | no | Intervallo nel quale resta applicabile. |
| `osservazioni_origine` | no | Osservazioni da cui deriva. |
| `vincoli` | no | Limiti di uso, accesso o conservazione. |

## Invarianti

1. Un'evidenza DEVE riferirsi a una proposizione esplicita.
2. Fonte, contenuto e tempo di acquisizione DEVONO essere tracciabili.
3. La direzione del supporto DEVE essere dichiarata.
4. Affidabilità e rilevanza NON DEVONO essere confuse.
5. Un'evidenza NON DEVE essere trattata come conclusiva per definizione.
6. Modifiche, revoche o sostituzioni DEVONO essere tracciate.
7. Evidenze conflittuali NON DEVONO essere eliminate implicitamente.
8. L'uso dell'evidenza DEVE rispettare i `CONSTRAINT` applicabili.
9. Un'evidenza NON DEVE modificare direttamente uno `STATE` né eseguire una `ACTION`.

## Relazioni

```yaml
proposizione: null
osservazioni_origine: []
decisioni_supportate: []
evidenze_conflittuali: []
vincoli: []
```

- `EVIDENCE` può derivare da una o più `OBSERVATION`;
- può supportare o confutare una `DECISION` o una sua motivazione;
- può essere limitata da `CONSTRAINT`;
- può contribuire alla futura valutazione di `RISK`.

## Regole di validazione

Un'istanza è valida se e solo se la proposizione è identificata; direzione, fonte e contenuto sono dichiarati; acquisizione, affidabilità e rilevanza sono tracciabili; eventuali trasformazioni sono documentate; conflitti e limiti d'uso sono rappresentati esplicitamente.

## Esempio valido

### `VERIFICA_DOCUMENTI_COMPLETI`

```yaml
nome: VERIFICA_DOCUMENTI_COMPLETI
proposizione: la richiesta contiene tutti i documenti obbligatori
direzione: supporta
fonte: CONTROLLO_DOCUMENTALE_2026_104
contenuto: esito positivo su 7 documenti richiesti
tempo_acquisizione: 2026-07-23T22:53:00Z
affidabilita: alta
rilevanza: diretta
integrita:
  impronta_verificata: true
osservazioni_origine:
  - OSSERVAZIONE_DOCUMENTI_PRESENTI
```

## Controesempio

### `SECONDO_ME_LA_RICHIESTA_VA_BENE`

Non è un'evidenza valida perché non identifica una proposizione verificabile, una fonte tracciabile né criteri di affidabilità e rilevanza.

## Questioni aperte

1. Definire scale normative di affidabilità e forza probatoria.
2. Stabilire la rappresentazione di catene di custodia e trasformazioni.
3. Definire regole comuni per evidenze scadute o revocate.
4. Stabilire come aggregare evidenze dipendenti senza sovrastimarne il peso.
