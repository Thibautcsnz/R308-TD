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
def plus_grand_nbr (valeur1, valeur2):

    if valeur1 < valeur2:
        print(f'le plus grand est {valeur2}')
    else:
        print(f'le plus grand est {valeur1}')

plus_grand_nbr(valeur1, valeur2)

