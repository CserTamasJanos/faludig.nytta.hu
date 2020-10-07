# Számlálós ciklus (for ciklus)

# 1. feladat (nev10)

for i in range(10):
    print("Gábor")


# 2. feladat (ismetlesN)

n = int(input("Kérek egy egész számot: "))
szoveg = input("Kérek egy szöveget: ")

#                      1. megoldás
szovegki = ""

for i in range(n):
    szovegki += f"{szoveg} "

print(szovegki)

#                      2. megoldás - mert a feladat szövegében az szerepel, hogy 'írjuk ki n-szer', illetve itt nem hagyok fölösleges szóközt a végén

for i in range(n):
    if i == n - 1:
        print(szoveg)
    else:
        print(szoveg, end=" ")


import time # - 3. és 4. feladathoz


# 3. feladat (visszaszamol)

for i in range(10):
    print(10 - i)
    time.sleep(1)

print("Lejárt az időd.")
time.sleep(3)


# 4. feladat (nev_mozog)

n = 51
balchar = ""
jobbchar = "_" * (int(n/2) + int((n % 2) != 0))       # a sor hátsó n/2 karaktere (n/2 + 1 karaktere, ha n páratlan)

for i in range(n):
    if i == n - 1:
        jobbchar += "_"
        print(f"Gábor{jobbchar}")
    elif i < n / 2:
        print(f"{balchar}Gábor{jobbchar}", end="\r")
        balchar += "_"
        jobbchar = jobbchar[1:]
    else:
        balchar = balchar[1:]
        jobbchar += "_"
        print(f"{balchar}Gábor{jobbchar}", end="\r")
    time.sleep(0.1)

# mivel a string egy karakterekből álló lista, és a listákat elvileg itt még nem vettük,
# az indexelés elhagyható, ha csak balról jobbra mozgatom a nevemet


import random # - 5., 6., 23., 24. és 26. feladathoz


# az 5. és 6. feladatban használt furcsa karaktersorozatok magyarázata: 126. sortól a 139. sorig,
# ha meg akarod érteni, először olvasd el a megoldásokat, majd a magyarázatot, majd újból a megoldásokat


# 5. feladat (randomcsillag)

# a default konzol méret windows cmd esetén: 80 karakter szélesség, 25 karakter magasság - ezzel fogok dolgozni.
# pycharmban nem tudom, hogy miért, de nem működik a kódom
# VSCode-ban működik, csak valami nem stimmel
# cmd-ből indítva valami gond van a charset-tel
# Windows PowerShell-ből indítva rendesen működik.
# az előző 4 sor igaz a 6. feladatra is.

# segítség a pozícionáláshoz: https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences

print("\033[2J", end="") # törlöm a képernyőt - ugyanaz, mint cmd vagy WinPS-ben a clear

for i in range(200):
    randx = random.randint(1, 80)
    randy = random.randint(1, 25)
    print(f"\033[{randy};{randx}H*", end="")

print("\033[26;1H", end="") # "jó" (26. sor 1. oszlop) helyre állítom a kurzort


# 6. feladat (randomszin)

# segítség a színezéshez:   https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
#                           https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences

print("\033[2J", end="")

for i in range(200):
    randx = random.randint(1, 80)
    randy = random.randint(1, 25)
    
    poziANSI = f"\033[{randy};{randx}H"

    szin = 0                            # sötét színek kódjai 30-tól 37-ig, világos kódok 90-97-ig lesznek

    rand16 = random.randint(0, 15)      # 0-7-ig reprezentálja a sötét színeket, 8-15-ig a világos színeket
    vilagos = 8 <= rand16               # a szín sötét vagy világos (0-7-ig False, 8-15-ig True)
    if vilagos:
        szin = 90 + rand16 - 8          # a világos színek kódjai: 90-től 97-ig, a random számunk 8-15-ig <- eltolom a random számot, hogy 90 és 97 közötti legyen 
    else:
        szin = 30 + rand16              # a sötét színek kódjai: 30-től 37-ig, a random számunk 0-7-ig <- eltolom a random számot, hogy 30 és 37 közötti legyen 
    
    szinANSI = f"\033[{szin}m"


    print(f"{poziANSI}{szinANSI}*", end="")

