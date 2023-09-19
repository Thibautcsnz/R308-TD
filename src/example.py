def affiche(chaine):
    """
    Affiche une chaîne de caractères précédée de "texte à afficher :".

    :param: chaine: La chaîne de caractères à afficher.
    :type: chaine: str

    :return: Aucune valeur de retour.
    :rtype: None
    """
    print("texte à afficher:", chaine)

class Velo:
    """
    Représente un vélo par sa marque, sa taille de pneu en pouces, sa couleur et son nombre de vitesses.
    """

    def __init__(self, marque, taille_pneu, couleur, nombre_vitesses):
        """
        Initialise une instance de la classe Vélo avec les attributs spécifiés.

        :param marque: La marque du vélo.
        :type marque: str
        :param taille_pneu: La taille des pneus en pouces.
        :type taille_pneu: int
        :param couleur: La couleur du vélo.
        :type couleur: str
        :param nombre_vitesses: Le nombre de vitesses du vélo.
        :type nombre_vitesses: int
        """
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nombre_vitesses = nombre_vitesses
        self.vitesse_courante = 1

    def gear_up(self):
        """
        Augmente la valeur de la vitesse courante du vélo.

        :return: La nouvelle vitesse courante.
        :rtype: int
        """
        if self.vitesse_courante < self.nombre_vitesses:
            self.vitesse_courante += 1
        return self.vitesse_courante

    def gear_down(self):
        """
        Diminue la valeur de la vitesse courante du vélo.

        :return: La nouvelle vitesse courante.
        :rtype: int
        """
        if self.vitesse_courante > 1:
            self.vitesse_courante -= 1
        return self.vitesse_courante

def main():
    """
    Fonction principale qui démontre l'utilisation des éléments précédents.
    """
    # (1) Définir une chaîne de caractères str1
    str1 = "Exemple de chaîne à afficher"

    # (2) Faire appel à la fonction affiche en lui passant la chaîne str1
    affiche(str1)

    # (3) Créer une instance de Vélo nommée v1
    v1 = Velo("MarqueXYZ", 26, "Rouge", 7)

    # (4) Faire appel aux méthodes gear_up et gear_down
    print("Vitesse courante du vélo:", v1.gear_up())
    print("Vitesse courante du vélo après réduction:", v1.gear_down())

if __name__ == "__main__":
    main()
