# Une liste chainée est une structure de données linéaire
# dans laquelle les élément ne sont stockés à des emplacement
# de mémoire contigus.
# Les éléments d'une listes chainéesont désignés à l'aide de pointeurs
# Une liste chainée est représentée par un pointeur vers le premier noeud
# de la liste chainée
# le premier noeud est appelé head (tête)
# Si la liste chainée est vide alors la valeur de la tête est null
# chaque noeud d'une liste se compose d'au moins deux parties:
# Données
# Pointeur (ou référence) vers le noeud suivant
# Exemple
class Node:
    # fonction pour initialiser l'objet node
    def __init__(self, data):
        self.data = data  # affecte les données
        self.next = None  # initialise next en tant que null


# class liste chainée
class LinkedList:
    # fonction pour initialiser l'objet chainée de la classe LinkedList
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# créons une simple liste chainée avec 3 noeuds


# L'exécution du code commence ici
if __name__ == "__main__":
    # créer une liste chainée vide
    llist = LinkedList()
    # affecter les noeuds
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    # Trois noeuds ont été créée, pour l'heure sans aucun lien
    # Nouas avons des références à ces trois blocs en tant que head
    # pour le premier ensuite le deuxième et le troisième
    llist.head.next = second
    second.next = third  # relie le deuxième noeud au troisième noeud
    llist.printList()
