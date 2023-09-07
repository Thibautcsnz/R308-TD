def superieur_au_seuil(valeur: float, seuil: float = 10.0) -> bool:
    """
    Vérifie si une valeur est supérieure à un seuil donné.
    :param valeur: La valeur à vérifier.
    :param seuil: Le seuil à comparer (par défaut, 10.0).
    :return: True si valeur est supérieure à seuil, sinon False.
    """
    return valeur > seuil

# Demander à l'utilisateur d'entrer la valeur à vérifier
valeur_a_verifier = float(input("Entrez la valeur à vérifier : "))

# Vérifier si la valeur est supérieure au seuil par défaut
if superieur_au_seuil(valeur_a_verifier):
    print(f"La valeur {valeur_a_verifier} est supérieure au seuil par défaut (10.0)")
else:
    print(f"La valeur {valeur_a_verifier} n'est pas supérieure au seuil par défaut (10.0)")

# Demander à l'utilisateur d'entrer le seuil personnalisé
seuil_personnalise = float(input("Entrez le seuil personnalisé : "))

# Utiliser la fonction superieur_au_seuil avec la valeur et le seuil personnalisé
est_superieur = superieur_au_seuil(valeur_a_verifier, seuil_personnalise)

# Utiliser une structure conditionnelle if pour afficher le résultat du seuil personnalisé
if est_superieur:
    print(f"La valeur {valeur_a_verifier} est supérieure au seuil personnalisé ({seuil_personnalise})")
else:
    print(f"La valeur {valeur_a_verifier} n'est pas supérieure au seuil personnalisé ({seuil_personnalise})")


