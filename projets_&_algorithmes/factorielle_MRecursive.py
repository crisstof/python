# factorielle d'un nombre
# !6 = 6*5*4*3*2*1=720
def factorielle(n):
    return 1 if (n == 1 or n == 0) else n * factorielle(n - 1)


num = 6
print("La factorielle de", num, "est", factorielle(num))
