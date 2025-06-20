#!/bin/bash
# memoire 
number=0;

# programme
while [ $number -lt 5 ]; do # boucle infinie
    echo -n "voulez-vous continuer ? (o/n): "
    read reponse
    if [[ $reponse = 'n' ]];then
        break;
    fi
    number=$((number + 1)); # incrementation de la variable number
    echo $number; # affichage de la variable number
done # fin de la boucle

echo "fin de programme"