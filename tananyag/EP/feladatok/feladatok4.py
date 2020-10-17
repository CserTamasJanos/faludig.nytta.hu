# Szövegkezelés

# hasznos lesz: https://www.w3schools.com/python/python_ref_string.asp

# 1. feladat

import time     # 23., 24. feladathoz
import random   # 18., 19., prog. tételek: 1., 2., 3., 4. feladathoz
print(" ".join("Gábor"))


# 2. feladat

for char in "Gábor":
    print(char)


# 3. feladat    -   2. feladatsor, 28. feladat

nev = "Gábor"
for i in range(len(nev)):
    print(f"{' ' * i}{nev[i]}")


# 4. feladat

szo = input("Kérek egy szót: ")
print(f"*{szo}*")
#       vagy
print(szo.center(len(szo) + 2, '*'))


# 5. feladat    -   2. feladatsor, 27. feladat (ott több megoldást is adok)

szoveg = input("Kérek egy szöveget: ")
print(szoveg[::-1])


# 6. feladat - a feladat "e"-t ír, ez alapján én nem számolnám meg az "E"-ket. ha mégis meg kéne, akkor .lower() vagy .upper() és ugyanez a megoldás

szoveg = input("Kérek egy szöveget: ")
print(szoveg.count('e'))


# 7. feladat    -   csak a nemüres 'szavakat' (karakterláncokat) számolom. egyébként len(szoveg.split())

szoveg = input("Kérek egy szöveget: ")
# igen, itt már teljesen elveszett a motivációm az olvashatóságot illetően, mert valszeg senki nem olvassa a kódom :'( :D :D
szodb = sum(szo != "" for szo in szoveg.strip().split())
# ha mégis olvasod és esetleg nem értenéd a 46. sort, de szeretnéd: dobj egy '3/7'-et discordon - vagy valami
print(szodb)


# 8. feladat    -   a mondat '!' esetén felkiáltó vagy óhajtó is lehet, illetve '...' esetén is kijelentő lesz az output

mondat = input("Kérek egy mondatot: ")
if mondat[-1] == '.':                   # vagy mondat.endswith('.')
    print("A mondat kijelentő.")
elif mondat[-1] == '?':                 # vagy mondat.endswith('?')
    print("A mondat kérdő.")
elif mondat[-1] == '!':                 # vagy mondat.endswith('!')
    print("A mondat felszólító.")
else:
    print("Az utolsó karakter nem a '.', '?', '!' karakterek egyike.")


# 9. feladat

szoveg = input("Kérek egy szöveget: ")
print(szoveg.upper())
print(szoveg.lower())


# 10. feladat

szo = input("Kérek egy szót: ")
# azért írom felül a 'szo' változót, mert azt kéri a feladat, hogy 'cseréljük le' - a print nem is kéne
szo = szo.capitalize()
print(szo)


# 11. feladat

szo = input("Kérek egy szót: ")
if szo.count('j') > 0:
    print("A szóban van 'j' betű.")
else:
    print("A szóban nincs 'j' betű.")


# 12. feladat

szo = input("Kérek egy szót: ")
if szo.count("ly") > 0:
    print("A szóban van 'ly' betű.")
else:
    print("A szóban nincs 'ly' betű.")


# 13. feladat

szo = input("Kérek egy szót: ")
# ha nem érted de szeretnéd: discord -> '3/13' (mint 47. sor komment)
db = sum(szo.count(maganhangzo) for maganhangzo in "aáeéiíoóöőuúüű")
print(db)


# 14. feladat

szo = input("Kérek egy szót: ")
# ezt az str.maketrans()-t úgy kell elképzelni, mintha bent lenne előtte egy 'import str' sor
fordit = str.maketrans("áéíóöőúüű", "aeiooouuu")
# így az str modul maketrans() metódusa ugyanúgy hívható, mint amikor pl.: math.sqrt()-t hívunk
print(szo.translate(fordit))
#                                                                     annyi csak a könnyebbség, hogy a string metódusokhoz nem kell külön importálni az str modult


# 15. feladat

szoveg = input("Kérek egy szöveget: ")
szoveg = szoveg.replace(' ', "\n")
print(szoveg)


