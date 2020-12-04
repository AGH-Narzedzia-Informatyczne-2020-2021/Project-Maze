import os

# sprawdznia i tworznie folderu lists
directory = "lists"
parent_dir = os.getcwd() + "\ChecklistDir"
path = os.path.join(parent_dir, directory)
if not os.path.exists(path):
    os.mkdir(path)

# liczba checklist
global n

# global ChecklistNames
ChecklistNames = []

# wybrana checklista
global name

# linia do wykonania (to nie powinno być tu ale nie umiem inaczej zrobic)
global line

for i in os.listdir("ChecklistDir/lists/"):
    ChecklistNames.append(i)

n = len(ChecklistNames) - 1
