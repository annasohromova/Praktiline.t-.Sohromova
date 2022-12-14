

1#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu

from cmath import pi
#rom random import *

#print("Puu läbimõõdu arvutamine")
#try: 
#    C=float(input("Määrake puu ümbermõõt -> "))
#    if C>0:
#       d=round(C/pi,2)
#        print(f"Puu läbimõõt = {d}")
#   else:
#        print("Puu läbimõõt on", round(d,2))
#except:
#    print("Andmetüüp on vale")

#2 Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

from math import *
import math

print("Ristüliku omadused")
try:
    M=float(input("Ristlüliku esimene külg ->"))
    N=float(input("Ristlüliku teine külg ->"))
    if M>0 and N>0: 
       c=math.sqrt(N**2+M**2)
       print("Ristküliku pikkus on", round(c,2))
    else:
        print("M ja N peab olema suurem kui 0")
except: 
    print("Andmetüüp on vale")

#3 Leidke järgnevast näiteprogrammist semantiline viga

try:
    aeg=float(input("Mitu tundi kulus sõiduks? "))
    teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
    if aeg>0 and teepikkus:
        kiirus=teepikkus/aeg
        print("Sinu kiirus oli" + str(kiirus) + "km/h")
    else:
         print("aeg ja teepikkus peab olema suurem kui 0")
except:
    print("Andmetüüp on vale")


#4 Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.

print("määrage viis täisarvuu")
try:
    a=float(input("Sisestage esimene täisarv -> "))
    b=float(input("Sisestage teine täisarv -> "))
    c=float(input("Sisestage kolmas täisarv -> "))
    d=float(input("Sisestage neljas täisarv -> "))
    e=float(input("Sisestage viies täisarv -> "))
    if a>0 and b>0 and c>0 and d>0 and e>0:
        h=(a+b+c+d+e)/5
        print("Aritmeetiline keskmine", h)
    else:
        print("a, b ,c ,d , e peab olema suurem kui 0")
except:
    print("Andmetüüp on vale")



#Joonista samasugune konn

print("   @..@")
print("  (----)")
print(" ( \__/ )")
print(" ^^ "" ^^")

#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)


from random import *


print("Seadke kolm külge")
try:
    a=randint(0,100)
    b=randint(0,100)
    c=randint(0,100)
    print(f"a={a}\n,b={b}\n,c={c}")
    if a>0 and b>0 and c>0:
        P=a+b+c 
        print(f"Ümbermõõt on {P}")
    else: 
        print("a, b, c peab olema suurem kui 0")
except:
       print(f"Andmetüüp on vale")
print()


#Pitsa

try:
    P=randint(1,6)
    summa=(12.9*1.1)/P 
    print(f"{P}-st Igaüks maksab {summa}")
except:
    print("Andmetüüp on vale")
print()


#Kütusekulu arvutamine


print("Kütsekulu arvutamine")
try:
    l=float(input("Kütsekulu liitride kogus: "))
    km=float(input("Läbitud kilomeetrid: "))
    if l>0 and km>0:
       kulu=l/km*100
    else:
        print("l ja km peab olema suurem kui 0")
except:
    print(f"Kütsekulu arvutamine 100 km kohta on võrdne: {kulu}") 
print()


#Rulluisutajad
#print("RULLUISTUJAD")
#M=int(input("Minutid: "))
#M=M/60 
#tee=M*29.9 
#print(f"Jõuab {tee} km")
#print()


#Ajateisendus


#print("Ajateisendus " ) 
#M=int(input("Sisesta aja minutites")) 
#H=M//60 #h
#M=M%60 #min
#print(f"{H}:{M}")



#Ülesanne "Ema roobot"
#Ema küsib "mis hinde sa koolis said?", laps vastab ja ootab ema reaktsioon 

print("Ema roobot")
a=input("Sisesta: ")
print(a.isalpha(), a.isdigit())
if a.isdigit() and int(a)>0 and int(a)<=5:
    a=int(a)
    if a==5:
        print("Väga hea")
        pass 
    elif a==4: 
        print("Hea")
        pass
    elif a==3: 
        print("Keskmine...")
        pass 
    elif a==2 or a==1:
        print("Halvasti...")
        pass