print("\033[26;1H\033[0m", end="") # "jó" (26. sor 1. oszlop) helyre állítom a kurzort, és reset-elem a grafikus tulajdonságait


# string-ekben a \ karakter-t escape karakternek hívják, segítségével lehet irányítani, színezni - és sok más - a kurzort.
# Pl.: \n új sort dob, és az új sor elejére viszi a kurzort.

# a kurzor pozícióját a '\033[ y ; x H' karakterosorozattal (idézöjelek és space-ek nélkül) lehet megadni,
# ahol y a balfelső saroktól - (1,1) pont - mért függőleges, x a balfelső saroktól mért vízszintes koordináta

# a szöveg színét a '\033[ c m' k karakterosorozattal (idézöjelek és space-ek nélkül) lehet megadni,
# ahol c a kívánt szín színkódja - a színkódok itt találhatóak: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

# a pozíciónál és a színezésnél is, a \ utáni 033 szám jelenti, hogy most ANSI escape kód következik,
# a 033 utáni [ karakter egy konkrét kód osztályt jelöl (Control Sequence Introducer)
# az utolsó, záró karakter jelöli a konkrét kódtípust - H esetén pozícionálunk, m esetén színezünk.
# a [ és záró karakter között a hivatkozott ANSI escape kódtípus argumentumait kell megadni (;-vel elválasztva, ha több van neki)
# ellenőrző kérdés: a jelen fájl (feladatok2.py) 86. sorában, a print függvény argumentumában, mit jelent a J karakter? (és mit jelent a 2, mint a J kódtípus argumentuma?)


# 7. feladat (negyzetszamok)

for i in range(31):
    print(i ** 2)


# 8. feladat (2hatvanyok)

for i in range(1, 31):
    print(2 ** i)


# 9. feladat (paratlan)

for i in range(1, 100, 2):
    print(i)

#        2. megoldás - páratlan számok képletével:

for i in range(1, 51):
    print(2 * i - 1)

#        3. megoldás - az előző, csak 0-tól indulva:

for i in range(50):
    print(2 * i + 1)


# 10. feladat (paratlan2)

for i in range(99, 0, -2):
    print(i)

#        az előző feladat 3. megoldásához hasonlóan:

for i in range(50):
    print(2 * (50 - i) - 1)


# 11. feladat (szamtanisor1)

for i in range(50):
    print(10 + i * 7)

#        így is lehet, csak akkor ki kell számolni az utolsó tagot:

for i in range(10, 354, 7):
    print(i)


# 12. feladat (szamtanisor2)

a_1 = float(input("Kérem a sorozat első tagját: "))
d = float(input("Kérem a sorozat differenciáját: "))

for i in range(20):
    print(a_1 + i * d)


# 13. feladat (szamtanisor3)

a_k1 = float(input("Kérem a két szomszéd közül az elsőt: "))
a_k2 = float(input("Kérem a két szomzéd közül a másodikat: "))

d = a_k2 - a_k1

print("A sorozat előző 10 tagja:")
for i in range(1, 11):
    print(a_k1 - (11 - i) * d)          # azért (11 - i)-vel és nem csak simán i-vel szorzom a d-t, hogy ne visszafelé írja ki a sorozat tagjait

print("\nA sorozat következő 10 tagja: ")
for i in range (1, 11):
    print(a_k2 + i * d)


# 14. feladat (homerseklet_atvaltas)

for i in range(-30, 31):
    print(f"{i}°C = {1.8 * i + 32}°F.")


# 15. feladat (ketjegyu3)

for i in range(-99, 100, 3):
    if not (-10 < i < 10):
        print(i)

#                    vagy:

for i in range(-99, 100):
    if not (-10 < i < 10) and (i % 3 == 0):
        print(i)


# 16. feladat (osztok) - ugyan a feladat szövegében nincs benne, de feltételezem, hogy egész számot várunk, illetve, hogy nem negatív - 17. 18. feladatoknál is

