# En tant que pile, la file d'attente est une structure
# de données linéaire de manière (FIFO), avec une file d'attente
# l'élément ajouté le mmoins  récemment est supprimé en premier
# opérations:
# Enqueue: ajouté un élément à l file d'attente
# si la file est pleine il y a une condition de débordement.
# Dequeue: supprime un élément. Les éléments sont sautés dans
# le même ordre dans lequel ils sont poussés.
# si elle est vide es une condition de sous dépassement
# Front: obtenir l'élément avant de la file
# Rear: obteir le dernier éément
# initialisation
queue = []
# ajout
queue.append("g")
queue.append("f")
queue.append("e")

print("File attente initiale")
print(queue)

print("\nélément retiré de la file d'attente")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)
