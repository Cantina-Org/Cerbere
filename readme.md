# Cerbere

Cerbere est le SSO (Single Sign On) de la suite cantina

# Ce service passera en Public Archive lorsque la nouvelle version de Olympe sera faite. Le SSO sera directement intégré dans Olympe pour plus de légerté et plus de simplicité.

### ⚠️: Installer Cerbere peut causer des problèmes sur votre machine si vous faites de mauvaises manipulations ! À vos risques et périls 😆 !

***

## Contribuer :

#### Attention : l'installation de l'outil [Cerbere](https://github.com/Cantina-Org/Cerbere) (conseillé via [Ouranos](https://github.com/Cantina-Org/Ouranos)) est obligatoire ! (Sinon c'est un peu comme avoir une voiture sans les roues 😇.)

### Étape 1:
Cloner votre [fork](https://github.com/Cantina-Org/Cerbere/fork) de Cerbere.

### Étapes 2:
Créer un fichier `config.json` à la racine du projet Cerbere.

### Étapes 3:
Remplisser le fichier `config.json` avec ça: 
```json
{
    "database": [
        {
            "database_username": "",
            "database_password": "",
            "database_addresse": "",
            "database_port": ""
        }
    ],
    "port": 3001
}
``` 
Compléter les champs de la catégorie `database` avec les identifiants de votre base de données.


### Étapes 4:
Lancer le fichier `app.py` via votre éditeur de code. (Vous devez exécuter le fichier depuis le dossier du projet). 

### Étapes 5:
Rendez-vous sur la page `[host:port]/` pour visualiser le service.

*** 

## Pour utiliser Cantina Cerbere en production :

#### ⚠️: Cerbere est encore en développement et peut donc causer des problèmes irréversible sur votre machine (pouvant entrainer une réinstallation complète du système hôte!) si vous faites de mauvaises manipulations !

L'installation de **Cerbere** en production peux être faite grâce à notre outils [**Ouranos**](https://github.com/Cantina-Org/Ouranos). 
Pour cela, veuiller suivres les instructions donnée dans le fichier `README.md` de [**Ouranos**](https://github.com/Cantina-Org/Ouranos)

