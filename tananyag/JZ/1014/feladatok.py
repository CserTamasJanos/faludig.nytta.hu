import random

# feladat 1

szamok = []
van = False
for i in range(100):
    rnd = random.randint(0, 100)
    szamok.append(rnd)
    if not van and 45 < rnd < 55:
        print(i, rnd)
        van = True

if not van:
    print("Nincs 45 és 55 közötti elem.")


# feladat 2

szamsor = input("Kérek pár számot vesszővel elválasztva:\n").split(',')
prod = 1

for szam in szamsor:
    prod *= int(szam)

print(prod)


# feladat 3

szamok = [random.randint(0, 1000) for i in range(50)]
szam = int(input("Kérek egy számot 0 és 1000 között: "))
if szam in szamok:
    print(szamok.index(szam))
else:
    print("Nincs ilyen szám a listában.")


# feladat 4

szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy nagyobb számot: "))
szamok = []
van = False

for i in range(50):
    rnd = random.randint(szam1, szam2)
    if not van and round((szam1 + szam2) / 2) == rnd:
        van = True
    szamok.append(rnd)

if van:
    print("Szerepel.")
else:
    print("Nem szerepel.")


# feladat 5

primek = 0
for szam in szamok:
    osztok = 0
    for j in range(1, szam + 1):        # átírni while-ra
        if osztok < 3 and szam % j == 0:
            osztok += 1
    if osztok == 2:
            primek += 1
print(primek)
print(szamok)