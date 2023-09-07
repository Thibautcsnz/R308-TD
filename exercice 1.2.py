def nombre (a : int, b : int) -> int:
    #arguments nommés
    a = int(input("Premier nombre :"))
    b = int(input("Deuxième nombre :"))

    if (a < b):
        print(b)
    elif (a > b):
        print(a)
    else:
        if (a == b):
            print("Egaux")

nombre(int, int)

#autre programme

def plus_grand_nombre_reel(nombre1: float, nombre2: float) -> float:
    """
    Retourne le plus grand des deux nombres réels donnés en entrée.8
    :param nombre1: Le premier nombre réel.
    :param nombre2: Le deuxième nombre réel.
    :return: Le plus grand nombre réel entre nombre1 et nombre2.
    """
    return max(nombre1, nombre2)

# Demander à l'utilisateur d'entrer deux nombres réels
nombre1 = float(input("Entrez le premier nombre réel : "))
nombre2 = float(input("Entrez le deuxième nombre réel : "))

# Appeler la fonction plus_grand_nombre_reel avec les nombres saisis par l'utilisateur
resultat = plus_grand_nombre_reel(nombre1, nombre2)

# Afficher le résultat
print("Le plus grand nombre réel est :", resultat)


