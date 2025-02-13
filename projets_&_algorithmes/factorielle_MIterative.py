# factorielle d'un nombre
# !6 = 6*5*4*3*2*1=720
def factorielle(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
    return fact


num = 6
print("La factorielle de", num, "est", factorielle(num))
