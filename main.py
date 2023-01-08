import pandas as pd
import math
from decimal import Decimal

with open("in.txt", "r") as inputlar:
    metin = inputlar.read()
    veriler = metin.split("\n")
print("Input:\n", veriler)
bs = len(veriler[1])
print("bas sa = ", bs)
veriler = [float(i) for i in veriler]
sinSayisi = int(veriler[0])
print("Sinif sayisi = ", sinSayisi)
veriler.remove(veriler[0])
print("Veriler:\n", veriler)
vs = len(veriler)
print("Veri sayisi = ", vs)
veriler.sort()
print("Siralanmis veriler:\n", veriler)

sinAr = float(round(Decimal((veriler[vs-1]-veriler[0])/sinSayisi), 1))
print("Sinif araligi = ", sinAr)

sinirList = list()
min = veriler[0]
for i in range(0, sinSayisi):
    sin = list()
    sin.append(min)  # sinif alt sinir
    sin.append(float(round(Decimal(min+sinAr), 2)))  # sinif ust sinir
    sinirList.append(sin)
    min = float(round(Decimal(min+sinAr+0.01), 2))
print("Sinif sinirlari:\n", sinirList)

SinOrtDegList = list()
for i in sinirList:
    SinOrtDegList.append(float(round(Decimal((i[0]+i[1])/2), 2)))
print("Sinif orta degerleri:\n", SinOrtDegList)

frekanslar = list()
siniflar = list()
for i in range(0, sinSayisi):
    frekanslar.append(0)
for j in range(0, sinSayisi):
    sinif = list()
    for i in range(0, vs):
        if veriler[i] >= sinirList[j][0] and veriler[i] <= sinirList[j][1]:
            frekanslar[j] += 1
            sinif.append(veriler[i])
    siniflar.append(sinif)
print("Frekanslar:\n", frekanslar)
print("Siniflar:\n", siniflar)

GorFr = list()
for i in frekanslar:
    GorFr.append(float(round(Decimal(i/vs), 2)))
print("Goreli frekanslar:\n", GorFr)

top = 0
for i in veriler:
    top += i
ort = float(round(Decimal(top/vs), 5))
print("Ortalama = ", ort)

max = frekanslar[0]
maxInd = 0
for i in range(sinSayisi):
    if frekanslar[i] > max:
        max = frekanslar[i]
        maxInd = i
d1 = abs(frekanslar[maxInd]-frekanslar[maxInd-1])
d2 = abs(frekanslar[maxInd]-frekanslar[maxInd+1])
mod = float(round(Decimal(sinirList[maxInd][0]+d1/(d1+d2)*sinAr), 1))
print("Mod = ", mod)
mid = vs/2
top = 0
midInd = 0
for i in range(0, sinSayisi):
    top += frekanslar[i]
    if top >= mid:
        midInd = i
        break
Fb = 0
for i in range(0, midInd):
    Fb += frekanslar[i]
medyan = float(round(Decimal(sinirList[midInd][0]+(vs/2-Fb)/frekanslar[midInd]*sinAr), 1))
print("Medyan = ", medyan)

top = 0
for i in range(vs):
    top += veriler[i]
x = top/vs
top2 = 0
for i in range(vs):
    top2 += math.pow(veriler[i]-x, 2)
varyans = float(round(Decimal(top2/(vs-1)), 9))
stSapma = float(round(Decimal(math.sqrt(varyans)), 9))
print("Varyans = ", varyans)
print("Standart Sapma = ", stSapma)


d = {'Alt': sinirList[sinSayisi-1][0], 'Ust': sinirList[sinSayisi-1][0], 'Orta': SinOrtDegList, 'Frekans': frekanslar, 'Goreli Frekans': GorFr}
df2 = pd.DataFrame(data=d)
print(df2)
with open("out.txt", "w+") as outputlar:
    outputlar.write(str(df2))
    outputlar.write("\n\nOrtalama = " + str(ort) + "\n")
    outputlar.write("Mod = " + str(mod) + "\n")
    outputlar.write("Medyan = " + str(medyan) + "\n")
    outputlar.write("Varyans = " + str(varyans) + "\n")
    outputlar.write("Standart Sapma = " + str(stSapma) + "\n")
