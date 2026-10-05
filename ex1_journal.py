from pathlib import Path

chemin = Path("journal.txt")
titre = []

if not chemin.exists():
    for i in range(3) :
        entre = input("entrez un titre : ")
        titre.append(entre)
    with chemin.open("w",encoding="utf-8") as file :
        for element in titre :
            file.write(element+"\n")
else :
    with chemin.open("a",encoding="utf-8") as file :
        entre = input("entrez un titre : ")
        file.write(entre+"\n")

with chemin.open("r", encoding="utf-8") as file:
    contenu = file.read()
    print(contenu,end="")

# w sert a ecrire sur le fichier en ecrasant le contenue précedant
# a sert à ajouter du contenue sur le fichier
# r sert à lire le contenu du fichier