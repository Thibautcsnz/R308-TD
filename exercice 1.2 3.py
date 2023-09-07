def plus_grand_liste(liste):
    return(max(liste))
def plus_grand_liste_v2(*args) -> int:
    max = args[0]
    for p in args :
        if p> max :
            max = p
    return max

max  = plus_grand_liste_v2(2,3,4,5,6,7,10,20)
print(f"maximum ={max}")

#autre programme
def plus_grande_valeur(liste_valeurs):
    """
    Retourne la plus grande valeur dans une liste de valeurs.

    :param liste_valeurs: La liste de valeurs à examiner.
    :return: La plus grande valeur dans la liste.
    """
    if not liste_valeurs:
        raise ValueError("La liste de valeurs ne peut pas être vide")

    plus_grande = liste_valeurs[0]
    for valeur in liste_valeurs:
        if valeur > plus_grande:
            plus_grande = valeur

    return plus_grande

# Exemple d'utilisation de la fonction
valeurs = [3, 1, 6, 2, 9, 10, 20, ]
resultat = plus_grande_valeur(valeurs)
print("La plus grande valeur dans la liste est :", resultat)
