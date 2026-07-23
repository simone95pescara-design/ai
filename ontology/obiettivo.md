---
id: OBJECTIVE
nome: Obiettivo
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - STATE
  - ACTION
  - CONSTRAINT
sostituisce: null
---

# Obiettivo (`OBJECTIVE`)

## Definizione

Un **obiettivo** è un risultato desiderato espresso come condizione verificabile del sistema o del suo ambiente.

`OBJECTIVE` descrive **che cosa deve risultare vero**, non il percorso da seguire. Non seleziona azioni, non determina transizioni e non modifica direttamente lo stato.

## Scopo

`OBJECTIVE` consente di:

- dichiarare risultati desiderati separandoli dai mezzi operativi;
- valutare progresso, raggiungimento e mancato raggiungimento;
- confrontare alternative rispetto a criteri espliciti;
- collegare stati e risultati osservabili a finalità dichiarate;
- impedire che procedure o azioni siano scambiate per risultati.

## Confini

Un obiettivo:

- esprime una condizione desiderata;
- possiede criteri verificabili di raggiungimento;
- può avere una priorità e un orizzonte temporale;
- può essere limitato da vincoli;
- può dipendere da altri obiettivi;
- può risultare raggiunto, non raggiunto, parzialmente raggiunto o non valutabile secondo regole dichiarate.

Un obiettivo NON è:

- uno stato corrente;
- un'azione;
- una transizione;
- un trigger;
- una decisione;
- una procedura;
- un'intenzione priva di criteri di verifica.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore leggibile e univoco. |
| `condizione_desiderata` | sì | Predicato che descrive il risultato atteso. |
| `criteri_raggiungimento` | sì | Regole verificabili per dichiarare l'obiettivo raggiunto. |
| `ambito` | sì | Sistema, entità o contesto cui l'obiettivo si applica. |
| `orizzonte_temporale` | no | Termine o intervallo entro cui valutare il risultato. |
| `priorita` | no | Ordine relativo rispetto ad altri obiettivi. |
| `metriche` | no | Misure utilizzate per valutare progresso o risultato. |
| `vincoli` | no | Vincoli applicabili al perseguimento o alla valutazione. |
| `dipendenze` | no | Altri obiettivi necessari o correlati. |
| `stati_rilevanti` | no | Stati che contribuiscono alla valutazione. |

## Invarianti

1. Un obiettivo DEVE essere espresso come condizione desiderata e non come comando operativo.
2. Un obiettivo DEVE avere criteri verificabili di raggiungimento.
3. Un obiettivo NON DEVE prescrivere direttamente una specifica `ACTION`.
4. Un obiettivo NON DEVE modificare direttamente uno `STATE`.
5. Il raggiungimento DEVE essere valutato mediante dati o condizioni osservabili.
6. Gli eventuali conflitti tra obiettivi DEVONO essere risolti mediante priorità o regole esplicite.
7. Un obiettivo soggetto a termine temporale DEVE dichiarare il riferimento temporale usato.
8. Un obiettivo NON DEVE essere dichiarato raggiunto quando i criteri richiesti risultano solo parzialmente soddisfatti, salvo regola esplicita.
9. Il perseguimento di un obiettivo DEVE rispettare tutti i `CONSTRAINT` applicabili.

## Relazioni

```yaml
stati_rilevanti: []
azioni_possibili: []
vincoli: []
dipendenze: []
metriche: []
```

Relazioni previste:

- `OBJECTIVE` può essere valutato rispetto a uno o più `STATE`;
- `ACTION` può contribuire al raggiungimento di un `OBJECTIVE`, senza esserne parte costitutiva;
- `CONSTRAINT` può limitare i modi ammissibili di perseguire o valutare un `OBJECTIVE`;
- future `OBSERVATION` ed `EVIDENCE` possono supportarne la valutazione;
- future `DECISION` possono scegliere alternative in funzione di uno o più obiettivi;
- futuri `RISK` possono ostacolarne il raggiungimento.

Le relazioni verso entità non ancora definite sono informative e non normative finché le relative schede non diventano stabili.

## Regole di validazione

Un'istanza di `OBJECTIVE` è valida se e solo se:

1. il nome è univoco nel modello;
2. la condizione desiderata è formulata come risultato e non come attività;
3. l'ambito è identificato;
4. i criteri di raggiungimento sono verificabili;
5. eventuali metriche hanno unità, soglie e modalità di rilevazione definite;
6. eventuali termini temporali sono non ambigui;
7. eventuali dipendenze da altri obiettivi sono prive di cicli non risolti;
8. i conflitti con altri obiettivi sono governati da regole esplicite;
9. il perseguimento non richiede la violazione di vincoli applicabili.

## Esempio valido

### `RIDURRE_TEMPO_RISPOSTA`

```yaml
nome: RIDURRE_TEMPO_RISPOSTA
condizione_desiderata: il tempo mediano di risposta è inferiore a 2 ore
ambito: richieste di assistenza con priorità normale
criteri_raggiungimento:
  - mediana_30_giorni < 2 ore
orizzonte_temporale: entro il 31 dicembre 2026
metriche:
  - mediana_30_giorni
vincoli:
  - nessuna richiesta ad alta priorità può essere ritardata
```

L'obiettivo dichiara un risultato misurabile senza imporre quale azione debba essere eseguita.

## Controesempio

### `INVIA_SUBITO_UNA_EMAIL`

Non è un obiettivo valido perché prescrive un'azione specifica. Il risultato desiderato deve essere espresso separatamente, per esempio come condizione di avvenuta informazione del destinatario.

## Questioni aperte

1. Definire una tassonomia normativa tra obiettivi terminali, intermedi e strumentali.
2. Stabilire la semantica standard del raggiungimento parziale.
3. Definire se priorità e utilità appartengano all'obiettivo o a una futura entità di policy.
4. Stabilire come modellare obiettivi incompatibili o dinamicamente modificati.
