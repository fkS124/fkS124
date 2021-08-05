liste = [int(input("nombre")) for i in range(5)]

print("non triée :", liste)

def pos_neg(liste):
    for i in liste:
        if i < 0:
            del(liste[liste.index(i)])
            liste.insert(0, i)
        elif i > 0:
            del(liste[liste.index(i)])
            liste.insert(len(liste)-1, i)
    return liste
        
print("triée :", pos_neg(liste))
new_liste = pos_neg(liste)
new_liste.sort()

print("triée croissante:", new_liste)

def insertion(n, liste):
    liste.append(n)
    liste.sort()
    return liste

inserage = int(input("insert a number :"))
new_liste = insertion(inserage, new_liste)
print("liste triée:", new_liste)