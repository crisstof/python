# Le module heapq en python fournit la structure de données
# heap qui représente une file d'attente prioritaire
# la propriété elle donne toujours le plus petit élément
# (min heap) chaque fois que l'élémen est dépilé
# heap[0] renvoie le plus petit élément )à chaque fois
# il prend en charge l'extraction et l'insertion du plus petit élément
# Les heap sont de deux types:
# Max-Heap: la clé presente au noeud racine est la plus grande
# parmi les clés présentes sur tous les enfants
# la même propriété doit être récursivement vraie pour
# tous les sous-arbres de cet arbre binaire
# Min-Heap: la clé presente au noeud racine doit être au minimum
# parmi les clés présentes sur tous les enfants
# la même propriété doit être récursivement vraie pour
# tous les sous-arbres de cet arbre binaire
import heapq

li = [5, 7, 9, 1, 3]

# convertir la liste en heap
heapq.heapify(li)
print(list(li))
# ajout
heapq.heappush(li, 4)
print(list(li))

# extraire le plus petit nombre
heapop = heapq.heappop(li)
print(heapop)
print(list(li))
