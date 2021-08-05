# base de donnée temporaire contenant les matrice que l'utilisateur a rentré pendant que le programme est en
# cours d'execution
all_matrices = []
choice = ""


def input_matrice():

    """Fonction pour permettre à l'utilisateur de rentrer ses propres matrices dans la base de donnée temporaire
    de manière pratique, rapide et intuitive.

    Pour rentrer une matrice dans la base de donnée temporaire :

    - Choisir le nombre de dimensions
    - Choisir le nombre de termes par dimensions
    - Entrez chaque ligne de matrice une à une de la forme :
    Pour une matrice de 3 dimensions et 3 termes tel que :
    [1    0   2]
    [25  68  96]
    [2   6   98]

    Tapez comme suivant :
        # affichage console
        1 0 2
        # affichage console
        25 68 96
        # affichage console
        2 6 98
    """

    global all_matrices
    
    new_matrice = []

    n_dimension = int(input("Dimension(s):"))
    n_termes = int(input("Nombre de termes(s):"))

    print("Entrez chaque terme de la ligne espacé d'un espace.")
    print("Ex: '1 0 2 3' donnera la liste [1, 0, 2, 3], entrez 'exit' à la place de cette ligne pour sortir de l'input.")
    
    for i in range(n_dimension):
        print(f"Ligne numéro {i}")

        chaine = str(input())
        # sépare la chaine de caractère obtenue chaque espace
        print(chaine.split(" "))

        if chaine == "exit":
            print("Arrêt forcé du protocol. Retour au menu.")
            return 0

        # pour force l'utilisateur à rentrer des valeurs cohérente avec ses choix précédents, on fait une boucle while
        # avec pour condition l'invalidité de la chaine de caractère
        while len(chaine.split(" ")) != n_termes:
            print("Taille de ligne inaqéquate, veuillez réessayer ou entrer 'exit' pour sortir.")
            chaine = str(input())
            if chaine == "exit":
                print("Arrêt forcé du protocol. Retour au menu.")
                return 0

        # enregistre la ligne dans la nouvelle matrice
        new_matrice.append(chaine.split(" "))

        # transforme les caractères en entier dans toute la matrice
        for z in range(n_termes):
            try:
                new_matrice[i][z] = int(new_matrice[i][z])
            except ValueError:
                new_matrice[i][z] = eval(new_matrice[i][z])
            except Exception as e:
                print(e)
                print("Erreur, recommencement du protocol.\n")
                input_matrice()

    # rentre la nouvelle matrice dans la base de donnée temporaire
    all_matrices.append(new_matrice)


def add(matrix1, matrix2):

    """Affiche l'addition de deux matrices choisies par l'utilisateur."""
    
    new_matrice = []
    
    if len(all_matrices[matrix1]) != len(all_matrices[matrix2]) or len(all_matrices[matrix1][0]) != len(all_matrices[matrix2][0]):
        print("Les matrices sont dans dimensions différentes, l'addition est impossible.")
        return 

    # ajoute les termes de la matrice ayant le meme index et met le resultat dans la nouvelle matrice
    for i in range(len(all_matrices[matrix1])):
        intermediate_list = []
        for z in range(len(all_matrices[matrix1][i])):
            intermediate_list.append(int(all_matrices[matrix1][i][z] + all_matrices[matrix2][i][z]))
        new_matrice.append(intermediate_list)
    
    print(f"Le résultat de l'addition de la matrice n°{matrix1} et de la matrice n°{matrix2} est :")
    for w in range(len(new_matrice)):
        print(new_matrice[w])


def substract(matrix1, matrix2):

    """Affiche la soustraction de deux matrices choisie par l'utilisateur."""

    new_matrice = []

    if len(all_matrices[matrix1]) != len(all_matrices[matrix2]) or len(all_matrices[matrix1][0]) != len(all_matrices[matrix2][0]):
        print("Les matrices sont dans dimensions différentes, l'addition est impossible.")
        return

    # soustrait les termes de la matrice ayant le meme index et met le resultat dans la nouvelle matrice
    for i in range(len(all_matrices[matrix1])):
        intermediate_list = []
        for z in range(len(all_matrices[matrix1][i])):
            intermediate_list.append(int(all_matrices[matrix1][i][z] - all_matrices[matrix2][i][z]))
        new_matrice.append(intermediate_list)

    print(f"Le résultat de la soustraction de la matrice n°{matrix1} et de la matrice n°{matrix2} est :")
    for w in range(len(new_matrice)):
        print(new_matrice[w])
        