# 16. feladat   -   a sorted() fv az ékezetes betűket z-nél nagyobbnak veszi, később oldom meg, hogy magyar abc szerint működjön

szo = input("Kérek egy szót: ")
szo = ''.join(sorted(szo))
# rossz_abc = "abcdefghijklmnopqrstuvwxyzáéíóöőúüű"                                 -   a megoldás gondolata itt az lenne, hogy mindkét abc karaktereit leképezem a 0, 1, ... len(abc) sorozatra
# jo_abc =    "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"                                 -   ha ez megvan, akkor meg a két számsorozat között megadok egy permutációt és akkor lesz egy 'rossz -> számsor -> számsor -> jó' leképezésem
# rossz_abc_kodolas = str.maketrans(rossz_abc, [i for i in range(len(rossz_abc))])  -   list nem lehet argumentum -> nem jó, csináljunk 'kézzel' dictionary-t
# jo_abc_kodolas = str.maketrans(jo_abc, [i for i in range(jo_abc)])                -   list nem lehet argumentum -> nem jó, csináljunk 'kézzel' dictionary-t
print(szo)


# 17. feladat

szo = input("Kérek egy szót: ")
if szo == szo[::-1]:
    print("A szó anagramma.")
else:
    print("A szó nem anagramma.")


# 18. feladat

jelszo = ''.join([random.choice("abcdefgh1234567890_") for i in range(8)])
print(jelszo)


# 19. feladat

vezetek = input("Adja meg a vezetéknevét: ")
kereszt = input("Adja meg a keresztnevét: ")

# a.
felhasznalo = vezetek[:2] + kereszt[:2]
print(felhasznalo)

# b.
felhasznalo = vezetek[:2] + kereszt[-2:]
print(felhasznalo)

# c.
felhasznalo = vezetek[:3] + str(random.randint(100, 999))
print(felhasznalo)


# 20. feladat   -   mi a helyzet a postafiókos irányítószámokkal?

irszam = input("Kérek egy budapesti irányítószámot: ")
print(f"Az irányítószám a(z) {int(irszam[1:3])}. kerülethez tartozik.")


# 21. feladat   -   előfordulhat, hogy több j/ly is szerepel egy szóban, ezt az esetet most nem vizsgálom.
#                   indok: az '...adja meg, hogy j vagy ly a helyes...'-ben a 'vagy' szót kizáróként értelmezem :P

szavak = ["ajtó", "hajó", "gólya", "pólya", "papagáj",
          "lyuk", "hely", "rajz", "jól", "helyes"]
pontok = 0
for szo in szavak:
    kerdes = szo.replace('j', '_').replace('ly', '_')
    valasz = input(f"{kerdes}\nMilyen betű áll az üres helyen?\n")
    if valasz != "" and valasz in szo:
        print("A válasz helyes.")
        pontok += 1
    else:
        print("A válasz helytelen.")

print(f"Elért pontszám: {pontok}.")


# 22. feladat

szoveg = input("Kérek egy szöveget: ")
karakterek = []

for char in szoveg:
    if char not in karakterek:
        karakterek.append(char)
print(f"A szövegben {len(karakterek)} db különböző karakter van.")


# 23. feladat   -   Windows Terminal-ból indítva jól működik, simán cmd-ben, PowerShell-ben nem. 24-es ugyanígy

szo = input("Kérek egy szót: ")
for char in szo:
    time.sleep(1.5)
    print(char, end='\r')
    time.sleep(0.1)
    print(' ', end='\r')


# 24. feladat   -   ANSI kódok magyarázat: feladatok2.py 126. sortól 139. sorig     -    konzolméret amivel dolgozom: 80x25

szo = input("Kérek egy max 80 karakter hosszú szót: ")
torolANSI = "\033[2J"
balfelsoANSI = "\033[1;1H"
print(f"{torolANSI}{balfelsoANSI}{szo}", end="\r")

xANSI = 1
yANSI = 1

for i in range(1, len(szo) + 1):
    xANSI = i
    time.sleep(0.75)
    for j in range(2, 26):
        yANSI = j
        pozicioANSI = f"\033[{yANSI - 1};{xANSI}H"
        print(f"{pozicioANSI} ")
        pozicioANSI = f"\033[{yANSI};{xANSI}H"
        print(f"{pozicioANSI}{szo[i - 1]}")
        time.sleep(0.05)

