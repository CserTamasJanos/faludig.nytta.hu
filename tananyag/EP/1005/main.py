# lista = []
# lista2 = ["szöveg1", "szöveg2"]
# print(lista2)
# lista3 = ["szöveg1", 5, 10.5, False]
#
# lista4 = list(range(10))
# lista4.append(10)
# lista4.remove(8)
#
#
# dictionary = {
#     "kulcs1": "érték",
#     "kulcs2": 5,
#     "kulcs3": 10.5,
#     "kulcs4": True
# }
#
# for kulcs in dictionary:
#     print(kulcs)
#
# for kulcs in dictionary.keys():
#     print(kulcs)
#
# for ertek in dictionary.values():
#     print(ertek)
#
# for kulcs in dictionary:
#     print((dictionary[kulcs]))
#
# print(dictionary["kulcs1"])
#
# tuple1 = ("asd", 2, True)
#
# print(tuple1)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[1][1])

import random
#
# veletlen_szam = random.random() # 0 és 1 közötti lebegőpontos számot ad vissza
# print(veletlen_szam)
#
# a = 100
# b = 10
# veletlen_szam2 = random.random() * a + b # 10 és 110 közötti szám
#
# veletlen_szam3 = random.randint(0, 100) #0 még benne van 100 nem
# print(veletlen_szam3)
#
lista = []

for i in range(100):
    lista.append(random.randint(0, 1000))

print(lista)

# sorozatszámítás

# osszeg = 0
# for elem in lista:
#     osszeg += elem # '+' helyett -, *, is jó
#
# print(osszeg)
# print(sum(lista)) # ellenőrzés

#feladat
# n = 100
# db = 0
# osszeg = 0
#
# for j in range(100):
#     db += 1
#     osszeg += lista[j]
#
# avg = osszeg / db
# print(avg)
#
# osszeg = 0
# for elem in lista:
#     osszeg += elem
#
# print(osszeg/len(lista))

# Eldöntés

# i = 0
# while i < len(lista) and not lista[i] < 10:
#     i += 1
#
# van = bool(i < len(lista))
#
# print(van)
#
# #órai példa:
# i = 0
# while i < len(lista) and lista[i] % 2 != 0:
#     i += 1
#
# print(i == len(lista))

# Kiválasztás

# i = 0
# while lista[i] % 2 != 0:  # T tulajdonságos előfeltétel fontos, különben lista[i]-re hiba lesz túl nagy i-nél
#     i += 1
#
# print(i)
#
# # feladat nytta/2
#
nevsor = ['Almási Bálint', "Kovács Jenő", "Kiss Pista", "Teréz Gergő"]
#
# i = 0
# while nevsor[i] != "Kiss Pista":
#     i += 1
#
# print(i)

# Keresés

# i = 0
# while i < len(nevsor) and nevsor[i] != "Teréz Gergő":
#     i += 1
#
# if i < len(nevsor):
#     print(i)
# else:
#     print("Nincs ilyen.")

# órai pelda

# i = 0
# while i < len(lista) and lista[i] % 2 != 0:
#     i += 1
# if i != len(lista):
#     print(lista[i])

#feladat nytta/1
# listasd = [1, 2, 1, 34, 23, 52, 2, 0, 312, 2, 3, 21 ]
#
# i = 0
# while i < len(listasd) and not listasd[i] < 0:
#     i += 1
#
# if i < len(listasd):
#     print(i)
# else:
#     print("Nincs ilyen.")

# Megszámolás

# import math
#
# db = 0
# for elem in lista:
#     if math.sqrt(elem) % 1 == 0:
#         db += 1
#
# print(db)

# Maximumkiválasztás
from timeit import default_timer as timer
t = timer()

maxindex = 0
i = 1
for elem in lista[1:]:
    if elem > lista[maxindex]:
        maxindex = i
    i += 1

print(lista[maxindex])

eltelt = (timer() - t) * 1000
print(eltelt)

#órai megoldás

t = timer()

max_ertek = lista[0]
i = 1
hossz = len(lista)
while i < hossz:
    if lista[i] >max_ertek:
        max_ertek = lista[i]
    i += 1
print(max_ertek)
eltelt = (timer() - t) * 1000
print(eltelt)
print(max(lista))

# ezmiez? csak azért gyorsabb, mert a while-ban van feltétel???  # szóval elvileg a pszeudókódban a számlálós ciklust while-t implementáljuk - ????

import sys                    # ???
t = timer()
max_ertek = sys.maxsize * -1  # ???
for elem in lista:
    if elem > max_ertek:
        max_ertek = elem
eltelt = (timer() - t) * 1000
print(eltelt)
# feladat

magass = {
    "Kitti": 176,
    "Béla": 145,
    "Cecil": 180,
    "László": 155,
    "Pista": 201
}

maxkey = "Kitti"

for key in magass:
    if magass[key] > magass[maxkey]:
        maxkey = key

print(maxkey)

# órai megoldás

dictionary = {
    "Pisti": 176,
    "Nóra": 165,
    "Marci": 182,
    "János": 156,
}

max_ertek = sys.maxsize * -1
for elem in dictionary.values():
    if elem > max_ertek:
        max_ertek = elem

print(max_ertek)

# órai megoldás 2

dictionary = {
    "Pisti": 176,
    "Nóra": 165,
    "Marci": 182,
    "János": 156,
}

max_ertek = sys.maxsize * -1
max_kulcs = ""
for kulcs in dictionary:
    if dictionary[kulcs] > max_ertek:
        max_ertek = dictionary[kulcs]
        max_kulcs = kulcs

print(f"Legmagasabb diák: {max_kulcs}, {max_ertek}cm.")