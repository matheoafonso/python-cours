# Créé par matheo, le 12/10/2023 en Python 3.7
def moyenne(tab : list) -> float:
    '''
        Fonction moyenne : Prend un tableau de valeurs en paramètre et en retourne la moyenne de ses valeurs.
    '''
    total_temps = sum(resultat for resultat in tab)
    moyenne = total_temps / len(tab)
    return moyenne

def minimum(tab : list) -> float:
    '''
       Fonction minimum : Prend un tableau de valeurs en paramètre et en retourne la valeur minimale.
    '''
    min = 0
    if len(tab) > 0:
        min = tab[0]
        for i in range(len(tab)):
            if tab[i] < min:
                min = tab[i]
    return min

def maximum(tab : list) -> float:
    '''
       Fonction maximum : Prend un tableau de valeurs en paramètre et en retourne la valeur maximale.
    '''
    max = 0
    if len(tab) > 0:
        max = tab[0]
        for i in range(len(tab)):
            if tab[i] > max:
                max = tab[i]
    return max

def etendue(tab : list) -> float:
    '''
       Fonction etendue : Prend un tableau de valeurs en paramètre et en retourne l'étendue des valeurs.
    '''
    max = maximum(tab)
    min = minimum(tab)
    return max - min

def mediane(tab : list) -> float:
    '''
       Fonction mediane : Prend un tableau de valeurs en paramètre et en retourne la valeur médiane.
    '''
    tab.sort()
    n = len(tab)
    if n % 2 == 0:
        mediane = (tab[n // 2 - 1] + tab[n // 2]) / 2
    else:
        mediane = tab[n // 2]

    return mediane


def convertSecondsInMinutesSeconds(temps_s : int) -> list :
    minutes = int(temps_s // 60)
    secondes = int(temps_s % 60)
    result = [minutes, secondes]
    return result

def afficheTemps(nom : str, temps_s : int):
    result = convertSecondsInMinutesSeconds(temps_s)
    print(f"{nom} : {result[0]}m{result[1]}s")


resultats = []
nombre_de_pilotes = int(input("Combien de pilotes dans la course?"))

for i in range(nombre_de_pilotes):
    nom_pilote = str(input("Nom du pilote : "))
    temps_m = int(input("Temps en minutes : "))
    temps_s = int(input("Temps en secondes : "))
    temps_total = temps_m * 60 + temps_s
    resultats.append([nom_pilote, temps_total])

# Calcul de la moyenne
temps_pilotes = [resultat[1] for resultat in resultats]
moy = moyenne(temps_pilotes)

# Calcul du minimum et du maximum
temps_pilotes = [resultat[1] for resultat in resultats]
min = minimum(temps_pilotes)
max = maximum(temps_pilotes)

# Calcul de l'étendue
etendueValeurs = etendue(temps_pilotes)

# Calcul de la médiane
medianeValeurs = mediane(temps_pilotes)

print("\nTableau des résultats :")
print("Nom du pilote | Temps en secondes")
for resultat in resultats:
    print(f"{resultat[0]:<13} | {resultat[1]}")

print("\nStatistiques:")
afficheTemps("Moyenne", moy)
afficheTemps("Minimum", min)
afficheTemps("Maximum", max)
afficheTemps("Etendue", etendueValeurs)
afficheTemps("Médiane", medianeValeurs)