print("\033[26;1H", end='')


# Programozási tételek 1. (megszámolás, összegzés, maximum- és minimum-kiválasztás, eldöntés, kiválasztás, keresés)

# ez hasznos lesz:          http://info.nytta.hu/temak/prog/elemi_tetelek_of.pdf
# ez lehet, hogy méginkább: http://info.nytta.hu/temak/prog/Programozasi_tetelek.pdf
# ugyan a while ciklus a kövi feladatsoron van, az elemi prog. tételek között már használjuk, így én is használni fogom.
# a másik, hogy 'for i in range(x)' fajta ciklusok helyett, ahol lehe simán a 'for dolog in sorozat' fajta ciklussal dolgozom

# 1. feladat

szamok = [random.randint(10, 99) for i in range(200)]
print(' '.join([str(szam) for szam in szamok]))

# a.    -    összegzés - sum(szamok) helyett
osszeg = 0
for szam in szamok:
    osszeg += szam
atlag = osszeg / 200
print(f"A számok átlaga: {atlag}")

# b.    -    megszámolás - sum(szam > atlag for szam in szamok) helyett
darab = 0
for szam in szamok:
    if szam > atlag:
        darab += 1
print(f"{darab} db átlagon felüli szám van.")

# c.    -    megszámolas - sum(szam % 10 == 0 for sam in szamok) helyett
darab = 0
for szam in szamok:
    if szam % 10 == 0:
        darab += 1
print(f"{darab} db 0-ra végződő szám van.")

# d.    -    maximumkiválasztás, megszámolás - maximum = max(szamok), sum(szam == maximum for szam in szamok) helyett
max_index = 0   # mert a max.kivál. output-hoz kell az index
max_ertek = szamok[0]
for i in range(1, 200):
    if szamok[i] > max_ertek:
        max_ertek = szamok[i]
max_db = 0
for szam in szamok:
    if szam == max_ertek:
        max_db += 1
print(f"A legnagyobb szám {max_ertek} és ez {max_db} db eleme a listának.")

# e.    -    minimumkiválasztás, megszámolás - ugyanaz, mint az előző, csak fordított rel. jellel és max helyett min elnevezésekkel
#            viszont most nem sztenderd módon oldom meg
minimum = min(szamok)
min_db = sum(szam == minimum for szam in szamok)
print(f"A legkisebb szám {minimum} és ez {min_db} db eleme a listának.")

# f.    -    kiválasztás, maximumkiválasztás - most engem nem fog érdekelni az index, csak az érték
max_null = 10
for i in range(200):
    if szamok[i] % 10 == 0 and szamok[i] > max_null:
        max_null = szamok[i]
print(f"A legnagyobb 0-ra végződő szám: {max_null}")

# g.    -    keresés, kiválasztás - azért nem csak kiválasztás, mert nem tudjuk biztosra, hogy van
#                                 - a kiválasztás tétel csak 1 elemet választ ki, de előfordulhat, hogy nem csak 1 többszöröse szerepel a 15-nek
#                                 - ha figyelembe vesszük az előző sort, és az összes többszörös kell, akkor a tétel nem elemi, és a neve kiválogatás
index = 0
while index < 200 and szamok[index] % 15 != 0:
    index += 1
if index == 200:
    print("Nincs a számok között 15-nek egyik többszöröse sem.")
else:   # most megírom külön a kiválasztást is
    index = 0
    while szamok[index] % 15 != 0:
        index += 1
    print(
        f"A számok között szerepel a 15-nek többszöröse, pl.: {szamok[index]}")

# g. egyszerűbb megoldás
index = 0
while index < 200 and szamok[index] % 15 != 0:
    index += 1
if index == 200:
    print("Nincs a számok között 15-nek egyik többszöröse sem.")
else:
    print(
        f"A számok között szerepel a 15-nek többszöröse, pl.: {szamok[index]}")

# g. 'mondjukhogyprecíz' (nem elemi) megoldás
tobbszorosok = []
for szam in szamok:
    if szam % 15 == 0 and szam not in tobbszorosok:
        tobbszorosok.append(szam)
