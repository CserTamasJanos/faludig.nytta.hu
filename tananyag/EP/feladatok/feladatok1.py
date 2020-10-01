# Kiíratás, adatbekérés billentyűzetről, változók, matematikai műveletek

# 1. feladat (lakcim)

irsz = input("Kérem adja meg az irányítószámát: ")
varos = input("Kérem adja meg a várost: ")
kozter = input("Kérem adja meg a közterület nevét: ")
kjelleg = input("Kérem adja meg a közterület jellegét: ")
hazsz = input("Kérem adja meg a házszámot: ")

cim = f"{irsz} {varos}, {kozter} {kjelleg} {hazsz}"

print(cim)


# 2. feladat (nevek)

vez1 = input("Kérek egy vezetéknevet: ")
vez2 = input("Kérek még egy vezetéknevet: ")
ker1 = input("Kérek egy keresztnevet: ")
ker2 = input("Kérek még egy keresztnevet: ")

print(f"{vez1} {ker1}")
print(f"{vez1} {ker2}")
print(f"{vez2} {ker1}")
print(f"{vez2} {ker2}")


# 3. feladat (fizetes)

havi = int(input("Kérem adja meg a havi fizetést (Ft-ban): "))
evi = havi * 12

print(f"Az éves fizetés: {evi} Ft.")


# 4. feladat

arfolyam = float(input("Kérem adja meg az aktuális EUR/HUF árfolyamot: "))
eur = float(input("Kérem adja meg mennyi EUR-t váltsunk: "))
ft = eur * arfolyam

print(f"Az átváltott összeg: {ft} Ft.")


# 5. feladat (teglalap_ker_ter)

a = float(input("Az a oldal hossza: "))
b = float(input("A b oldal hossza: "))

K = (a + b) * 2
T = a * b

print(f"A téglalap kerülete: {K}; területe: {T}")


import math                                 # A következő két feladathoz.


# 6. feladat (kor_ker_ter)

r = float(input("Kör sugara: "))
K = 2 * r * math.pi
T = r ** 2 * math.pi

print(f"A kör kerülete {K}; területe: {T}")


# 7. feladat (pitagorasz)

a = float(input("Egyik befogó: "))
b = float(input("Másik befogó: "))
c = math.sqrt(a ** 2 + b ** 2)

print(f"Az átfogó: {c}")


# 8. feladat (atlagsebesseg)

d = float(input("A megtett út hossza (km): "))
t = float(input("Eltelt idő (óra): "))
v = d / t

print(f"Az átlagsebesség {v} km/h.")


# 9. feladat (uzemanyag)

fogy = float(input("Az autó fogyasztása (l/100km): "))
bar = float(input("A benzin ára (Ft/l): "))
d = float(input("Az út hosza (km): "))

kolts = (fogy * d * bar) / 100

print(f"Az útiköltség: {kolts} Ft.")


# 10. feladat (testtomegindex)

tomeg = float(input("Testtömege (kg): "))
magas = float(input("Magassága (cm): "))

tindex = tomeg / ((magas / 100) ** 2)

print(f"Testtömegindex (BMI): {tindex}")


# 11. feladat (zoldseges)

alma = 350
szilva = 400
szolo = 699

print(f"alma: {alma} Ft/kg\nszilva: {szilva} Ft/kg\nszőlő: {szolo} Ft/kg")

malm = float(input("Hány kg almát kér? "))
mszi = float(input("Hány kg szilvát kér? "))
mszo = float(input("Hány kg szőlőt kér? "))

almar = malm * alma
sziar = mszi * szilva
szoar = mszo * szolo

veg = almar + sziar + szoar

print(f"{malm} kg alma = {almar} Ft.\n{mszi} kg szilva = {sziar} Ft.\n{mszo} kg szőlő = {szoar} Ft\nVégösszeg: {veg} Ft.")


# 12. feladat (hordo)

hordo = int(input("Mekkora a hordó (egész l)? "))
kancso = int(input("Mekkora a kancsó (egész l)? "))

tkancso = hordo // kancso
marad = hordo % kancso
hanyad = hordo / kancso

print(f"{tkancso} teli kancsó mérhető ki, {marad} l víz marad, a hordó és a kancsó térfogatának hányadosa pedig {hanyad}.")


