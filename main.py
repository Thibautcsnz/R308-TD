
# Classe TriangleRectangle
class TriangleRectangle:
    def __init__(self, cote1, cote2, angle_droit=Point()):
        self.__cote1 = cote1
        self.__cote2 = cote2
        self.__angle_droit = angle_droit

    def hypothenuse(self):
        return math.sqrt(self.__cote1 ** 2 + self.__cote2 ** 2)

    def perimetre(self):
        return self.__cote1 + self.__cote2 + self.hypothenuse()

    def surface(self):
        return 0.5 * self.__cote1 * self.__cote2

    def est_isocèle(self):
        return self.__cote1 == self.__cote2

    # Getters pour les côtés et l'angle droit
    def get_cote1(self):
        return self.__cote1

    def get_cote2(self):
        return self.__cote2

    def get_angle_droit(self):
        return self.__angle_droit

# Exemple d'utilisation de la classe TriangleRectangle
point_angle_droit = Point(0, 0)
triangle1 = TriangleRectangle(3, 4)  # Utilisation du premier constructeur
triangle2 = TriangleRectangle(5, 12, point_angle_droit)  # Utilisation du second constructeur

print("Longueur de l'hypothénuse de triangle1 :", triangle1.hypothenuse())
print("Périmètre de triangle2 :", triangle2.perimetre())
print("Surface de triangle1 :", triangle1.surface())

if triangle1.est_isocèle():
    print("triangle1 est isocèle.")
else:
    print("triangle1 n'est pas isocèle.")

# Accéder aux attributs privés
print("Côté 1 de triangle1 :", triangle1.get_cote1())
print("Côté 2 de triangle1 :", triangle1.get_cote2())
print("Angle droit de triangle2 :", triangle2.get_angle_droit().get_x(), triangle2.get_angle_droit().get_y())
