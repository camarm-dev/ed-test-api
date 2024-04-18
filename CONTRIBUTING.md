# Contribuer

Bienvenue sur ce guide de contribution ! Il n'est pas encore très complet, mais vous permettra de comprendre un peu mieux comment fonctionne `ed-test-api`...

_N'hésitez pas à me contacter via [discord](https://discordapp.com/users/690581743425814548) ou par mail (software@camarm.dev) pour plus d'informations..._

## Sommaire
- [Technologies](#technologies)
- [Structure](#structure)
- [Authentification]()
- [Modèles de données]()
- [Routes]()

## Technologies

Ce projet utilise le framework [`fastapi`](https://fastapi.tianglo.com). Concernant les modules supplémentaires :
- `PyJWT` pour la gestion des **tokens JWT**
- L'**ORM** `SQLAlchemy` pour la gestion de la base **SQLite**

## Structure

Le projet est structuré ainsi :
- `database/` - Dossier contenant les base de données SQLite
- `server/` - Dossier contenant le code du serveur
  - `models/` - Dossier contenant les modèles / schémas des différents objets "Ecoledirecte" (voir [Modèles de données]())
  - `routes/` - Dossier contentant les différents fichiers définissant les différentes routes (voir [Routes]())
  - `types/` - Dossier contenant des types utiles
  - `utils/` - Dossier contenant des morceaux de programme réutilisables (ex: pour l'authentification)
  - `main.py` - Programme principal
- `main.py` - Le programme principal, permettant le lancement du serveur