# 13. feladat (bankjegy)

print("Bankjegyautomata\n\nA legkisebb címlet 1000 Ft, a maximálisan felvehető összeg 300 000 Ft.\n")
felvesz = int(input("Adja meg mekkora összeget kíván felvenni! "))

tize = felvesz // 10000
maradek = felvesz % 10000

ote = maradek // 5000
maradek = maradek % 5000

e = maradek // 1000

ell = tize * 10000 + ote * 5000 + e * 1000

print(f"\nA kiadott bankjegyek:\n\n {tize:2} * 10 000 = {tize*10000:6}\n {ote:2} *  5 000 = {ote*5000:6}\n {e:2} *  1 000 = {e*1000:6}\n{'_' * 21}\n\nÖsszeg:{ell:14} Ft")

# Az itteni és későbbi formázás magyarázatához majd kerítek valami linket.
# A lényeg, hogy a f"{valtozo:formatum}" kifejezésben a 'valtozo' egy változó, a ':' jelenti, hogy formázva lesz, a 'formatum' meg valamilyen formázó karaktersorozat.


# 14. feladat (uzemido) - Szerintem itt az üzemidőt ...nap ...óra ...perc ...másodperc formában gondolta a költő, de az eredeti feladat megoldása az alábbi.

ump = int(input("Az eszköz üzemideje (mp): "))

nap = ump // (3600 * 24)
maradek = ump % (3600 * 24)

ora = maradek // 3600

mp = maradek % 3600

print(f"Az eszköz üzemideje: {nap} nap {ora} óra {mp} másodperc.")


# 15. feladat (utazasikoltseg)

print("Utazási költségtérítés\n")

ut = float(input("Add meg a megtett utat km-ben! "))
fogy = float(input("Add meg az autó fogyasztását 100 km-re literben! "))
ar = float(input("Add meg az üzemanyagárat ft-ban! "))

uzemakolts = (ut * fogy * ar) / 100
pluszkolts = int(ut > 100) * ut * 25                                # Azért így oldottam meg, hogy ne legyen benne if, mert ez a feladat nem az 'Elágazások' feladatosztály része.
osszkolts = uzemakolts + pluszkolts

print(f"\033[;7mKöltségtérítés: {osszkolts:.3f} ft.\033[0;0m")      # \033[;7m => megcseréli a konzol szövegének és hátterének a színét, \033[0;0m => alaphelyzetbe állítja.
                                                                    # https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html


#Elágazások

# 16. feladat (fagy)

hom = float(input("Mennyi a kinti hőmérséklet (C°)? "))

if hom <= 0:
    print("Odakint fagy van.")


# 17. feladat (kerdes)

valasz = input("Szeretsz programozni? ")

if valasz.lower() == "igen":
    print("Még sokra viszed az életben.")

print("Viszont látásra!")                   # A feladatot úgy is lehet értelmezni, hogy az elköszönés az if-en belül van


# 18. feladat (paritas)

szam = int(input("Kérek egy egész számot: "))

if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")


# 19. feladat (oszthato3)

szam = float(input("Kérek egy számot: "))

if szam % 3 == 0:
    print("A szám osztható 3-mal.")
else:
    print("A szám nem osztható 3-mal.")


# 20. feladat (elojel)

szam = complex(input("Kérek egy számot: "))               # Egyébként az összes olyan feladatnál, ahol nincs megadva, hogy milyen számot várunk,
                                                          # float() helyett a complex() fv-t is használhatnánk, mert a komplex számok bővebb halmaz.
                                                          # Mondjuk a <, > reláció nincs a komplexeknél értelmezve, meg oszthatóságnál is lehet, hogy meghal a python. :D

if szam < 0:
    print("A szám negatív.")
elif szam > 0:
    print("A szám pozitív.")
else:
    print("A szám nem pozitív és nem is negatív.")


# 21. feladat (relacio)

szam1 = float(input("Kérek egy számot! "))
szam2 = float(input("Kérek még egy számot! "))

if szam1 < szam2:
    print(f"{szam1} < {szam2}")
elif szam1 == szam2:
    print(f"{szam1} = {szam2}")
else:
    print(f"{szam1} > {szam2}")


# 22. feladat (kozotte)

szam = float(input("Kérek egy számot! "))

