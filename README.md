# To-Do List Application

Cette application est une simple To-Do List développée avec Flask et SQLite. Elle permet de gérer des tâches de manière efficace, en offrant des fonctionnalités d'ajout, de mise à jour et de suppression des tâches. Cette application est idéale pour les débutants souhaitant apprendre les bases du développement web avec Flask.

## Fonctionnalités

- **Ajouter des Tâches** : Permet d'ajouter des tâches avec un titre et une description.
- **Mettre à Jour les Tâches** : Permet de marquer les tâches comme complétées ou non complétées.
- **Supprimer des Tâches** : Permet de supprimer des tâches de la liste.
- **Interface Utilisateur Simple** : Utilisation de HTML et CSS pour une interface utilisateur claire et esthétique.
- **Base de Données SQLite** : Stockage des tâches dans une base de données SQLite simple et efficace.

## Structure du Projet

Le projet est structuré comme suit :
TO-DO-LIST-MAIN/
│
├── instance/
│ └── tasks.db
│
├── static/
│ └── styles.css
│
├── templates/
│ └── index.html
│
├── app.py
├── requirements.txt
├── setup.py
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md

- **`app.py`** : Le fichier principal de l'application où se trouvent les routes Flask et la logique de base de données.
- **`instance/`** : Répertoire contenant la base de données SQLite.
  - **`tasks.db`** : Fichier de la base de données SQLite.
- **`static/`** : Répertoire contenant les fichiers statiques (CSS, images, etc.).
  - **`styles.css`** : Fichier CSS pour la mise en page et le style de l'application.
- **`templates/`** : Répertoire contenant les modèles HTML.
  - **`index.html`** : Modèle HTML principal pour afficher les tâches et le formulaire d'ajout.

## Installation et Configuration

1. **Cloner le Dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/to-do-list.git
   cd to-do-list

2. **Créer et Activer un Environnement Virtuel** :
```bash
python -m venv venv
source venv/bin/activate  # Pour Windows utilisez `venv\Scripts\activate`
```

3. **Installer les Dépendances** :
```bash
pip install -r requirements.txt
```
4. **Lancer l'Application** :
```bash
flask run
```

## Utilisation
Accédez à l'application via votre navigateur à l'adresse ```http://127.0.0.1:5000/```.
Utilisez le formulaire pour ajouter de nouvelles tâches.
Cliquez sur les boutons de validation et de suppression pour mettre à jour ou supprimer des tâches.

## Contribuer
Les contributions sont les bienvenues ! Vous pouvez soumettre des pull requests pour corriger des bugs, ajouter des fonctionnalités ou améliorer la documentation.

## Licence
