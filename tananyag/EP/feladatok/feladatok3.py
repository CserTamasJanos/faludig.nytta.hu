# Tömbök

# ez hasznos lesz: https://www.w3schools.com/python/python_ref_list.asp

# 1. feladat

nevek = ["Laci", "Peti", "Kitti", "Gabi", "Erik"]

# a.
for nev in nevek:
    print(nev)

# b.
magassagok = []
for nev in nevek:
    magas = int(input(f"Hány cm magas {nev}? "))
    magassagok.append(magas)

#c.
osszeg = 0
for cm in magassagok:
    osszeg += cm

atlag = osszeg / 5
print(f"Az átlagmagasság {atlag} cm.")

#               vagy

atlag2 = sum(magassagok) / 5
print(f"Az átlagmagasság {atlag2} cm.")

# d.
nevek.sort()
print(nevek)

# a d. feladat csak a nevek[] rendezését kérte, a magasságokét nem. ha szeretnéd, hogy jó legyen az e. feladat, kommenteld ki a 31. sort.

# e.
max_ertek = max(magassagok)
print(f"A legmagasabb ember(ek) magassága: {max_ertek} cm. És ő(k):")
for i in range(5):
    if magassagok[i] == max_ertek:
        print(nevek[i])

for i in range(5):
    szelet_min_ertek = min(magassagok[:5-i])
    min_hely = magassagok.index(szelet_min_ertek)
    min_nev = nevek[min_hely]

    magassagok.pop(min_hely)
    magassagok.append(szelet_min_ertek)

    nevek.pop(min_hely)
    nevek.append(min_nev)

print(nevek)
print(magassagok)


import random # 2., 3., 5., 6., 7., 10. feladathoz


# 2. feladat - a 0-ra végződők számának meghatározása miatt .random() helyett .randint()-et fogok használni, de igazából mindegy

# szamok = [random.randint(51, 149) for i in range(20)] # python-ban így is meg lehet adni egy listát: nev = [ertek/kifejezes for elem in sorozat] - ugyanaz, mint a 65-68-ig sorok

szamok = []
for i in range(20):
    rnd = random.randint(51, 149)
    szamok.append(rnd)

szamok.sort()
for szam in szamok:
    print(szam)

osszeg = sum(szamok)
atlag = osszeg / 20

# vnulldb = sum(szam % 10 == 0 for szam in szamok) - nem csak listákat lehet így megadni... - nev = fuggveny(ertek/kifejezes for elem in sorozat) - ugyanaz, mint a 79-82-ig sorok

vnulldb = 0
for szam in szamok:
    if szam % 10 == 0:
        vnulldb += 1

print(f"A számok összege: {osszeg}; átlaga: {atlag}; 0-ra végződők száma: {vnulldb}")

# összevetve a 63. és 77. sorokat, egysoros megoldás, ha csak a 0-ra végződők megszámolása a feladat:
# osszeg = sum(szam % 10 == 0 for szam in [random.randint(51, 149) for i in range(20)])


# 3. feladat

szamok = []
for i in range(0, 19):
    rnd = 0
    if i == 0:
        rnd = random.randint(10, 99)
    else:
        rnd = random.randint(szamok[i - 1], 99)
    szamok.append(rnd)
    print(szamok[i])


# 4. feladat - while ciklus a feladatsorok szerint "még nem volt", ezért for-ral oldom meg
#            - a .sort() az ékezetes betűket z-nél nagyobbként értékeli, ugyanakkor a feladat szövege csak annyit mond, hogy rendezzük a "tömböt", hogy hogyan, azt nem.

nevek = []
volt_ures = False

for i in range(10):
    if not volt_ures:
        nev = input("Kérek egy nevet: ")
        if nev != "":
            nevek.append(nev)
        else:
            volt_ures = True

nevek.sort()
for nev in nevek:
    print(nev)


# 5. feladat - itt is azért nem while a megoldás, mert "még nem vettük"

# egysoros megoldás:
# szerepel = bool(0 < sum(szam == 13 for szam in [random.randrange(11, 100, 2) for i in range(50)]))

szamok = []
szerepel = False

for i in range(50):                                 
    rnd = random.randrange(11, 100, 2)
    szamok.append(rnd)
    if rnd == 13:
        szerepel = True

if szerepel:
    print("A számok között szerepel a 13.")
else:
    print("A számok között nem szerepel a 13.")


# 6. feladat - a 'kétjegyűek' szó miatt, még mindig int-ekkel dolgozok, float-ra azt a megoldást adnám, hogy megvizsgálom az új rnd-t, hogy szerepel-e már

ketjegyuek = []
for i in range(10, 100):
    ketjegyuek.append(i)
#                                   vagy ketjegyuek = [i for i in range(10, 100)]
szamok = []
for i in range(50):
    rnd = random.choice(ketjegyuek)
    szamok.append(rnd)
    ketjegyuek.remove(rnd)

print(szamok)


# 7. feladat - nem tudom tovább nélkülözni a while-t sajnos. itt csak for-ral csak úgy tudnám megírni, hogy kiírom, hogy 5 különböző számot kérek, de nem tudnám leellenőrizni.
#            - illetve le tudnám, csak ahhoz meg saját függvényt kéne írnom, és itt sem tartunk még.

lottoszamok = [i for i in range(1, 91)]
tippek = []

