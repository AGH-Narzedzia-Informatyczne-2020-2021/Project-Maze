import os

global n

global ChecklistNames
ChecklistNames =[]

for i in os.listdir("ChecklistDir/lists/"):
    ChecklistNames.append(i)


n=len(ChecklistNames)-1