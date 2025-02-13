# ByteArray en python donne une séquence modifiable
# d'entier dzns l plage 0<=x<256

# création d'un bytearray
a = bytearray((12, 8, 25, 2))
print("Création du byteArray")
print(a)

print("**acces aux éléments**")
print("Affichage des élément:", a[1])

print("\nmodification des éléments ")
a[1] = 3
print(a)
print("\najout d'éléments x02")
a.append(30)
print(a)