for i in range(1, 6):
    tipp = input(f"Kérem a {i}. tippet: ")
    while tipp in tippek:                                           # python-ban logikai kifejezések esetén az 'in' is értelmes,
        print("A megadott tipp, már szerepel a tippek között.")     # a while feltétele azt jelenti, hogy a tipp benne van-e a tippek listájában.
        tipp = input("Kérek egy még nem szereplő tippet: ")
    tippek.append(tipp)

huzas = []
for i in range(5):
    rnd = random.choice(lottoszamok)
    huzas.append(rnd)
    lottoszamok.remove(rnd)

print("Az 5-ös lottó eheti számai:")
huzas.sort()
for szam in huzas:
    print(szam)

talalat = sum(tipp in huzas for tipp in tippek)                     # kezdek ellustulni, de remélem a korábbi egysorosok után ez már érthető, ahogy a 159. sor is.
print(f"A találatok száma: {talalat}")


# 8. feladat - eggyel általánosabban oldom meg, egyszerűen állítható a 'napok' változóval, hogy hány napot nézzünk

napok = 12
utalasok = [int(input(f"A(z) {i}. napi átutalások száma: ")) for i in range(1, napok + 1)]                       # igen, lusta vagyok, sry... :D
atlag = sum(utalasok) / napok
tobb_mint_atlag = sum(utalas > atlag for utalas in utalasok)                                                    # igen, lusta... :D
print(f"Az átutalások napi átlaga: {atlag:.2f}. Az átlagnál forgalmasabb napok száma {tobb_mint_atlag}.")


# 9. feladat - megint azért for, mert a while a kövi feladatsorhoz tartozik

rendszamok = []
sebessegek = []

ures = False

for i in range(1, 11):
    if not ures:
        rendszam = input(f"A(z) {i}. jármű rendszáma: ")
        if rendszam == "":
            ures = True
        else:
            sebesseg = float(input("A jármű sebessége (km/h): "))

            rendszamok.append(rendszam)
            sebessegek.append(sebesseg)

van = False
for i in range(len(rendszamok)):
    if sebessegek[i] > 90:
        if not van:
            print("A gyorshajtók adatai: ")
            van = True
        print(f"Rendszám: {rendszamok[i]}; Sebesség: {sebessegek[i]}")

if not van:
    print("Nem volt gyorshajtó.")


# 10. feladat - egyjegyű számokról van szó, ezért megint .randint()-et használok

nev = ["Károly", "Gergely", "Réka", "Angéla", "Lóránt", "Judit", "István", "Gábor", "Katalin", "Anna"]
ido = [random.randint(0, 9) for i in range(10)]             # lustaaaaa

# a.
atlag = sum(ido) / 10
# b.
kettonel_tobb = sum(i > 2 for i in ido)                     # lustaaaaa
# c.
van = bool(sum(i == 0 for i in ido) > 0)                    # lustaaaaa

print(f"Átlagosan {atlag} órát interneteznek a diákok.\n{kettonel_tobb} diák internetezik 2 óránál többet.")
if van:
    print("Van olyan diák, aki egy órát sem internetezik.")
else:
    print("Nincs olyan diák, aki egy órát sem internetezik.")


# 11. feladat - nincs megadva, hogy 'i' most az index, vagy az adott elem sorszáma, én indexnek veszem, de amúgy tökmindegy.
#             - egy fokkal érdekesebb a feladat (meg a fenti sor is), ha 6 helyett valamilyen páratlan számmal osztva nézzük a maradékot.

szamok = [i * (i % 6) for i in range(40)]               # lustaaaaa
# paros = sum(szam % 2 == 0 for szam in szamok) - a kövi ciklus is ugyanazokkal, ugyanazokon iterál végig, a lépésszám miatt inkább ott számolom meg, és inkább a páratlanokat, hogy if se kelljen.

paratlan = 0
for szam in szamok:
    print(szam)
    paratlan += szam % 2

if paratlan == 20:
    print("Ugyanannyi páros és páratlan szám van.")
elif paratlan > 20:
    print("A páratlan számokból van több.")
else:
    print("A páros számokból van több.")


# 12. feladat - ha gyors algoritmust szeretnénk, ez egy tökalap, elemi számelméleti (+kombinatorikai) feladat.
#               kell hozzá ismerni a számelmélet alaptételét,
#               kell hozzá tudni leszámolni hogy hány elemű az A := {0, 1, ..., n1} x {0, 1, ..., n2} x ... x {0, 1, ..., nk} halmaz
#               kell hozzá tudni, hogy ha egy szorzat páratlan, akkor minden tényezőjének páratlannak kell lennie
#               kell hozzá tudni a hatványozás azonosságaiból az (a^2)*(b^2) = (a*b)^2 többtényezős szorzatra és tetszőleges páros hatványra való általánosítását
#               ha mindez megvan, a végén kijön, hogy ha n db cella ajtaját nyitjuk-zárjuk, akkor a történet végén nyitott cellák sorszámai a négyzetszámok 1-től n-ig.
#               az előző sori megoldással csak fel kell sorolni a négyzetszámokat 100-ig: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
#               (   vagy fel kell sorolni a négyzetszámokat n-ig:   megoldas = [i ** 2 for i in range(int(math.sqrt(n)))]    )
#               ha 0 matek hátterünk van, akkor modellezve a történetet, az algoritmus:

cellak = [False for i in range(100)]                # lustaaaaa

for i in range(1, 101):
    for j in range(100):
        if (j + 1) % i == 0:
            cellak[j] = not cellak[j]

print("A nyitott cellák sorszámai: ")
for i in range(1, 101):
    if cellak[i - 1]:
        print(i)