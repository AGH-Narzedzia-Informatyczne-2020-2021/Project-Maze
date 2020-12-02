import os

#liczba checklist
global n

#tablica zawierajaca nazwy checklist
global ChecklistNames
ChecklistNames =[]

#wybrana checklista
global name

#linia do wykonania (to nie powinnp być tu ale nie umiem inaczej zrobic)
global line

for i in os.listdir("ChecklistDir/lists/"):
    ChecklistNames.append(i)


n=len(ChecklistNames)-1

