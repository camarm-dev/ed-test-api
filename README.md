# ed-test-api
Serve an API which reproduces the EcoleDirecte behavior without an EcoleDirecte account !

ed-test-api is a **testing purposes** development EcoleDirecte like API.

## Lancer

- Configurer dans `config.json`
```json
{
  "static_token": true // Le token est statique alors il n'expirera jamais, sinon il faudra le regénérer toutes les 10 requêtes
}
```
- Installer les dépendances
```shell
pip install fastapi
```
- Lancer le serveur
```shell
python3 main.py
```

- Visiter [localhost:8000](http://localhost:8000/docs)

## Comment ça marche ?

- Un dossier `responses/`, qui contient les définitions des requêtes et leurs réponses (réponses différentes en fonction utilisateur):

eg. `requests/login.json`
```json
{
  "get": {
    "response": {
      "jean": {

      },
      "marie": {

      }
    },
    "action": "func_name(data)"
  }
  
}
```

- "get", "put", "delete", "post": argument verbe
  - response: la réponse pour "Jean" et "Marie"
  - action: nom d'une fonction python pour modifier des valeurs temporaires ([action](#champ-action))

- Un fichier `requests.json` qui lie route et requête :
```json
{
  "/login.awp": "login.json"
}
```

## Ajouter une route

1. Ajouter la route dans `requests.json`, (lier le nom de fichier de l'étape 2)
2. Ajouter les specs de la réponse dans `response/<nom>.json`
3. Si besoin, ajouter une fonction dans `utils.py` (fonction utilisée par `action`)

## Champ action

Le champ `action` doit contenir du code python, qui peut modifier des données temporaires et autres... Les arguments possibles sont:
- `user`: Le nom d'utilisateur
- `token`: Le token
- `conf`: Le contenu du fichier `config.json
- `data`: Le contenu de `data` dans le corps de requête

> [!CAUTION]
> Si vous ne souhaitez pas d'action, mettez `...`

## Contribuer

- Corrigez des requêtes
- Ajoutez des requêtes
- Ou reporter un bug !
