import json
from pathlib import Path

def charger_taches(chemin):
    if not Path(chemin).exists():
        return []
    else :
        with Path(chemin).open("r",encoding="utf-8") as file :
            donnees = json.load(file)
            if isinstance(donnees,list):
                return donnees
            else:
                print("la donne n'est pas une liste")
                raise SystemExit

def sauvegarder_taches(taches, chemin):
    with open(chemin,"w",encoding="utf-8") as file :
        json.dump(taches, file, ensure_ascii=False,indent=2)

try :
    tache = charger_taches("taches.json")
except json.JSONDecodeError:
    print("le fichier de tâches est invalide")
    raise SystemExit

while True:
    print("""
    Menu
-------------
1. Ajouter 
2. Afficher
3. Supprimer
4. Quitter.
    """)
    entre = input("entrez votre choix : ")
    entre_int = int(entre)
    if entre_int == 1 :
        titre = input("entrez un titre : ")
        tache.append(titre)
        sauvegarder_taches(tache,"taches.json")
    elif entre_int == 2 :
        for i,t in enumerate(tache, 1) :
            print(f"{i}.{t}")
    elif entre_int == 3 :
        index = input("entrez l'indice du nombre à supprimer : ")
        index_int = int(index)
        true_index = index_int - 1
        try :
            tache.pop(true_index)
        except IndexError :
            print("entree non valide")
        else :
            sauvegarder_taches(tache,"taches.json")
    elif entre_int == 4 :
        break
    else :
        print("option non valide")

    # au prochain lancement la tache sera supprimée