def plus_grand_nombre(nombre1: int, nombre2: int) -> int:
    nombre1 = input('Entrez le premier nombre : ')
    nombre2 = input('Entrez le deuxième nombre : ')

    if (nombre1 > nombre2):
        return nombre1
    elif (nombre1 < nombre2):
        return nombre2
    else:
        return "égaux"


resultat = plus_grand_nombre(int ,int)
print("Le nombre le plus grand est :", resultat)