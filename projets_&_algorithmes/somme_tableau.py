def _total(tableau):
    # initialisation d'une variable destinée à stocker le total
    # avant d'itérrer dans les valeurs du tableau saisi
    total = 0
    # on passe en revue les éléments du tableau
    for i in tableau:
        total = total + i
        return total
    # initialise
    tableau = []


tableau = [12, 3, 4, 15]
# taille du tableau
n = len(tableau)
total = _total(tableau)
# affiche tableau
print("Le total du tableau est", total)
