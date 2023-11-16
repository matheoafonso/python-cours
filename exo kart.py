# Créé par matheo, le 04/10/2023 en Python 3.7
def Moyennee_temps(NBR):
    somme = 0
    calcul = 0
    mini = 60
    max = 0
    for i in range(NBR):
        min = float(input("combien de minute ?"))
        sec = float(input("combien de seconde ?"))
        if sec < mini:
            mini = sec
        if sec > max:
            max = sec
        somme = somme + sec
        if min <= 1:
            somme = somme + 60
    calcul = somme/NBR
    while calcul >= 60:
        minute = int(calcul/60)
        calcul = calcul -60
    print(Mediane)
    print ("Le minima est de : 1 minute " + str(mini) + " secondes. Et le maxima est de : 1 minutes " + str(max) + " secondes.")
    return(str(minute) + " minute " + str(calcul) + " secondes " )
