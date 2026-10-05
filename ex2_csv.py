import csv

taches = [
    { "titre" : "Reviser Python", "faite" : False } ,
    { "titre" : "Lire le cours", "faite" : True } ,
    { "titre" : "Acheter du pain, du lait", "faite" : False }
]

def exporter_csv(taches, chemin):
    with open(chemin,"w",newline="",encoding="utf-8") as file :
        writer = csv.DictWriter (
            file,fieldnames=["titre","faite"]
        )
        writer.writeheader()
        for tache in taches :
            writer.writerow(tache)

def importer_csv(chemin):
    liste = []
    with open(chemin,"r",encoding="utf-8") as file :
        reader = csv.DictReader(file)
        for i in reader :
            if i["faite"] == "True":
                i["faite"] = True
            elif i["faite"] == "False":
                i["faite"] = False
            liste.append(i)
        print(type(liste[0]["faite"]))    
    return liste

exporter_csv(taches,chemin="taches.csv")
importer_csv("taches.csv")
