# Trasformazione corrente

## Stato epistemico

`problema-osservato`

## Formulazione

```text
esecutore libero di dedurre struttura e requisiti da richieste generiche
→ esecutore incapace di modificare senza autorizzazione esplicita e verificabile
```

## Stato iniziale

Una richiesta incompleta poteva essere interpretata come autorizzazione a scegliere autonomamente:

- struttura di directory e file;
- modelli del dominio;
- linguaggio e dipendenze;
- test e CI;
- collocazione degli artefatti.

Questo ha prodotto modifiche dall'alto non giustificate dal problema osservato.

## Stato finale desiderato

Prima di qualsiasi modifica esiste un controllo che distingue:

- ciò che è osservato;
- ciò che è proposto;
- ciò che è deciso;
- ciò che è esplicitamente autorizzato.

Una modifica è eseguibile soltanto quando problema, trasformazione, artefatti, operazioni, vincoli e criterio di verifica sono espliciti. In caso contrario l'esecutore può soltanto analizzare e proporre.

## Evidenza richiesta

Il contratto operativo deve rendere esplicitamente vietati:

- creazione o modifica di struttura non nominata;
- introduzione di modelli e requisiti dedotti;
- aggiunta di strumenti, configurazioni e workflow non autorizzati;
- trasformazione di esempi o pratiche comuni in decisioni;
- uso di richieste generiche come autorizzazione strutturale.

## Fuori ambito

- definizione del dominio data;
- codice applicativo;
- test automatici;
- CI;
- agenti e workflow;
- scelte tecnologiche.

## Limite

Questa trasformazione controlla l'autorità dell'esecutore. Non autorizza ancora alcuna implementazione del sistema di trading.