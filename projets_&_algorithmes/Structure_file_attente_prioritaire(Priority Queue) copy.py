# Les files d'attentes prioritaires sont des structures
# abstraite où chaque donnée/valeur à une certaine priorité
# comme une compagnie aérienne chaque bagage affair, première classe ...
# un élément de haute priorité est retiré de la file d'attente avant
# un élément de basse priorité
# si 2 éléments on la même priorité il s sont servis selon
# l'ordre de la file d'attente


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join([str(i) for i in self.queue])

    # verifie si la file est vide
    def isEmpty(self):
        return len(self.queue) == 0

    # insère un élément dans la file
    def insert(self, data):
        self.queue.append(data)

    # extrait l'élément de la file en fonction de la priorité
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


if __name__ == "__main__":
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())
