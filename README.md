<div align="center">

<br>
<br>

<img src=".github/banner.png"/>

# Ecoledirecte test API
_ed-test-api is a **testing purposes** development EcoleDirecte like API._


Ce programme sert une API qui reproduit le fonctionnement de l'API d'Ecoledirecte !


</div>

## Sommaire
- [À propos](#à-propos)
- [Compatibilité](#compatibilité)
- [Roadmap](#roadmap)
- [Déployer](#déployer)
- [Contribuer](#contribuer)

## À propos

Ce projet a été créé suite au développement et à la montée des clients alternatifs Ecoledirecte pour permettre à leur développeur de tester simplement et rapidement les fonctionnalités, en assurant leur compatibilité avec Ecoledirecte...

## Compatibilité

- Compatible comptes élèves seulement pour l'instant.
- Les tokens utilisés sont différents: ce sont des tokens JWT.
- Voir [roadmap](#roadmap) pour la compatibilité des fonctionnalités.

> [!CAUTION]
> This project is under a full rewrite, so the roadmap is outdated and code is not stable !

## Roadmap

- [ ] Login
  - [ ] Token expiration
  - [ ] Multiple accounts support
  - [ ] Modules comptes
- [ ] Timeline & timelineCommune
- [ ] EDT
  - [ ] Récupérer par jour
  - [ ] Récupérer en tre deux dates
  - [ ] Dataset d'une semaine
- [ ] Devoirs
  - [ ] Dataset d'une semaine de devoirs 
  - [ ] Statut fait / non fait
  - [ ] Lister
  - [ ] Lister par jour
- [ ] Notes

- [ ] Swagger
  - [ ] Body data
  - [ ] Réponses

**Web admin**
- [ ] Modifier chaque objet
- [ ] Modifier chaque objet en brut

## Déployer

Ce projet est déployable facilement, dans n'importe quel contexte...

### Bare metal

Lancer le serveur de test directement avec python :
- Installation des dépendances
```shell
pip install -r requirements.txt
```
- Configurez selon vos envies en modifiant [config.json]()
- Lancer le serveur
```shell
python3 main.py
```

### Docker

Déployer simplement ed-test-api avec Docker :

#### Créez votre propre image
- Construction de l'image
```shell
docker build -t . ed-test-api
```
- Configurez selon vos envies en modifiant [config.json]()
- Lancer le conteneur
```shell
docker run -d --rm -p 8000:8000 ed-test-api
```

#### Ou créez un conteneur avec une image pré-construite

> [!WARNING]
> L'image n'est pas encore déployée !

- N'oubliez pas d'inclure un `config.json` et / ou **une base de donnée** via les volumes, si vous souhaitez utiliser une configuration autre que par défaut et / ou réutiliser des données...
```shell
docker run -d --rm -p 8000:8000 [-v config.json:/web/config.json -v database.db:/web/database/database.db] ghr.io/camarm/ed-test-api
```

### config.json

```js
{
  "database": "database/database.db", // Chemin jusqu'à la base de données
  "secret": "ne pas laisser vide..." // Secret utilisé pour les token JWT (`openssl rand -base64 172 | tr -d '\n'`)
}

```

## Contribuer

- Reporter des bugs ou suggérer des modifications via les [issues](/issues).
- Ajouter une fonctionnalité: [`CONTRIBUTING.md`](CONTRIBUTING.md)
