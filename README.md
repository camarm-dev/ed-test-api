# ed-test-api
Serve an API which reproduces the EcoleDirecte behavior without and EcoleDirecte account !

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

- Un dossier `requests/`, qui contient les définitions des requêtes et leurs réponses (réponses différentes en fonction utilisateur):

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
    "action": ""
  }
  
}
```

- "get", "put", "delete", "post": argument verbe
  - response: la réponse pour "Jean" et "Marie"
  - action: nom d'une fonction python pour modifier des valeurs temporaires (arguments possibles: `data`: request data)

- Un fichier `requests.json` qui lie route et requête :
```json
{
  "/login.awp": "login.json"
}
```

## Contribuer

- Corrigez des requêtes
- Ajoutez des requêtes
- Ou reporter un bug !
