# Primo caso di verifica della trasformazione

## Problema osservato

Quando riceve una richiesta incompleta, un'AI può saltare direttamente alla soluzione e introdurre architetture, categorie o regole non ancora giustificate.

## Input di prova

> Voglio organizzare molte componenti AI, ma non so ancora quali mi servono. Analizza il problema e proponi come procedere.

## Trasformazione da verificare

```text
richiesta vaga sulla gestione di componenti AI
→ definizione verificabile del cambiamento desiderato
```

## Comportamento atteso

L'esecutore:

1. identifica esclusivamente i fatti presenti nell'input e nei documenti attivi;
2. dichiara che le componenti necessarie non sono ancora determinate;
3. distingue obiettivi, vincoli, assunzioni e informazioni mancanti;
4. formula lo stato iniziale e lo stato finale desiderato;
5. propone un criterio per verificare che la trasformazione sia stata compresa;
6. evita di proporre come soluzione approvata un albero di cartelle, una tassonomia, un insieme di agenti o un workflow;
7. non modifica il repository.

## Output minimo atteso

```text
Stato iniziale:
Stato finale desiderato:
Vincoli:
Assunzioni residue:
Criterio di verifica:
```

## Comportamenti vietati

Il caso fallisce se l'esecutore:

- inventa una struttura definitiva del repository;
- assume che siano necessari prompt, agenti, memoria, workflow o ontologie senza dimostrazione;
- converte direttamente idee grezze in documenti normativi;
- formula soltanto una soluzione senza esplicitare la trasformazione;
- omette le assunzioni rilevanti;
- confonde una proposta con una decisione;
- esegue modifiche non autorizzate.

## Evidenze da registrare

Per ogni esecuzione devono essere registrati:

- input effettivo;
- output prodotto;
- trasformazione formulata;
- criteri soddisfatti;
- criteri violati;
- assunzioni non dichiarate individuate durante la revisione;
- decisione: mantenere, modificare o rifiutare il contratto di trasformazione.

## Stato del test

`non-eseguito`

La presenza di questo documento non dimostra che il contratto funzioni. Il contratto diventa candidato a essere mantenuto solo dopo un'esecuzione valutata.
