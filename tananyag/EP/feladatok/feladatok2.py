# Számlálós ciklus (for ciklus)

# 1. feladat (nev10)

# for i in range(10):
#     print("Gábor")


# 2. feladat (ismetlesN)

# n = int(input("Kérek egy egész számot: "))
# szoveg = input("Kérek egy szöveget: ")

#                     # 1. megoldás
# szovegki = ""

# for i in range(n):
#     szovegki += f"{szoveg} "

# print(szovegki)

#                     # 2. megoldás - mert a feladat szövegében az szerepel, hogy 'írjuk ki n-szer', illetve itt nem hagyok fölösleges szóközt a végén

# for i in range(n):
#     if i == n - 1:
#         print(szoveg)
#     else:
#         print(szoveg, end=" ")


# import time # - 3. és 4. feladathoz


# 3. feladat (visszaszamol)

# for i in range(10):
#     print(10 - i)
#     time.sleep(1)

# print("Lejárt az időd.")
# time.sleep(3)


# 4. feladat (nev_mozog)

# n = 51
# balszoveg = ""
# jobbszoveg = "_" * (int(n/2) + int((n % 2) != 0))

# for i in range(n):
#     if i == n - 1:
#         jobbszoveg += "_"
#         print(f"Gábor{jobbszoveg}")
#     elif i < n / 2:
#         print(f"{balszoveg}Gábor{jobbszoveg}", end="\r")
#         balszoveg += "_"
#         jobbszoveg = jobbszoveg[1:]
#     else:
#         balszoveg = balszoveg[1:]
#         jobbszoveg += "_"
#         print(f"{balszoveg}Gábor{jobbszoveg}", end="\r")
#     time.sleep(0.1)

# mivel a string egy karakterekből álló lista, és a listákat elvileg itt még nem vettük,
# az indexelés elhagyható, ha csak balról jobbra mozgatom a nevemet

import random # - 5. és 6. feladathoz


# 5. feladat (randomcsillag)

# a default konzol méret windows cmd esetén: 80 karakter szélesség, 25 karakter magasság - ezzel fogok dolgozni.
# pycharmban nem tudom, hogy miért, de nem működik a kódom
# VSCode-ban működik, csak valami nem stimmel
# cmd-ből indítva valami gond van a charset-tel
# Windows PowerShell-ből indítva rendesen működik.
# a zelőző 4 sor igaz a 6. feladatra is.

# segítség a pozícionáláshoz: https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences

# print("\033[2J", end="") # törlöm a képernyőt - ugyanaz, mint cmd vagy WinPS-ben a clear

# for i in range(200):
#     randx = random.randint(1, 80)
#     randy = random.randint(1, 25)
#     print(f"\033[{randy};{randx}H*", end="")

# print("\033[26;1H", end="") # "jó" (26. sor 1. oszlop) helyre állítom a kurzort


# 6. feladat

# segítség a színezéshez:   https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
#                           https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences

print("\033[2J", end="")

for i in range(200):
    randx = random.randint(1, 80)
    randy = random.randint(1, 25)
    
    poziANSI = f"\033[{randy};{randx}H"

    szin = 0                            # sötét színek kódjai 30-tól 37-ig, világos kódok 90-97-ig lesznek

    rand16 = random.randint(0, 15)      # 0-7-ig reprezentálja a sötét színekek, 8-15-ig a világos színeket
    vilagos = 8 <= rand16               # a szín sötét vagy világos
    if vilagos:
        szin = 90 + rand16 - 8          # a világos színek kódjai: 90-től 97-ig, a random számunk 8-15-ig <- eltolom a random számot, hogy 90 és 97 közötti legyen 
    else:
        szin = 30 + rand16              # a sötét színek kódjai: 30-től 37-ig, a random számunk 0-7-ig <- eltolom a random számot, hogy 30 és 37 közötti legyen 
    
    szinANSI = f"\033[{szin}m"


    print(f"{poziANSI}{szinANSI}*", end="")

print("\033[26;1H\033[0m", end="")