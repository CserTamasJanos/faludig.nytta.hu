# RZ első melóban alkalmazott szoftvere.
# az eredeti - általa megírt - kód: mappak_2.py

import os
from csv import reader

directories = ['1_RFP_ajánlat', '2_PO', '3_Contract', '4_Invoices', '5_Audit_Check', '6_service documents_forms']

opened_file = open("nevek.csv", encoding="utf-8")
read_file = reader(opened_file)
names = list(read_file)
# vagy egy sorban az egész, bár az nem feltétlenül szép:
# nevek = list(reader(open("nevek.csv", encoding="utf-8")))

# én jobban szeretek abban a mappában lenni, amiben dolgozni kell, és itt a kövi sorban ugye nyilván attól függően, hogy hol van a .py file abszalút, vagy relatív hivatkozást adok meg
path = "Alvállalkozók"
os.chdir(path)

for name_list in names:
    dir_name = name_list[0]
    os.mkdir(dir_name)
    for dir in directories:
        os.chdir(dir_name)      # itt ugye az is jó, hogy nem .chdir-ezek, hanem sub_dir_name = f"{dir_name}\\{dir}"" és akkor .mkdir(sub_dir_name)
        os.mkdir(dir)           # csak ha már használom az os module-t akkor miért ne így :D :D
        os.chdir("..")          # és a két sorral feljebbi sub_dir_name-ben azért \, mert a windóz így használja, de érdekes, hogy működik /-el is (ahogy nálad is)
#                                 és azt meg gondolom tudod, hogy azért 2 db \, mert az 1 db-nak különleges jelentése van
# még az egészet annyival lehetne szépíteni, hogy megvizsgálod, hogy létezik-e már olyan mappa/fájl, amit létre akarsz hozni, hogy ne haljon meg, ha pl. 2x futtatod
# meg mondjuk a 13. sornál is vizsgálhatnánk, hogy létezik-e a mappa, hogy ne halljon meg, ha nem létezik. :D

# feladat1: csináld meg excel makrónak, mert eredetileg egy excel oszlopban vannak a nevek
# feladat2: csináld meg batch vagy shell script-ként, feltételezve, hogy meg van már a nevek.csv fájl