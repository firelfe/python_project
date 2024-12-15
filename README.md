# python_project
Jeu du Pendu en Python

Ce programme propose un jeu du pendu simple. L'utilisateur doit deviner un mot en proposant des lettres.

- Lancement du jeu :
  Exécutez le script avec le fichier contenant les mots en argument :
  python projet_pendu.py <fichier_mots>
  typiquement il faut que le fichier "projet_pendu" et "mot" soit dans le même dossier,
  la commande nécessite le nom exact des fichier soit : python projet_pendu.py mot.txt

- Format du fichier :
  Chaque mot doit être sur une ligne séparée.
  Exemple : mot
  
            mot1
  
            mot2

- Règles :
  Vous avez 8 vies pour deviner le mot. Chaque erreur vous coûte une vie.
  Un dessin du pendu est affiché à chaque étape.

- Tests :
  Assurez-vous que `pytest` est installé (via `pip install pytest`).
  Utilisez `pytest` pour lancer les tests unitaires présents dans le script :
  pytest projet_pendu.py

Bon jeu !
