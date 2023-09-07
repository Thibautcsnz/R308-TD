#autre programme

def nombre_valeurs_inferieures(liste_valeurs, seuil=3.0):
    """
    Retourne le nombre de valeurs inférieures à un seuil donné dans une liste de valeurs.

    :param liste_valeurs: La liste de valeurs à examiner.
    :param seuil: Le seuil à comparer (par défaut, 3.0).
    :return: Le nombre de valeurs inférieures au seuil.
    """
    compte = 0
    for valeur in liste_valeurs:
        if valeur < seuil:
            compte += 1
    return compte

# Exemple d'utilisation de la fonction avec un seuil par défaut de 3.0
valeurs = [1.5, 2.8, 3.2, 4.7, 0.9]
resultat = nombre_valeurs_inferieures(valeurs)
print("Le nombre de valeurs inférieures au seuil par défaut (3.0) est :", resultat)

# Exemple d'utilisation de la fonction avec un seuil personnalisé
seuil_personnalise = float(input("Entrez le seuil personnalisé : "))
resultat = nombre_valeurs_inferieures(valeurs, seuil_personnalise)
print(f"Le nombre de valeurs inférieures au seuil personnalisé ({seuil_personnalise}) est :", resultat)