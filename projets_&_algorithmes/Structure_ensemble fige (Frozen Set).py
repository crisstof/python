# Les ensembles figé en Python sont des objets immuables
# qui ne prennent en charge que les méthodes et opérateurs
# qui produisent un résultat sans affecter l'ensemble
# ou les ensembles figés auxquels ils sont appliqués
# Alors que les éléments d'un ensemble peuvent être modifiés
# à tout moment, les éléments de l'ensemble figé restent
# les mêmes après la création de l'ensemble figé

# cet ensemble est idetique à {"a", "b", "c"}
normal_set = set(["a", "b", "c"])
print("ensemble normal ")
print(normal_set)

# frozen set
frozen_set = frozenset(["e", "f", "g"])
print("ensemble figé")
print(frozen_set)
# la fonction ci-dessous provoquerait
# une erreur car nous essayons de modifier un ensemble figé
# frozen_set.add("h")
normal_set.add("Z")
print(normal_set)
