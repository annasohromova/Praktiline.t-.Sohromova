

1#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu

from cmath import pi
from importlib.resources import Package

#print("Puu läbimõõdu arvutamine")
#C=float(input("Määrake puu ümbermõõt -> "))
#d=C/pi
#print("Puu läbimõõt on", round(d,2))
#print()

#2 Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

from math import *
import math

#print("Ristüliku omadused")
#M=float(input("Ristlüliku esimene külg ->"))
#N=float(input("Ristlüliku teine külg ->"))
#c=math.sqrt(N**2+M**2)
#print("Ristküliku pikkus on", round(c,2))
#print()

#3 Leidke järgnevast näiteprogrammist semantiline viga

#aeg=float(input("Mitu tundi kulus sõiduks? "))
#teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
#kiirus=teepikkus/aeg
#print("Sinu kiirus oli" + str(kiirus) + "km/h")
#print()


#4 Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.

#print("määrage viis täisarvuu")
#a=float(input("Sisestage esimene täisarv -> "))
#b=float(input("Sisestage teine täisarv -> "))
#c=float(input("Sisestage kolmas täisarv -> "))
#d=float(input("Sisestage neljas täisarv -> "))
#e=float(input("Sisestage viies täisarv -> "))
#h=(a+b+c+d+e)/5
#print("Aritmeetiline keskmine", h)


#Joonista samasugune konn

#print("   @..@")
#print("  (----)")
#print(" ( \__/ )")
#print(" ^^ "" ^^")

#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)


from random import *


print("Seadke kolm külge")
a=randint(0,100)
b=randint(0,100)
c=randint(0,100)
print(f"a={a}\n,b={b}\n,c={c}")
P=a+b+c 
print(f"Ümbermõõt on {P}")
print()


#Pitsa


P=randint(1,6)
summa=(12.9*1.1)/P 
print(f"{P}-st Igaüks maksab {summa}")
print()


#Kütusekulu arvutamine


print("Kütsekulu arvutamine")
l=float(input("Kütsekulu liitride kogus: "))
km=float(input("Läbitud kilomeetrid: "))
kulu=l/km*100 
print(f"Kütsekulu arvutamine 100 km kohta on võrdne: {kulu}") 
print()


#Rulluisutajad
print("RULLUISTUJAD")
M=int(input("Minutid: "))
M=M/60 
tee=M*29.9 
print(f"Jõuab {tee} km")
print()


#Ajateisendus


print("Ajateisendus " ) 
M=int(input("Sisesta aja minutites")) 
H=M//60 #h
M=M%60 #min
print(f"{H}:{M}")