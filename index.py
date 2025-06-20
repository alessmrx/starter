#!/bin/python

import random;

# jeu.py
nombre_a_trouver = random.randint(1, 100)
print("Le jeu commence")
print(nombre_a_trouver)
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