if len(tobbszorosok) > 0:
    print("A számok között szerepel a 15-nek többszöröse és ez(ek):")
    tobbszorosok.sort()
    for tobbszoros in tobbszorosok:
        print(tobbszoros)


# I am really overwhelmed by my dev. internship - first week was tough and there are many more left to survive.
# From now, I will not care anymore about writing the "ideal" solution.
# Feel free to contribute if you want to maintain the style before:
# https://github.com/faludig/faludig.nytta.hu/tree/master/tananyag/EP/feladatok

# 2. feladat
db = 120
dobasok = [random.randint(1, 6) for i in range(db)]
print(' '.join([str(dobas) for dobas in dobasok]))

# a.
gyakorisagok = {}
for dobas in dobasok:
    if dobas not in gyakorisagok:
        gyakorisagok[dobas] = 1
    else:
        gyakorisagok[dobas] += 1

for dobas in gyakorisagok:
    print(f"A(z) {dobas} gyakorisága: {gyakorisagok[dobas]}.")

# b.
if db / 6 in gyakorisagok.values():
    print("Van olyan szám, amelynél a dobások száma az összdobások 1/6-od része.")
else:
    print("Nincs olyan szám, amelynél a dobások száma az összdobások 1/6-od része.")

# c.
max_ertek = max(gyakorisagok.values())
max_helyek = [kulcs for kulcs in gyakorisagok if gyakorisagok[kulcs] == max_ertek]
print("A sorozat módusza(i):")
for szam in max_helyek:
    print(szam)

# d.
min_ertek = min(gyakorisagok.values())
min_helyek = [kulcs for kulcs in gyakorisagok if gyakorisagok[kulcs] == min_ertek]
print("A legkevesebbszer előforduló számok:")
for szam in min_helyek:
    print(szam)

# e.
print("A következő számokat dobtuk legalább 10-szer:")
for szam in gyakorisagok:
    if gyakorisagok[szam] >= 10:
        print(szam)

# f. - igen, azért azt még tartom, hogy a feladatsorok szerint még nem volt while
elofordul = False
for i in range(len(dobasok) - 1):
    if not elofordul and dobasok[i] == dobasok[i + 1]:
        elofordul = True
        print("Létezik 2 dobás, ahol egymás után ugyanazt az eredményt kaptuk.")


# 3. feladat

db_diakok = 20
diakok = [random.randint(160, 190) for i in range(db_diakok)]
db_nalamagasabb = [sum(magasabb > diakok[i] for magasabb in diakok[:i]) for i in range(db_diakok)]
print("Diákok sorszámai, akiket a legtöbb nála magasabb diák előzi meg:")
for i in range(db_diakok):
    if db_nalamagasabb[i] == max(db_nalamagasabb):
        print(f"{i + 1}.")


# 4. feladat

db_meres = 50
min_magassag = 100
max_magassag = 2000
meresek = [random.randint(min_magassag, max_magassag) for i in range(db_meres)]

#a. és b.
db_hegycsucs = 0
min_hegycsucs = max_magassag
for i in range(1, db_meres - 1):
    if meresek[i - 1] < meresek[i] > meresek[i + 1]:
        db_hegycsucs += 1
        if meresek[i] < min_hegycsucs:
            min_hegycsucs = meresek[i]

print(f"A hegycsúcsok száma: {db_hegycsucs}.")
if db_hegycsucs > 0:
    print(f"A legalacsonyabb hegycsúcs {min_hegycsucs} m magas.")


# 5. feladat

db_szavak = 4 # legfeljebb 20
szavak = [input(f"{i + 1}. szó: ") for i in range(db_szavak)]

hossz_leghosszabb = 0
sum_szavakhossza = 0

for szo in szavak:
    hossz = len(szo)
    sum_szavakhossza += hossz
    if hossz > hossz_leghosszabb:
        hossz_leghosszabb = hossz

print(f"A szavak átlagos hossza: {sum_szavakhossza / db_szavak} karakter.")
print("A leghosszabb szó/szavak:")
for szo in szavak:
    if len(szo) == hossz_leghosszabb:
         print(szo)