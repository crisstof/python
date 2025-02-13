# approche sur la recherche et l'itération sur les caractère de la chaine
# vérifiz si le caractèree est un espace ou si la fin de chaine est atteinte
# et mettre à jour la longueur maximale d'un mot obtenu
# affciher le mot le plus long   substr().
# seconde approche l'idée est de diviser les mots de la chaine en une liste
# et de trier la liste dans l'ordre croissant de longueur des mots
# avec sorted()


# le pllus petit mot dans une phrase
def smallestWord(s):
    s = sorted(s, key=len)
    print(s[0])


if __name__ == "__main__":
    s = "Lisez Coding Magazine"
    lp = list(s.split(" "))
    smallestWord(lp)
