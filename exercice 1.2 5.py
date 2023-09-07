def dict(dico, chainecara = "salut"):

    for i in range(0, len(dico)):
        print(chainecara, dico[i])

#def dictv2(**kwargs):
#    for  key, value in kwargs items:
#    print f"{key}= {value}"

#val1 = int(input('entrer la première valeur'))
#val2 = int(input('entrer la deuxème valeur'))

#plus_grand_nbr(val1, val2)

#val3 = int(input("entre la valeur a comparer"))

#seuil(val3)
#seuil(val3,50)

liste=[1,20,2,50,2,55,9]

#print(plus_grand_liste(liste))

#print(nbr_inf_list(liste, 10))

dico={0:"jean", 1:"pierre", 2:"michelle"}
print(len(dico))
dict(dico)

#autre programme
def afficher_dictionnaire(dictionnaire, prefixe=""):
    """
    Affiche l'ensemble des données d'un dictionnaire avec un préfixe.

    :param dictionnaire: Le dictionnaire à afficher.
    :param prefixe: La chaîne de caractères à afficher avant chaque élément (par défaut, vide).
    """
    for cle, valeur in dictionnaire.items():
        print(f"{prefixe}{cle}: {valeur}")

# Exemple d'utilisation de la fonction
donnees = {"nom": "Thibaut", "age": 19, "ville": "Kaysersberg"}
afficher_dictionnaire(donnees, "Donnée: ")