if -30 < szam < 40:
    print("A szám -30 és 40 között van.")
else:
    print("A szám nincs a (-30,40) nyílt intervallumban.")


# 23. feladat - kimaradt a feladat "neve"

pont = float(input("A dolgozat pontszáma: "))

if pont < 0 or pont > 100:
    print("A pontszám nem értelmezhető.")
elif 0 <= pont <= 42:
    print("A dolgozat elégtelen.")
elif pont <= 57:
    print("A dolgozat elégséges.")
elif pont <= 72:
    print("A dolgozat közepes.")
elif pont <= 87:
    print("A dolgozat jó.")
else:
    print("A dolgozat jeles.")


# 24. feladat (telepules)

nev = input("A helység neve: ")
leleksz = int(input("A helység lélekszáma: "))

if leleksz <= 0:
    print("Hibás adatbevitel")
elif leleksz < 5000:
    print(f"A(z) {nev} nevű település község.")
elif leleksz < 20000:
    print(f"A(z) {nev} nevű település kisváros.")
elif leleksz < 100000:
    print(f"A(z) {nev} nevű település kozépváros.")
elif leleksz < 1000000:
    print(f"A(z) {nev} nevű település nagyváros.")
else:
    print(f"A(z) {nev} nevű település metropolis.")


# 25. feladat (muvelet)

szam1 = float(input("Kérek egy számot: "))
szam2 = float(input("Kérek mégy egy számot: "))
oper = input("Kérek egy műveleti jelet (+,-,/,*): ")

if oper == "+":
    print(f"Az eredmény: {szam1 + szam2}")
elif oper == "-":
    print(f"Az eredmény: {szam1 - szam2}")
elif oper == "/":
    print(f"Az eredmény: {szam1 / szam2}")
else:                                                   # Feltételezem, hogy az input jó - vagyis csak a '+', '-', '/', '*' karakterek egyike lehet.
    print(f"Az eredmény: {szam1 * szam2}")


# 26. feladat (osztalyzat)

oszt = input("Év végi matematika jegy: ")

if oszt == '1':
    print("Elégtelen.")
elif oszt == '2':
    print("Elégséges.")
elif oszt == '3':
    print("Közepes.")
elif oszt == '4':
    print("Jó.")
elif oszt == '5':
    print("Jeles.")
else:
    print("Hibás adat.")


# 27. feladat (hetnapjai)

nap = input("A nap sorszáma: ")

if nap == '1':
    print("hétfő")
elif nap == '2':
    print("kedd")
elif nap == '3':
    print("szerda")
elif nap == '4':
    print("csütörtök")
elif nap == '5':
    print("péntek")
elif nap == '6':
    print("szombat")
elif nap == '7':
    print("vasárnap")
else:
    print("Hibás adat.")                # A 26-27-28-as feladatokban azért nem szórakozok listákkal, meg ciklusokkal, mert a feladatsor, illetve tananyag szerint "még nem vettük".


# 28. feladat (honapok)

honap = input("A nap sorszáma: ")

if honap == '1':
    print("január")
elif honap == '2':
    print("február")
elif honap == '3':
    print("március")
elif honap == '4':
    print("április")
elif honap == '5':
    print("május")
elif honap == '6':
    print("június")
elif honap == '7':
    print("július")
elif honap == '8':
    print("augusztus")
elif honap == '9':
    print("szeptember")
elif honap == '10':
    print("október")
elif honap == '11':
    print("november")
elif honap == '12':
    print("december")
else:
    print("Hibás adat.")


# 29. feladat (vasarlas)

ar = int(input("Az áru ára (Ft): "))
db = int(input("Vásárolni kívánt mennyiség (db): "))
penz = int(input("Elérhető összeg (Ft): "))

ertek = ar * db

if ertek <= penz:
    print(f"Le tudjuk bonyolítani a vásárlást, és a megmaradt pénz {penz - ertek} Ft.")
else:
    print(f"A pénzünk {penz // ar} db termékre elég.")


# 30. feladat (szokoev)

ev = int(input("Milyen évet írunk? "))

if (ev % 4 == 0 and ev % 100 != 0) or ev % 400 == 0:
    print("Az év szökőév.")
else:
    print("Az év nem szökőév.")