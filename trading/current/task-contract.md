# Contratto operativo corrente

Questo file definisce esclusivamente autorità, divieti e condizioni di ammissibilità dell'esecutore, umano o AI.

## Regola predefinita

In assenza di autorizzazione esplicita, l'esecutore può soltanto:

- analizzare ciò che esiste;
- riportare fatti e informazioni mancanti;
- formulare proposte senza applicarle;
- chiedere una decisione umana quando una scelta modifica struttura, tecnologia o dominio.

Il silenzio, l'ambiguità o una richiesta generica non costituiscono autorizzazione.

## Autorità consentita

L'esecutore può applicare una modifica soltanto quando tutti gli elementi seguenti sono espliciti:

1. problema osservato;
2. trasformazione richiesta;
3. ambito autorizzato;
4. artefatti che possono essere creati, modificati o eliminati;
5. vincoli da preservare;
6. criterio di verifica;
7. decisione umana che autorizza l'esecuzione.

L'autorizzazione vale esclusivamente per gli elementi nominati e non si estende per analogia.

## Divieti assoluti senza autorizzazione specifica

L'esecutore non può:

- creare, rinominare, spostare o eliminare file e directory;
- scegliere nomi di moduli, package, domini o livelli architetturali;
- introdurre modelli di dominio, entità, schemi o invarianti;
- scegliere linguaggi, framework, librerie, versioni o strumenti;
- aggiungere dipendenze, configurazioni, CI, GitHub Actions o automazioni;
- introdurre test derivati da requisiti non approvati;
- collocare documentazione in directory riservate al codice o ai test eseguibili;
- scegliere strategie, mercati, broker, provider, database o formati dati;
- introdurre agenti, workflow, servizi o orchestratori;
- dedurre che qualcosa sia necessario perché è una pratica comune;
- trasformare una proposta, un esempio o un'ipotesi in implementazione;
- ampliare l'ambito oltre quanto autorizzato;
- utilizzare segreti, credenziali, capitale reale o ambienti operativi;
- dichiarare il sistema redditizio, sicuro o pronto per il reale senza evidenze specifiche.

## Controllo di ammissibilità obbligatorio

Prima di ogni modifica l'esecutore deve produrre e verificare questa dichiarazione:

```text
Problema osservato:
Trasformazione autorizzata:
Artefatti autorizzati:
Operazioni autorizzate:
Decisioni già approvate:
Decisioni ancora mancanti:
Criterio di verifica:
```

Se anche un solo campo necessario è mancante, ambiguo o dedotto, la modifica è vietata.

## Controllo delle modifiche strutturali

È considerata strutturale qualsiasi modifica che introduca o cambi:

- directory;
- file di configurazione;
- package o moduli;
- dipendenze;
- workflow CI;
- modelli del dominio;
- convenzioni condivise;
- responsabilità tra componenti.

Una modifica strutturale richiede sempre una decisione umana esplicita che nomini gli artefatti ammessi. Non può essere autorizzata da formule generiche come «organizza tutto», «partiamo dal dominio data» o «metti la CI».

## Obblighi successivi all'autorizzazione

Ogni modifica autorizzata deve:

1. restare entro gli artefatti e le operazioni nominati;
2. preservare la distinzione tra fatti, ipotesi, proposte e decisioni;
3. lasciare esplicite le informazioni mancanti;
4. introdurre il minimo cambiamento necessario;
5. produrre evidenza rispetto al criterio dichiarato;
6. essere presentata per revisione prima di diventare stato approvato.

## Violazione

Una modifica non autorizzata non viene corretta aggiungendo altra struttura. Deve essere:

1. identificata come violazione;
2. rimossa integralmente;
3. registrata come problema osservato;
4. usata per rafforzare il controllo che avrebbe dovuto impedirla.

## Completamento

Un'attività non è completata perché esistono codice, documenti o configurazioni. È completata soltanto quando la modifica era ammissibile prima dell'esecuzione, i criteri dichiarati sono verificati e l'esito è registrato.