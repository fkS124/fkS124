def somme_diviseurs(n):
    somme = 0
    for i in range(1, n+1):
        if i != n and n%i==0:
            somme+=i
    return somme

n1 = int(input("n1="))
amicaux = []

for i in range(1, 2001):
    if somme_diviseurs(i) == n1 and somme_diviseurs(n1) == i:
        amicaux.append(i)
        
print(f"{n1} est amical avec : {amicaux}")
    