def sup_seuil():

    a = int(input('Entrez un nombre :'))
    b = int(input('Voulez-vous entrez un seuil? : '))


    if (a < b):
        print(f"Le nombre est plus petit que le seuil de {b}")
    elif (a > b):
        print(f"Le nombre est plus grand que le seuil de {b}")
    else:
        if (a == b):
            print("Egaux")

sup_seuil()