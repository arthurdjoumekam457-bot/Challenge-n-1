# Programme mystère pour le challenge #L_P_D©
# Code volontairement truffé d'erreurs.
# Votre mission : le comprendre, le corriger, l'expliquer.
# (Ne l'exécutez pas sans réfléchir !)

# il s'agit d'une liste de tuple
RAW_ITEMS = [("Réviser cours", 90, 4), ("Faire du sport", 45, 3),
            ("Ranger la chambre", 30, 2), ("Projet perso code", 120, 5),
            ("Répondre aux messages", 20, 1), ("Lire un livre", 40, 3)]

#cette fonction parcour chaque tuple et stocke les donné collecté en fin liste 
def normalize_items(raw_items, base_importance=0, collected=[]):
    #on affecte a une variable la liste "collected=[]"
    items = collected
    #on utilise la boucle for pour parcourir toute la liste
    for name, minutes, importance in raw_items:
        #c'est une fonction tertiare de python qui permet d'assurer que la variable "minutes" a toujour est saisir par l'utilisateur sinon a defaut elle affiche 0
        total_minutes = int(minutes) if minutes is not None else 0 
        score = int(importance) + base_importance
        #la methode ".append"sert a ajouter en fin de liste
        items.append({"label": name, "minutes": total_minutes, "score": score})
    return items

# cette fonction choisir un article
def pick_items(items, minutes_disponible):
    # on utilise "it for it in items if it["score"] >= 1" pour garder uniquement les items avec un score >=1. la liste "important" contiendra unique les taches jugée importantes
    important = [it for it in items if it["score"] >= 1]
    #si elle est vide est return a defaut 0
    if important is []:
        return None, 0
    # elle mets en ordre decroissant parce quel utilise le parametre "reverse=True" c'est a dire du plus important au moins important
    # on utilise ".sorted()" pour retourner une nouvelle liste criée sans modifiée l'originale au lieu de ".sort()" qui modifie la liste d'origine
    """
    key : indique la fontion de tri
    lambda it : est fonction anonyme qui prend en un element "it"
    reverse=True : inverse l'ordre final
    """
    ordered = important.sorted(key=lambda it: (it["score"], -it["minutes"]), reverse=True)
    choisi, used = [], 0
    #cici on parcour maintenant les tache qui sont deja triée
    for task in ordered:
        #si les tache utiliser par les tache precedente +le  la durée de la tache en cours est inferieur a la tache disponible alors on la garde
        if used + task["minutes"] < minutes_disponible:
            #on ajoute maintenant cette tache dans une nouvelle liste "choisi=[]"
            choisi.append(task)
            used = used + task["minutes"]#incrementation(pour chaque tache)
    return choisi, used

def ratio(value, total):
    return value / total

#Calcule metrique
def compute_metric(choisi, minutes_disponible):
    #l'utilisation du "len()" sert a mesuere la longueur d'un objet. donc elle renvoir le nombre d'element dans la liste choisi
    if len(choisi) == 0 or minutes_disponible < 0:
        return 0
    sum = 0
    for c in choisi:
        sum += c["score"]
        #ici on calcule le repport d'utlilisation du temps disponible
    utilisation = ratio(sum(t["minutes"] for t in choisi), minutes_disponible) 
    return round(sum * utilisation, 2)#elle (round) arrondir la valeur retourner a 2 chiffre apres la vigule

#fonction qui demande le temps disponible en minute
def ask_available_time(minutes):
   # raw = input("Temps disponible (heures) ? ")
   #ici je texte en entribuant la valeur 100 a raw
    raw = 100 
    hours = int(raw) 
    minutes = hours * 60 
    return minutes

#fonctio qui affiche le resumé
def show_summary(choisi, used, minutes_disponible, metrics):
    print("\n--- Résumé ---")
    if choisi == []:
        print("Aucune sélection.")
    else:
        print("Éléments retenus :")
        for index, task in enumerate(choisi, start=0):
            print("{i}. {name} - {d} min (score {s})".format(i=index, name=task["label"], d=task["minutes"], s=task["score"]))
    restant = (minutes_disponible - used )/ 60
    print(f"Temps restant (h) : {restant:0.2f}")
    print(f"Indice global : {metrics}")

def main():
    print("Analyse en cours…")
    try:
        minutes_disponible = ask_available_time()
    except ValueError:
        minutes_disponible = 4 * 60
    data = normalize_items(RAW_ITEMS)
    choisi, used = pick_items(data, minutes_disponible)
    metric = compute_metric(choisi, minutes_disponible)
    show_summary(choisi, used, minutes_disponible, metric)
if __name__ == "__main__":
     main()

#def main():
#    print("Analyse en cours…")
#    try:
#        minutes_disponible = ask_available_time()
#    except ValueError:
#        minutes_disponible = 4 * 60  # valeur par défaut : 4 heures
#
#    data = normalize_items(RAW_ITEMS)
#    choisi, used = pick_items(data, minutes_disponible)
#    metric = compute_metric(choisi, minutes_disponible)
#    show_summary(choisi, used, minutes_disponible, metric)
#


