def somme_armstrong(n):
    n = str(n)
    somme = 0
    for i in n:
        somme += int(i)**3
    if somme == int(n):
        return True
    else:
        return False
    
n = int(input("n="))
for i in range(1, n+1):
    if somme_armstrong(i):
        print(i)