szam = int(input("Kérek egy nemnegatív egész számot: "))

print("A szám osztói: ")
if szam != 0:
    for i in range(1, szam+1):
        if szam % i == 0:
            print(i)
else:
    print("A 0-nak minden szám osztója.")


# 17. feladat (prim_teszt)

szam = int(input("Kérek egy nemnegatív egész számot: "))

osztok = 0
voszto = 2
for i in range(1, szam + 1):
    if szam % i == 0:
        osztok += 1
        if osztok == 2:
            voszto = i

if osztok > 2 or szam == 0:
    print(f"A(z) {szam} nem prím. Valódi osztója pl.: {voszto}.")
elif szam == 1:
    print("Az 1 nem prím, de nem is összetett szám - így nincs valódi osztója.")
else:
    print(f"A(z) {szam} prím.")
    

# 18. feladat (lnko)

szam1 = int(input("Kérek egy nemnegatív egész számot: "))
szam2 = int(input("Kérek egy másik nemnegatív egész számot: "))

lnko = 1

if szam1 == 0:
    print(f"{szam1} és {szam2} legnagyobb közös osztója: {szam2}.")
elif szam2 == 0 or szam1 == szam2:
    print(f"{szam1} és {szam2} legnagyobb közös osztója: {szam1}.")
else:
    for i in range(1, szam1 + 1):                                   # euklideszi algoritmussal sokkal hatékonyabb, de az rekurzív és rekurziót (meg fv-eket) nem tanultunk
        if szam1 % i == 0 == szam2 % i:                             # tökmindegy, hogy melyik számot adom a range-nek, az lnko nem lehet nagyobb a kisebb számnál,
            lnko = i                                                # szóval, ha a nagyobbat adtam, mégtöbb felesleges lépés lesz, de a lényeg, hogy így is úgy is működik
    print(f"{szam1} és {szam2} legnagyobb közös osztója: {lnko}.")


# 19. feladat (szim3hegyu)

for i in range(100, 1000):
    if i % 10 == ((i - i % 100) / 100):                    # lehetne string-ként összehasonlítani az első és utolsó karaktert, de ugye a listákat itt elvileg még nem vettük
        print(i, i * -1)


# 20. feladat (fibonacci)     # itt is egy rekurzív fv-en elegánsabb a dolog, csak még nem tanultuk

a_n_1 = 1                     # a_n_1 az a_n előtti
a_n_2 = 1                     # a_n_2 az a_n_1 előtti elem, csak változónévben nem lehet '-' karakter

print(a_n_1)
print(a_n_2)

for i in range(8):
    a_n = a_n_1 + a_n_2
    print(a_n)

    a_n_2 = a_n_1
    a_n_1 = a_n


# 21. feladat (amstrong)

for i in range(100, 1000):                                    # az amstrong számok definíció szerint csak nemnegatív, egész számok lehetnek
    elsojegy = (i - i % 100) / 100
    masodikjegy = (i % 100 - i % 10) / 10
    harmadikjegy = i % 10
    osszeg = elsojegy ** 3 + masodikjegy ** 3 + harmadikjegy ** 3

    if i == osszeg:
        print(i)


# 22. feladat (faktor)

szam = int(input("Kérek egy nemnegatív egész számot: "))        # feltételezem, hogy csak nemnegatív, egész számokra értelmezzük a faktoriálist

faktor = 1
for i in range(1, szam + 1):
    faktor *= i

print(faktor)


# 23. feladat (6dobas)

db = 0

for i in range(100):
    dobas = random.randint(1, 6)
    print(dobas)
    if dobas == 6:
        db += 1

print(f"\n{db} db 6-os dobás volt.")


# 24. feladat (dobasosszeg10)

db = 0

for i in range(20):
    dobas1 = random.randint(1, 6)
    dobas2 = random.randint(1, 6)
#                                        nem kéri a feladat (az előző sem), hogy írjuk ki a dobásokat
    if dobas1 + dobas2 == 12:
        db += 1

print(f"\n{db} db dupla 6-os dobás volt.")


# 25. feladat (sorosszeg)

sum = 0

