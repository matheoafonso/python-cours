import random

# Fonction pour initialiser la grille de jeu
def initialiser_grille(largeur, hauteur, mines):
    grille = [[' ' for _ in range(largeur)] for _ in range(hauteur)]

    # Placer les mines aléatoirement
    for _ in range(mines):
        x, y = random.randint(0, largeur - 1), random.randint(0, hauteur - 1)
        while grille[y][x] == '*':
            x, y = random.randint(0, largeur - 1), random.randint(0, hauteur - 1)
        grille[y][x] = '*'

    return grille

# Fonction pour afficher la grille de jeu
def afficher_grille(grille):
    for row in grille:
        print(" ".join(row))

# Fonction pour compter les mines adjacentes à une case
def compter_mines_adjacentes(grille, x, y):
    mines = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0 <= x + dx < len(grille[0]) and 0 <= y + dy < len(grille) and grille[y + dy][x + dx] == '*':
                mines += 1
    return mines

# Fonction pour révéler une case
def reveler_case(grille, x, y, affiche):
    if grille[y][x] != ' ':
        return

    mines_adjacentes = compter_mines_adjacentes(grille, x, y)
    grille[y][x] = str(mines_adjacentes) if mines_adjacentes > 0 else ' '

    if mines_adjacentes == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < len(grille[0]) and 0 <= y + dy < len(grille):
                    reveler_case(grille, x + dx, y + dy, affiche)

# Fonction principale du jeu
def demineur(largeur, hauteur, mines):
    grille = initialiser_grille(largeur, hauteur, mines)
    affiche = [[' ' for _ in range(largeur)] for _ in range(hauteur)]

    while True:
        afficher_grille(affiche)
        x = int(input("Entrez la coordonnée X (0 à {}): ".format(largeur - 1)))
        y = int(input("Entrez la coordonnée Y (0 à {}): ".format(hauteur - 1)))

        if grille[y][x] == '*':
            print("Vous avez perdu !")
            affiche[y][x] = '*'
            afficher_grille(affiche)
            break
        else:
            reveler_case(affiche, x, y, grille)

        if all(all(cell != ' ' or cell == '*' for cell in row) for row in affiche):
            print("Félicitations ! Vous avez gagné !")
            afficher_grille(affiche)
            break

# Paramètres du jeu
largeur, hauteur, mines = 8, 8, 10

# Lancer le jeu
demineur(largeur, hauteur, mines)
