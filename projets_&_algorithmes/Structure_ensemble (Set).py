# Un ensemble Python est une collection mutable de données
# qui n'autorise aucune duplication.
# Utilisés pour inclure des tests d'adhésion et éliminer les entrées double.
# La structure de données utilisée ici est le hachage.
# une technique pour effectuer l'insertion, suppression et la traversée o(1)
# en moyenne
# Si plisieurs valeurs sont présentes à la même position d'index
# pour fromer une liste liée.
# Dans les ensemble CPython sont implémentés à l'aide d'un dictionnaire
# avec des variables factices où la lcé est l'ensemble des membres
# avec de plus grandes optimisations de complexité temporelle

Set = set([1, 2, "Code", 4, "Magazine", 6, "Python"])
print(Set)
# accéder aux éléments
for i in Set:
    print(i, end=" ")
print()
# vérifier qu'un élément se trouve bien dans l'ensemble
print("Coding" in Set)
