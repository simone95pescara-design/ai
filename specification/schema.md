# Contratto delle schede ontologiche

Questo documento definisce la struttura obbligatoria delle schede contenute in `ontology/`.

## Metadati obbligatori

```yaml
id: IDENTIFICATORE_UNIVOCO
nome: Nome leggibile
versione: 0.1.0
stato_specifica: draft | stable | deprecated
data_approvazione: null
dipendenze: []
sostituisce: null
```

### Regole sui metadati

- `id` è stabile, univoco e scritto in maiuscolo.
- `versione` segue il versionamento semantico.
- `data_approvazione` è valorizzata solo per schede `stable` o `deprecated`.
- `dipendenze` contiene esclusivamente ID ontologici.
- `sostituisce` identifica una scheda precedente solo quando esiste una sostituzione formale.

## Sezioni obbligatorie

Ogni scheda deve contenere, nell'ordine:

1. **Definizione** — significato normativo del concetto.
2. **Scopo** — problema modellistico risolto dal concetto.
3. **Confini** — ciò che il concetto include e ciò che esclude.
4. **Attributi** — proprietà necessarie o ammesse.
5. **Invarianti** — condizioni sempre vere per ogni istanza valida.
6. **Relazioni** — collegamenti ammessi con altri concetti ontologici.
7. **Regole di validazione** — criteri verificabili di conformità.
8. **Esempio valido** — caso conforme alla definizione.
9. **Controesempio** — caso apparentemente simile ma non conforme.
10. **Questioni aperte** — ammesse soltanto nello stato `draft`.

## Livelli normativi

Le parole chiave hanno il seguente significato:

- **DEVE**: requisito obbligatorio;
- **NON DEVE**: divieto;
- **DOVREBBE**: raccomandazione motivata, derogabile solo esplicitamente;
- **PUÒ**: possibilità ammessa.

## Criteri per lo stato `stable`

Una scheda può diventare `stable` solo se:

- tutte le sezioni obbligatorie sono complete;
- non contiene questioni aperte;
- i termini impiegati sono definiti o di uso non ambiguo;
- le dipendenze sono già `stable`, salvo eccezione documentata;
- invarianti e regole di validazione sono verificabili;
- esempio e controesempio discriminano correttamente il concetto;
- non introduce contraddizioni con schede già stabili.

## Gestione delle modifiche

- Correzioni editoriali incrementano la versione patch.
- Estensioni retrocompatibili incrementano la versione minor.
- Cambiamenti semantici incompatibili incrementano la versione major.
- Una scheda `stable` non viene riscritta informalmente: ogni modifica deve dichiarare il proprio impatto semantico.
