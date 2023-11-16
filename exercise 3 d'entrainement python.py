# Créé par matheo, le 16/11/2023 en Python 3.7
from math import*
def divisible_par_deux(nombre):

    compteur = 0

    while nombre % 2 == 0:

        nombre = nombre // 2


        compteur += 1


    print(f"L'entier donné est divisible par {compteur} fois de suite.")

entier = int(input("Veuillez entrer un entier positif : "))

divisible_par_deux(entier)


