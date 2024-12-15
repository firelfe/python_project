# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 20:16:51 2024

@author: adeta
"""

# Pendu en Python

import random
import sys

def charger_mots_depuis_fichier(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            mots = [ligne.strip() for ligne in f if ligne.strip()]
        if not mots:
            raise ValueError("Le fichier est vide.")
        return mots
    except FileNotFoundError:
        print(f"Erreur : le fichier {fichier} est introuvable.")
        sys.exit(1)
    except ValueError as e:
        print(f"Erreur : {e}")
        sys.exit(1)

def choisir_mot(mots):
    return random.choice(mots)

def afficher_mot(mot, lettres_trouvees):
    return " ".join([lettre if lettre in lettres_trouvees else "_" for lettre in mot])

def demander_lettre(lettres_devinees):
    while True:
        lettre = input("Entrez une lettre : ").lower()
        if len(lettre) != 1 or not lettre.isalpha():
            print("Entrez une seule lettre alphabétique.")
        elif lettre in lettres_devinees:
            print("Vous avez déjà proposé cette lettre.")
        else:
            return lettre

def afficher_pendu(vies):
    """Affiche un dessin du pendu selon les vies restantes."""
    etapes = [
        r"""           +---+
           |   |
               |
               |
               |
               |
        =========""",
        r"""           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        r"""           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        r"""           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        r"""           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========""",
        r"""           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========""",
        r"""           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========="""
    ]
    if vies > 0:
        print(etapes[7 - vies])
    else:
        print(etapes[-1])

def jeu_pendu(fichier):
    mots = charger_mots_depuis_fichier(fichier)
    mot_a_deviner = choisir_mot(mots)
    lettres_trouvees = set()
    lettres_devinees = set()
    vies = 7

    print("Bienvenue dans le jeu du pendu !")
    print(f"Le mot contient {len(mot_a_deviner)} lettres.")

    while vies > 0:
        print("\nMot :", afficher_mot(mot_a_deviner, lettres_trouvees))
        print(f"Lettres déjà proposées : {', '.join(sorted(lettres_devinees))}")
        print(f"Vies restantes : {vies}")
        afficher_pendu(vies)

        lettre = demander_lettre(lettres_devinees)
        lettres_devinees.add(lettre)

        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            print(f"Bonne lettre : {lettre}")
            if lettres_trouvees >= set(mot_a_deviner):
                print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
                return
        else:
            vies -= 1
            print(f"Mauvaise lettre : {lettre}")

    afficher_pendu(vies)
    print("\nVous avez perdu ! Le mot était :", mot_a_deviner)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python pendu.py <fichier_mots>")
        sys.exit(1)

    fichier_mots = sys.argv[1]
    jeu_pendu(fichier_mots)

# --- TESTS UNITAIRES ---

def test_afficher_mot():
    assert afficher_mot("python", {"p", "y"}) == "p y _ _ _ _"
    assert afficher_mot("ordinateur", {"o", "r", "d"}) == "o r d _ _ _ _ _ _ r"
    assert afficher_mot("developpement", set()) == "_ _ _ _ _ _ _ _ _ _ _ _ _"
    assert afficher_mot("logiciel", {"l", "i", "o"}) == "l o _ i _ i _ l"

def test_charger_mots_depuis_fichier(tmp_path):
    fichier = tmp_path / "mots.txt"
    contenu = """python
ordinateur
programme
"""
    fichier.write_text(contenu)
    mots = charger_mots_depuis_fichier(fichier)
    assert mots == ["python", "ordinateur", "programme"]

def test_choisir_mot():
    mots = ["python", "ordinateur", "programme"]
    mot = choisir_mot(mots)
    assert mot in mots

def test_afficher_pendu(capsys):
    afficher_pendu(8)
    captured = capsys.readouterr()
    assert "   +---+" in captured.out
    assert "           |" in captured.out

    afficher_pendu(5)
    captured = capsys.readouterr()
    assert "   +---+" in captured.out
    assert "       O   |" in captured.out