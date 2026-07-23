---
id: ACTION
nome: Azione
versione: 0.1.0
stato_specifica: draft
data_approvazione: null
dipendenze:
  - STATE
  - TRIGGER
  - TRANSITION
sostituisce: null
---

# Azione (`ACTION`)

## Definizione

Un'**azione** è un'operazione intenzionale, eseguibile e osservabile che produce o tenta di produrre un effetto sul sistema o sul suo ambiente.

L'azione descrive **ciò che viene fatto**. Non rappresenta uno stato persistente, non costituisce un trigger e non modifica autonomamente lo stato ontologico: ogni cambio di stato resta responsabilità esclusiva di una `TRANSITION` valida.

## Scopo

`ACTION` consente di:

- rappresentare gli effetti operativi autorizzati dal modello;
- separare l'esecuzione di un comportamento dal cambiamento di stato;
- dichiarare esecutore, input, output ed effetti attesi;
- rendere esplicite precondizioni, errori e politiche di ripetizione;
- collegare risultati operativi a trigger successivi senza confondere causa ed effetto.

## Confini

Un'azione:

- esprime una singola intenzione operativa principale;
- è eseguita da un attore o componente identificabile;
- può leggere o modificare dati e risorse;
- può produrre output, errori e trigger;
- può essere autorizzata da uno stato o associata a una transizione;
- può riuscire, fallire o terminare con esito indeterminato secondo una politica dichiarata.

Un'azione NON è:

- uno stato;
- un trigger;
- una transizione;
- un obiettivo;
- una decisione;
- una sequenza di attività indipendenti;
- un effetto implicito privo di esecutore e criteri di esito.

## Attributi

| Attributo | Obbligatorio | Significato |
|---|---:|---|
| `nome` | sì | Identificatore leggibile e univoco dell'azione. |
| `significato` | sì | Operazione intenzionale rappresentata. |
| `esecutore` | sì | Attore o componente responsabile dell'esecuzione. |
| `input` | no | Dati o risorse necessari all'esecuzione. |
| `precondizioni` | sì | Predicati che devono risultare veri prima dell'avvio. |
| `effetti_attesi` | sì | Modifiche o risultati che definiscono il successo. |
| `output` | no | Informazioni prodotte dall'esecuzione. |
| `stati_ammessi` | sì | Stati nei quali l'azione può essere avviata. |
| `trigger_prodotti` | no | Trigger emessi in base all'esito. |
| `errori` | no | Classi di errore previste e distinguibili. |
| `politica_ripetizione` | no | Regole per retry, idempotenza e duplicati. |
| `compensazione` | no | Azione o regola usata per mitigare effetti già prodotti. |

## Invarianti

1. Un'azione DEVE rappresentare una sola intenzione operativa principale.
2. Un'azione DEVE dichiarare un esecutore identificabile.
3. Un'azione DEVE avere criteri verificabili di successo o fallimento.
4. Un'azione NON DEVE modificare direttamente lo stato ontologico del sistema.
5. Un eventuale cambio di stato conseguente DEVE avvenire tramite una `TRANSITION` valida.
6. Un'azione NON DEVE incorporare implicitamente la decisione su quale transizione eseguire.
7. Gli effetti prodotti DEVONO essere coerenti con gli effetti attesi dichiarati.
8. Un'azione con effetti non naturalmente idempotenti DEVE dichiarare una politica per duplicati e ripetizioni.
9. Il fallimento DEVE produrre un esito distinguibile dal successo.
10. I trigger prodotti DEVONO rappresentare fatti avvenuti e non comandi da eseguire.

## Relazioni

```yaml
esecutore: null
stati_ammessi: []
transizioni_associate: []
input: []
output: []
trigger_prodotti: []
vincoli: []
compensazione: null
```

Relazioni previste:

- `ACTION` può essere ammessa o vietata da uno o più `STATE`;
- `ACTION` può essere autorizzata prima o dopo una `TRANSITION`;
- `ACTION` può produrre uno o più `TRIGGER` in base all'esito osservato;
- `ACTION` può essere limitata da future entità `CONSTRAINT`;
- `ACTION` può produrre future entità `OBSERVATION` o `EVIDENCE`;
- `ACTION` può avere una relazione di compensazione con un'altra `ACTION`.

Le relazioni verso entità non ancora definite sono informative e non normative finché le relative schede non diventano stabili.

## Regole di validazione

Un'istanza di `ACTION` è valida se e solo se:

1. il nome è univoco nel modello;
2. il significato è formulato come operazione e non come stato o fatto avvenuto;
3. l'esecutore è identificato;
4. le precondizioni sono verificabili prima dell'avvio;
5. gli stati nei quali l'azione è ammessa sono dichiarati;
6. successo, fallimento ed eventuale esito indeterminato sono distinguibili;
7. gli effetti attesi sono osservabili o verificabili;
8. eventuali trigger prodotti corrispondono a fatti risultanti dall'esecuzione;
9. la politica per retry e duplicati è deterministica quando l'azione può essere ripetuta;
10. un eventuale cambio di stato è modellato separatamente mediante `TRANSITION`;
11. eventuali effetti parziali e compensazioni sono dichiarati quando rilevanti;
12. l'azione non combina operazioni indipendenti che potrebbero avere esiti separati.

## Esempio valido

### `NOTIFICA_APPROVAZIONE`

```yaml
nome: NOTIFICA_APPROVAZIONE
significato: Invia al richiedente una notifica relativa all'approvazione registrata.
esecutore: SERVIZIO_NOTIFICHE
input:
  - richiesta_id
  - destinatario
  - decisione_id
precondizioni:
  - stato_corrente == APPROVATA
  - destinatario è disponibile
  - decisione_id è valida
effetti_attesi:
  - una notifica è accettata dal canale di consegna
output:
  - notifica_id
  - tempo_accettazione
stati_ammessi:
  - APPROVATA
trigger_prodotti:
  successo: NOTIFICA_ACCETTATA
  fallimento: NOTIFICA_FALLITA
errori:
  - DESTINATARIO_NON_VALIDO
  - CANALE_NON_DISPONIBILE
politica_ripetizione:
  idempotenza: richiesta_id + decisione_id + destinatario
  tentativi_massimi: 3
compensazione: null
```

L'azione tenta di produrre un effetto operativo verificabile. Il suo esito può generare trigger distinti, ma non modifica direttamente lo stato della richiesta.

## Controesempio

### `APPROVA_E_NOTIFICA_RICHIESTA`

Non è un'azione valida perché combina una decisione, un cambio di stato e una notifica. Deve essere scomposta almeno in un trigger o decisione registrata, una `TRANSITION` verso `APPROVATA` e una `ACTION` separata di notifica.

## Questioni aperte

1. Stabilire se le azioni debbano essere classificate normativamente come pure, interne o con effetti esterni.
2. Definire la semantica standard degli esiti `successo`, `fallimento` e `indeterminato`.
3. Stabilire se retry, idempotenza e compensazione appartengano all'azione o a future entità di policy e vincolo.
4. Definire il rapporto tra azioni sincrone, asincrone e di lunga durata.
5. Stabilire se un'azione composta sia esclusa dal nucleo oppure ammessa tramite un costrutto separato di orchestrazione.
