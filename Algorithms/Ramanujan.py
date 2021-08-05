from math import sqrt

def factorielle(k):
    fact = 1
    for i in range(1, k+1):
        fact *= i
    return fact

def ramanujan(n_terme):
    somme = 0
    ramanujan_ = 1
    multi = ((2*sqrt(2))/9801)
    for i in range(1, n_terme + 1):
        somme += (factorielle(4)*(1103+26390*i))/(factorielle(i)**4*396**(4*i))
    ramanujan_ = multi * somme
    return ramanujan_


