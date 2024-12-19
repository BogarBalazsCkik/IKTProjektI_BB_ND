# Bogár Balázs - Németh Dominik 10.B
# Python első beadandó

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
        
