import tkinter as tk
import random

# Fonction pour initialiser la grille de jeu
def initialiser_grille(largeur, hauteur, mines):
    grille = [[0] * largeur for _ in range(hauteur)]
    for _ in range(mines):
        x, y = random.randint(0, largeur - 1), random.randint(0, hauteur - 1)
        while grille[y][x] == -1:
            x, y = random.randint(0, largeur - 1), random.randint(0, hauteur - 1)
        grille[y][x] = -1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < largeur and 0 <= y + j < hauteur and grille[y + j][x + i] != -1:
                    grille[y + j][x + i] += 1
    return grille

# Fonction pour révéler une case
def reveler_case(x, y):
    if 0 <= x < largeur and 0 <= y < hauteur and etat[y][x] == 0:
        etat[y][x] = 1
        if grille[y][x] == -1:
            # Partie terminée (vous avez perdu)
            canvas.create_rectangle(x * taille_case, y * taille_case, (x + 1) * taille_case, (y + 1) * taille_case, fill="red")
            canvas.create_text(x * taille_case + taille_case // 2, y * taille_case + taille_case // 2, text="💣", font=("Arial", 20))
            canvas.update()
            label.config(text="Vous avez perdu !")
        elif grille[y][x] == 0:
            # Aucune mine à proximité, révélez les cases adjacentes
            for i in range(-1, 2):
                for j in range(-1, 2):
                    reveler_case(x + i, y + j)
        else:
            # Affiche le nombre de mines adjacentes
            canvas.create_rectangle(x * taille_case, y * taille_case, (x + 1) * taille_case, (y + 1) * taille_case, fill="light gray")
            canvas.create_text(x * taille_case + taille_case // 2, y * taille_case + taille_case // 2, text=str(grille[y][x]), font=("Arial", 12))

# Fonction appelée lorsqu'une case est cliquée
def case_cliquee(event):
    x, y = event.x // taille_case, event.y // taille_case
    reveler_case(x, y)

# Fonction pour réinitialiser le jeu
def reinitialiser_jeu():
    global grille, etat
    grille = initialiser_grille(largeur, hauteur, mines)
    etat = [[0] * largeur for _ in range(hauteur)]
    canvas.delete("all")
    label.config(text="")

# Paramètres du jeu
largeur, hauteur, mines = 10, 10, 20
taille_case = 30

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Démineur")

# Création du canvas
canvas = tk.Canvas(fenetre, width=largeur * taille_case, height=hauteur * taille_case)
canvas.pack()

# Création d'une grille et d'un état initial
grille = initialiser_grille(largeur, hauteur, mines)
etat = [[0] * largeur for _ in range(hauteur)]

# Création d'une étiquette pour les messages
label = tk.Label(fenetre, text="", font=("Arial", 14))
label.pack()

# Liaison de la fonction case_cliquee à un clic de souris sur le canvas
canvas.bind("<Button-1>", case_cliquee)

# Bouton pour réinitialiser le jeu
bouton_reinitialiser = tk.Button(fenetre, text="Réinitialiser", command=reinitialiser_jeu)
bouton_reinitialiser.pack()

# Lancement du jeu
fenetre.mainloop()
