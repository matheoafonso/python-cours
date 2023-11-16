import math

        #Initilisation des variable
a=0
b=200
h=0

N=int(input("entrez le nombre de température"))
Total=0
Moyenne=0

        #Aquisition et calculs des temperatures
while (a < N):
    a=a+1
    print("Entrez température 1")

    Température=float(input())
    Total=Total+Température       #Calcul Total
    if Température < b:           #Recherche nombre min
        b = Température
    if Température > h:
        h = Température
Moyenne=Total/N
étendu=h-b

        #Afficher des resultats
print("La somme total des température est de",round(Total,1) ,"°C")
print("La moyenne des température est de",round(Moyenne,1) ,"°C")
print("La température minimale est de",round(b,1),"°C")
print("La température maximale est de",round(h,1),"°C")
print("L'étendu est de",round(étendu, 1))



