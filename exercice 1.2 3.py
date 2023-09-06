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
