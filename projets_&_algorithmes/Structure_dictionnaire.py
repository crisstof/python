# Le dictionnaire est une collection ordonnées de données
# qui stocke les données au format clé/valeur
# cpùùe mes tables de hashage avec complexité temporelle o(1)
# la clés est immuable
Dict = {"Nom": "John", 1: [1, 2, 3, 4]}
print(Dict)
print(Dict["Nom"])
print(Dict.get(1))
# affcihe avec une fonction de comprehension du dictionnaire
myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)
