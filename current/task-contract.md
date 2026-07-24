# Contratto dell'attività corrente

Questo file definisce esclusivamente autorità, input e obblighi dell'esecutore durante l'esperimento corrente.

## Scopo

Applicare l'ipotesi contenuta in [`transformation-contract.md`](transformation-contract.md) al caso di verifica attivo senza estendere l'ambito dell'esperimento.

## Input vincolanti

- [`state.md`](state.md), per fatti, decisioni e stato dell'esperimento;
- [`transformation-contract.md`](transformation-contract.md), per la trasformazione candidata;
- [`../tests/first-behavior-case.md`](../tests/first-behavior-case.md), per input e criteri di verifica;
- la richiesta effettiva dell'utente.

## Autorità

L'esecutore può:

- leggere e confrontare gli input vincolanti;
- applicare la trasformazione candidata;
- dichiarare fatti, assunzioni e questioni irrisolte;
- registrare l'esito del test;
- proporre di mantenere, modificare o rifiutare l'ipotesi.

L'esecutore non può:

- modificare file fuori dall'ambito esplicitamente autorizzato;
- introdurre architetture, categorie, componenti o regole permanenti;
- promuovere una proposta o un'ipotesi a decisione approvata;
- alterare i criteri del test durante la sua esecuzione.

## Output richiesto

L'esecuzione deve produrre:

- l'output previsto dal caso di verifica;
- l'elenco dei criteri soddisfatti e violati;
- le assunzioni non dichiarate rilevate in revisione;
- una proposta motivata: `mantenere`, `modificare` oppure `rifiutare`.

## Completamento

L'attività è completata solo quando l'esito è registrato. Questo contratto non stabilisce da solo se l'ipotesi di trasformazione sia valida.