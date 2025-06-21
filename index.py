#!/bin/python

import random;
import sys

mode_cheat = False
if len(sys.argv) > 1 and (sys.argv[1] == "--mode" and sys.argv[2] == "cheet"):
    mode_cheat = True

# index.py
nombre_a_trouver = random.randint(1, 100)
print("Le jeu commence")
if mode_cheat:
    print(f"[MODE CHEET] Le nombre à trouver est : {nombre_a_trouver}")
while True:
    reponse = input("Devine le nombre ? ")

    if not reponse.isdigit():
        print("Ce n'est pas un nombre, fais un effort")
        continue

    resultat = int(reponse)

    if resultat == nombre_a_trouver:
        print("C'est exact")
        break
    elif resultat > nombre_a_trouver:
        print("C'est plus petit")
    else:
        print("C'est plus grand")