def product(m1, m2):

    """Fonction qui affiche le résultat d'un produit de deux matrices."""
    
    if len(all_matrices[m1]) != len (all_matrices[m2][0]) or len(all_matrices[m2]) != len (all_matrices[m1][0]):
        print("Les matrices sont incompatibles")
        return
    
    new_matrice = [[] for i in range(len(all_matrices[m1]))]

    m1_rows = []
    m2_column = [[] for i in range(len(all_matrices[m2][0]))]

    # récupère les lignes de la matrice 1
    for r in range(len(all_matrices[m1])):
        m1_rows.append(all_matrices[m1][r])

    # récupère les colonnes de la matrice 2
    for row in range(len(all_matrices[m2])):
        for col in range(len(all_matrices[m2][row])):
            m2_column[col].append(all_matrices[m2][row][col])

    # effectue l'opération une fois que les colonnes et les lignes sont listées
    for a in range(len(m1_rows)):
        for z in range(len(m2_column)):
            actual_number = 0
            for b in range(len(m1_rows[a])):
                actual_number += (m1_rows[a][b] * m2_column[z][b])
            new_matrice[a].append(actual_number)

    # affiche le résultat
    print(f"Le résultat du produit de la matrice n°{m1} et de la matrice n°{m2} est :")
    for i in new_matrice:
        print(i)


def transposition(m):
    # on transpose la matrice donnée en argument
    return list(map(list,zip(*m)))


def smaller_matrice(m, i, j):
    # on rends une matrice plus petite pour appliquer la formule correctement
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def det_matrice(m):
    # si la matrice est de 2x2, le cas est plus simple :
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    # on applique une formule
    for c in range(len(m)):
        determinant += ((-1)**c) * m[0][c] * det_matrice(smaller_matrice(m, 0, c))
    return determinant


