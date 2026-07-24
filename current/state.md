# Stato operativo

## Fatti

- Il repository precedente era un prototipo centrato su un'ontologia non ancora giustificata da casi d'uso.
- È stata approvata una rifondazione senza compatibilità con quella struttura.
- Il materiale precedente deve restare soltanto nella cronologia Git.
- Il primo problema da risolvere è identificare la trasformazione utile prima di progettare l'architettura.

## Decisioni approvate

- Il repository deve sviluppare un protocollo di lavoro verificabile.
- L'AI deve agire come esecutore di istruzioni esplicite, non completare autonomamente le parti mancanti.
- Ogni modifica al repository deve derivare da un'esigenza dimostrata.
- Fatti, decisioni, ipotesi e proposte devono restare distinguibili.
- Nessuna architettura deve essere introdotta prima di aver definito e verificato la trasformazione richiesta.

## Fase corrente

`definizione-trasformazione`

## Obiettivo corrente

Verificare se una richiesta umana incompleta può essere trasformata in una descrizione esplicita e verificabile dello stato iniziale e dello stato finale desiderato, senza anticipare una soluzione tecnica.

## Ipotesi in verifica

- La trasformazione candidata è: trasformare un'intenzione umana incompleta in un cambiamento operativo verificabile, senza introdurre decisioni non autorizzate.
- La forma minima `stato iniziale → stato finale desiderato` può rendere esplicito il cambiamento richiesto.
- La separazione tra stato operativo, contratto dell'attività, contratto di trasformazione e caso di verifica è sufficiente per questo esperimento.

Queste ipotesi non costituiscono ancora regole permanenti.

## Criterio di uscita

La fase termina soltanto quando il caso di verifica della trasformazione è stato eseguito, il risultato è stato registrato e si può decidere se mantenere, modificare o rifiutare il contratto di trasformazione.
