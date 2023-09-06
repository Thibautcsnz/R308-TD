def nbr_inf_list(liste, seuil=3):
    j=0
    for i in range(0,len(liste)):
        if liste[i]<seuil:
            j = j+1

    return j

nbr_inf_list()