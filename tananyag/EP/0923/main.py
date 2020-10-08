# print("Hello World!")
# print('Hello World!')
# print("""
# Kedvesd asdas das
# asd
# asd
# asdasdasd
#
#
#
# asdasd
# """)
# print('I\'m Patrik')
# print("Ez a \"Python kurzus kezdőknek\"")
# print("C:\\\\Users\\User\\Documents\\asd")
#
# szoveg = "Szöveg"   # string
# egesz_szam = 10     # int
# valos_szam = 10.5   # float
# logikai = True      # bool
# x = None            # nincs adattípusa
#
# print("*" + "*")
# print("*" * 10)
# print(5 ** 10)
# print(5/2)
# print(5//2)
# print(5%2)
#
# szam1 = int(input("Kérek egy számot: "))
# szam2 = int(input("Kérek még egy számot: "))
#
# print(szam1 + szam2)
#
# print("Összeg: " + str(szam1) + str(szam2))
# print("Összeg: " + str(szam1 + szam2))
#
# print(f"Összeg: {szam1 + szam2}")
#
# kapcsos_zarojel = "{"
# print(f"{kapcsos_zarojel}")
#
#
# szoveg = "Ez egy szöveg"
# print(szoveg)
#
# #math fv-ek
# import math
# print(math.sqrt(25))
#
# #string fv-ek
# print(szoveg.lower())
# print(szoveg.find("E"))
# print(szoveg.count("e"))
#
# #vezérlőszerkezetek
#
# print(True and True)
# print(False or False)
# print(not False)
# print(100 < 100)
# print(100 != 100)
# print(100 >= 100)
#
# #elágazás
#
# homerseklet = int(input("Kérem adja meg a hőmérsékletet: "))
#
# if homerseklet > 25:
#     print("Meleg van.")
# elif homerseklet > 15 and homerseklet <= 25: # ekvivalens azzal, hogy csak simán elif homerseklet > 15 vagy # elif 25 >= homerseklet > 25 - utóbbi fontos, mert intervallumokat is meg lehet adni
#     print("Kellemes.")
# else:
#     print("Hideg van.")

#gyakorlás1
#
# szam = int(input("Kérek egy egész számot: "))
#
# if szam % 2 == 0:
#     print("A szám páros.")
# else:
#     print("A szám páratlan.")

#gyakorlás2
#
# valasz = input("Szeretsz programozni? ")
#
# if valasz.lower() == "igen":
#     print("Sokra viszed még az életben.")
# else:
#     print("Szomorú vagyok. :(")
#
# print(valasz)
#
#
# homerseklet = int(input("Kérem adja meg a hőmérsékletet: "))
#
# while homerseklet > 25:
#     print("Meleg van.")
#     homerseklet -= 1
#

# for x in "Sokra viszed még az életben.":
#     print(x)
#
# a_1 = float(input("Számtani sorozat első eleme: "))
# d = float(input("Számtani sorozat differenciája: "))
#
# counter = 0
#
# while counter < 10:                 #vagy counter nélkül for ciklussal - for i in range(10):        vagy for i in range(start=a_1, step=d):  ??? -ja nem mert TypeError: range() does not take keyword argumentsS
#     print(a_1 + d * counter)        #                                       print(a_1 + d * i)              print(i)
#     counter += 1
#

# for i in range(start=a_1, step=d):
#     print(i)


#számlálós ciklus (for ciklus) - feladatsor

#1. feladat
for i in range(10):
    print("Gábor")

#2. feladat
n = int(input("Kérek egy nemnegatív egész számot: "))
szoveg = input("Kérek egy szöveget: ")
# szovegki = ""

#for i in range(n):              # print() végén újsor nélkül, illetve string.utolsókaraktertleválaszt() ???
#    szovegki += szoveg + " "
#
#print(szovegki)

print(f"{szoveg} " * n)

#7. feladat
for i in range(31):
    print(i ** 2)