for i in range(1, 101):                     # feltételezem, hogy 1-től vesszük a természetes számokat
    sum += i

print(sum)
#                ciklus nélkül (n = 0-ra is jó):
n = 100
sum = int((n * (n + 1)) / 2)
print(sum)


# 26. feladat (dobasosszeg)

sum = 0

for i in range(100):                          # itt sem írom ki a konkrét dobásokat,
    sum += random.randint(1, 6)               # és direkt nem deklaráltam új - dobas nevű - változót, mert szerintem ez még olvasható/érthető
                                              # (aztán lehet, hogy https://www.python.org/dev/peps/pep-0008/ vagy a Clean Code szerint kellene)
print(sum)


# 27. feladat (szoveg_forditva)

szoveg = input("Kérek egy szöveget: ")
                                                # nincs ilyen string method -> nem lehet megúszni, hogy listaként tekintsek a stringre - hiába "itt nem vettük még"
print(szoveg[::-1])                             # https://www.w3schools.com/python/python_howto_reverse_string.asp

#                        2. megoldás, mert mégiscsak a for ciklusok feladatcsoportban vagyunk
visszafele = ""
for i in range(1, len(szoveg) + 1):
    visszafele += szoveg[-i]

print(visszafele)

#                        3. megoldás, mert mégiscsak :D
visszafele = ""
for i in range(len(szoveg)):
    visszafele = szoveg[i] + visszafele

print(visszafele)


# 28. feladat (nev_atlosan) - itt sem lehet megúszni, hogy tudjuk, hogy a string egy karakterlista

nev = "Gábor"
for i in range(len(nev)):
    print(f"{' ' * i}{nev[i]}")



# Egymásba ágyazott ciklusok

# 29. feladat (faktoriális) - az első 10 számot most 1-től 10-ig értelmezem, de ugyanúgy lehetne 0-tól, mint a 22. feladatban

for i in range(1, 10 + 1):
    faktor = 1
    for j in range(1, i + 1):
        faktor *= j
    print(f"{i}! = {faktor}.")


# 30. feladat (primek) - itt is feltételezem, hogy nemnegatív számokról beszélünk, mint a 16., 17., 18-as feladatokban

for i in range(500):
    osztok = 0
    for j in range(1, i + 1):
        if i % j == 0:
            osztok += 1
    if osztok == 2:
        print(i)


# 31., 32., 33. feladatoknál segítség a formázáshoz: https://www.w3schools.com/python/ref_string_format.asp


# 31. feladat (szamok)

#a.
for i in range(1, 10):
    ki = ""
    for j in range(i):
        ki += f"{i:<5}"
    print(ki)
#                                   vagy egy ciklussal:
for i in range(1, 10):
    print(f"{i:<5}" * i)

#b.
for i in range(9, 0, -1):
    ki = ""
    for j in range(i):
        ki += f"{i:>5}"
    print(f"{ki:>45}")
#                                   vagy egy ciklussal:
for i in range(9, 0, -1):
    print(f"{f'{i:>5}' * i:>45}")


# 32. feladat (vakacio) - itt sem kerülhető el a string-ek list-ként hazsnálata

szoveg = "VAKÁCIÓ"

# a.
for i in range(len(szoveg)):
    ki = ""
    for betu in szoveg[i:]:
        ki += f"{betu:<4}"
    print(ki)

# b.
for i in range(len(szoveg), -1, -1):
    ki = ""
    for betu in szoveg[i:]:
        ki += f"{betu:>4}"
    print(f"{ki:>28}")


# 33. feladat (szorzotabla)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:<4}", end="")
    print()


# 34. feladat - lemaradt a neve

# i, j-t nem deklarálok előre, mert akkor while cikusokkal oldanám meg, és ez nem az a feladatsor
# plusz ez ugye elv. C#-os feladatsor, ott sem a számlálos ciklus előtt deklarálom, hanem a ciklus "feltételében"

for i in range(2, -1, -1):
    for j in range(0, 3):
        if i == j:
            print(1)
        else:
            print(0)
    print()


# 35. feladat - szintén nincs neve

# Válasz: c)