def inverse(index_matrice):
    m = all_matrices[index_matrice]

    determinant = det_matrice(m)
    # si la matrice est en 2x2, le cas est plus simple :
    if len(m) == 2:
        result = [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
        print(f"La matrice n°{index_matrice} inversée est : ")
        for i in range(len(result)):
            print(result[i])
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    # trouve la matrice des cofacteurs
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = smaller_matrice(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * det_matrice(minor))
        cofactors.append(cofactorRow)
    # transpose la matrice des cofacteurs
    cofactors = transposition(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            try:
                cofactors[r][c] = cofactors[r][c]/determinant
            except ZeroDivisionError:  # evite une division par zero si le determinant est nul
                print("Cette matrice est ininversible.")
                return 0
    result = cofactors
    print(f"La matrice n°{index_matrice} inversée est : ")
    for i in range(len(result)):
        print(result[i])
    return cofactors


def show_matrixes():

    """Affiche d'une belle manière toutes les matrices contenues dans la base de donnée temporaire."""

    for i in range(len(all_matrices)):
        print(f"Matrice numéro {i} :")
        for z in range(len(all_matrices[i])):
            print(all_matrices[i][z])


def inverse_in_func(m):

    """Fonction retournant l'inverse d'une matrice inversible, sans afficher le résultat pour l'utiliser dans d'autres
    fonctions sans afficher les actions intermédiaires"""

    # trouve le determinant
    determinant = det_matrice(m)
    if determinant == 0:
        # on verifie si la matrice est inversible
        print("Determinant nul, matrice ininversible")
        return None
    # au cas c'est une matrice carrée de 2 dimensions, un cas plus simples est applicable :
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    # trouver la matrice des cofacteurs
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = smaller_matrice(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * det_matrice(minor))
        cofactors.append(cofactorRow)
    # transpose la matrice des cofacteurs
    cofactors = transposition(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            try:
                cofactors[r][c] = cofactors[r][c]/determinant
            except ZeroDivisionError:  # empeche une division par zero au cas ou le determinant est nul
                print("Division impossible.")
                return None
    return cofactors


def product_in_func(m1, m2):
    """Fonction qui retournes le produit de deux matrices, sans l'afficher pour l'utiliser dans d'autres fonctions
    sans afficher les actions intermédiaires."""

    if len(m1) != len(m2[0]) or len(m2) != len(m1[0]):
        print("Les matrices sont incompatibles")
        return None

    new_matrice = [[] for i in range(len(m1))]

    m1_rows = []
    m2_column = [[] for i in range(len(m2[0]))]

    for r in range(len(m1)):
        m1_rows.append(m1[r])

    for row in range(len(m2)):
        for col in range(len(m2[row])):
            m2_column[col].append(m2[row][col])

    for a in range(len(m1_rows)):
        for z in range(len(m2_column)):
            actual_number = 0
            for b in range(len(m1_rows[a])):
                actual_number += (m1_rows[a][b] * m2_column[z][b])
            new_matrice[a].append(actual_number)

    return new_matrice


def divide(m1, m2):

    matrice_inversee = inverse_in_func(all_matrices[m2])
    if matrice_inversee is None:
        print(f"La matrice n°{m2} est ininversible, la division est donc impossible.")
        return None
    result = product_in_func(all_matrices[m1], matrice_inversee)
    print(f"La division de la matrice n°{m1} par la matrice n°{m2} est :")
    for i in result:
        print(i)

    print("DISCLAIMER: L'INVERSION RETOURNE PARFOIS UNE VALEUR APPROCHEE, IL EST AINSI")
    print("POSSIBLE D'OBTENIR DES RESULTATS INCOHERENTS A CAUSE DE CES VALEURS.")
    print("Il ne s'agit que d'une limite imposée par le langage...")
    return None


def show_cmd():

    """Affiche toutes les commandes disponibles"""

    print("Bienvenue sur le gestionnaire de matrice.")
    print("Voici les commandes et les actions qui y sont liées :")

    print("""- 'input': entrez une matrice dans la base de donnée temporaire.
- 'show': montrez toutes les matrices présentes dans la base de donnée temporaire.
- 'addition': affiche l'addition de deux matrices présentes dans la base de donnée temporaire.
- 'substract': affiche la soustraction de deux matrices présentes dans la base de donnée temporaire.
- 'product': affiche le produit de deux matrices présentes dans la base de donnée temporaire.
- 'divide': affiche le quotient d'une matrice présente dans la base de donnée temporaire par une autre.
- 'det': affiche le determinant d'une matrice présente dans la base de donnée temporaire."
- 'exit': quitte l'application console.\n""")


while True:

    print("Entrez 'help' pour plus d'informations sur les commandes.")
    choice = str(input(">>> "))
    
    if choice == "input":
        input_matrice()
        show_matrixes()
    elif choice == "help":
        show_cmd()
    elif choice == "show":
        show_matrixes()
    elif choice == "addition":
        matrix1 = int(input("Index de matrice numéro 1 : "))
        matrix2 = int(input("Index de matrice numéro 2 : "))
        while matrix1 > len(all_matrices) or matrix1 < 0:
            matrix1 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 1 : "))
        while matrix2 > len(all_matrices) or matrix2 < 0:
            matrix2 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 2 : "))
        add(matrix1, matrix2)
    elif choice == "product":
        m1 = int(input("Index de matrice numéro 1 : "))
        m2 = int(input("Index de matrice numéro 2 : "))
        while m1 > len(all_matrices) or m1 < 0:
            m1 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 1 : "))
        while m2 > len(all_matrices) or m2 < 0:
            m2 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 2 : "))
        product(m1, m2)
    elif choice == "substract":
        matrix1 = int(input("Index de matrice numéro 1 : "))
        matrix2 = int(input("Index de matrice numéro 2 : "))
        while matrix1 > len(all_matrices) or matrix1 < 0:
            matrix1 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 1 : "))
        while matrix2 > len(all_matrices) or matrix2 < 0:
            matrix2 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 2 : "))
        substract(matrix1, matrix2)
    elif choice == "inverse":
        index_matrice = int(input("Index de matrice : "))
        while index_matrice > len(all_matrices) or index_matrice < 0:
            index_matrice = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice : "))
        inverse(index_matrice)
    elif choice == "divide":
        m1 = int(input("Index de matrice numéro 1 : "))
        m2 = int(input("Index de matrice numéro 2 : "))
        while m1 > len(all_matrices) or m1 < 0:
            m1 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 1 : "))
        while m2 > len(all_matrices) or m2 < 0:
            m2 = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice 2 : "))
        divide(m1, m2)
    elif choice == "det":
        m = int(input("Entrez l'index de la matrice : "))
        while m > len(all_matrices) or m < 0:
            m = int(input("Erreur dans l'index, veuillez entrer à nouveau l'index de la matrice : "))
        print(det_matrice(all_matrices[m]))
    elif choice == "exit":
        break
