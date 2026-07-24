# Contratto di trasformazione

## Stato epistemico

`ipotesi-in-verifica`

Questo documento non definisce ancora un'architettura permanente. Formula la trasformazione candidata che il repository deve verificare.

## Trasformazione candidata

Trasformare un'intenzione umana incompleta in un cambiamento operativo verificabile, senza introdurre decisioni non autorizzate.

## Stato iniziale

Una richiesta può essere incompleta, ambigua o priva di una soluzione già determinata.

## Stato finale atteso

La richiesta è riformulata come trasformazione esplicita:

```text
stato iniziale → stato finale desiderato
```

Lo stato finale deve essere abbastanza preciso da permettere la definizione successiva di un'attività verificabile, ma non deve anticipare una soluzione tecnica non ancora giustificata.

## Operazioni richieste

L'esecutore deve:

1. estrarre i fatti disponibili;
2. distinguere obiettivi, vincoli e informazioni mancanti;
3. dichiarare le assunzioni residue;
4. formulare la trasformazione richiesta;
5. indicare come verificare che la trasformazione sia stata compresa correttamente.

## Operazioni vietate

L'esecutore non deve:

- trasformare direttamente un'idea in architettura;
- introdurre componenti, categorie o workflow non dimostrati;
- presentare un'ipotesi come decisione;
- modificare il repository oltre l'ambito autorizzato;
- dichiarare valida la trasformazione senza una verifica concreta.

## Output minimo

```text
Stato iniziale:
Stato finale desiderato:
Vincoli:
Assunzioni residue:
Criterio di verifica:
```

## Criterio di accettazione

Il contratto è candidato a essere mantenuto quando, applicato a una richiesta incompleta:

- produce una trasformazione comprensibile e verificabile;
- non introduce una soluzione prematura;
- rende esplicite le assunzioni;
- permette di progettare il passo successivo senza confondere proposta e decisione.

## Decisione successiva

Dopo l'esecuzione del caso di verifica, il contratto deve essere mantenuto, modificato o rifiutato sulla base delle evidenze registrate.
