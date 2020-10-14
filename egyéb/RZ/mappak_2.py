#A feladat az volt, hogy a cég alvállalkozóinak neve alapján létre kellett hozni mappákat, és mindegyikhez
#egységesen ugyanazt a 6 alkönyvtárat.

import os
import csv

nevek = []

#Az inputot kimásoltam az Excelbõl Jegyzettömbbe (érdekes módon ha közvetlenül egy Excel-fájlt mentettem csv formátumban,
#akkor az ékezeteket nem olvasta be rendesen a Python), a nevek simán egymás alatt, új sorban.
with open("data1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        nevek.extend(row)
        
#Ez az a 6 mappa, ami mindegyik mappához kellett.
mappák = ['1_RFP_ajánlat', '2_PO', '3_Contract', '4_Invoices', '5_Audit_Check', '6_service documents_forms']
        
for i in range(len(nevek)):
    név = str(nevek[i])
    path = "Alvállalkozók/" + név
    os.mkdir(path)
    for j in range(len(mappák)):
        mappa = str(mappák[j])
        path2 = "Alvállalkozók/" + név + "/" + mappa
        os.mkdir(path2)
