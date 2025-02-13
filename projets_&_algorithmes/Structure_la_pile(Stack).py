# une pile est une structure de données linéaire
# qui stocke les éléments de manière
# Last-In/First-Out (LIFO) ou first-in / Last  out (FILO)
# dans une pile assiette les opérations sont push/pop
# les fonction associézs à stack
# empty() retourne si l pile est vide
# size() retourne la taille de la pile
# top() retourne le sommet de la pile
# push(a) ajoute un élément a au sommet de la pile
# pop() supprime l'élément du sommet de la pile
stack = []
stack.append("g")
stack.append("f")
stack.append("e")

print("pile initiale")
print(stack)

print("\nélément retiré de la pile")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
