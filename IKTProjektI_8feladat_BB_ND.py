# Bogár Balázs - Németh Dominik 10.B
# Python első beadandó

import math
lista=[2, 1, 2, 3, 5, 12, 6, 6, 4, 3]

print("a) feladat:")
tA=[2, 1, 2, 3, 5, 7, 6, 6, 4, 3]
otneltobb=0
for i in (tA):
    if(i<5):
        otneltobb+=1
print(otneltobb,"napon mértünk maximum 5 fokot")

print("b) feladat:")
tB=[2, 1, 2, 3, 5, 7, 6, 6, 4, 3]
kulonbseg=0
poz1=0
poz2=0
for i in range(len(lista)-1):
    if((lista[i+1]-lista[i]>=kulonbseg)):
        kulonbseg=abs(lista[i+1]-lista[i])
        poz1=i+1
        poz2=i+2
print(poz1,"és",poz2,"nap között volt a legnagyobb hőingadozás:",kulonbseg)

print("c) feladat:")
tC=[2, 1, 2, 3, 5, 7, 6, 6, 4, 3]
print("A terjedelme",max(lista)-min(lista),"volt.")

print("d) feladat:")
tD=[2, 1, 2, 3, 5, 7, 6, 6, 4, 3]
atlag=sum(lista)/len(lista)
negyzetkul=0
for i in (lista):
    negyzetkul+=(i-atlag)**2
print("Szórása:",f"{math.sqrt(negyzetkul/(len(lista)-1)):.3f}")