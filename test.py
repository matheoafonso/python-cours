import random

# Générer un nombre aléatoire entre 50 et 8000
nombre_secret = random.randint(50, 8000)

# Initialiser le nombre d'essais
essais = 0

print("Bienvenue dans le jeu de devinette !")
print("Je pense à un nombre entre 50 et 8000.")

while True:
    essais += 1
    # Demander au joueur de deviner le nombre
    devinette = int(input("Devinez le nombre : "))

    # Vérifier si la devinette est correcte
    if devinette == nombre_secret:
        print(f"Félicitations ! Vous avez deviné le nombre en {essais} essais.")
        break
    elif devinette < nombre_secret:
        print("Le nombre est plus grand. Essayez à nouveau.")
    else:
        print("Le nombre est plus petit. Essayez à nouveau.")
