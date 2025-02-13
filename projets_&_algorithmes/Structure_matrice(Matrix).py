# Une matrice est un tableau en deux dimensions
# ou chaque élément a strictement la même taille
# pour créer une matrice nous utiliserons le paquet numpy
import numpy as np

a = np.array([[1, 2, 3, 4], [4, 55, 1, 2], [8, 3, 20, 19], [11, 2, 22, 21]])
m = np.reshape(a, (4, 4))
print(m)
# affiche les éléments
print("Affiche les éléments")
print(a[1])
print(a[2][0])

print("ajouter un élément dans la matrice")
m = np.append(m, [[1, 15, 13, 11]], 0)
print(m)

print("suppression element")
m = np.delete(m, [1], 0)
print(m)
