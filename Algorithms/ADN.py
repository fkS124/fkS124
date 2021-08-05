def presence_A(seq):
    if "A" in str(seq):
        return True
    return False

def position_de_AT(seq):
    if "AT" in seq:
        return seq.index("AT")
    return None

def position(code,seq):
    if code in seq:
        return seq.index(code)
    return -1 # <- pour des raisons de facilités de comparaison, None est remplacé par -1

def find_murderer():
    moutarde = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    rose = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
    pervanche = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
    leblanc = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"
    
    murderers = ["moutarde", "rose", "pervanche", "leblanc"]
    murderers_adn = [moutarde, rose, pervanche, leblanc]
    
    first_code = "CATA"
    second_code = "ATGC"
    
    presence = []
    
    
    for i in murderers_adn:
        presence.append(position(first_code, i))

    # le coupable 1 est celui dont l'index le plus grand a été trouvé
    murderer1 = murderers[presence.index(max(presence))]
    
    # met à jour les listes (supprime la coupable 1 des deux listes et vide la liste de présence)
    del(murderers[presence.index(max(presence))])
    del(murderers_adn[presence.index(max(presence))])
    presence = []
    
    
    for i in murderers_adn:
        presence.append(position(second_code, i))

    murderer2 = murderers[presence.index(max(presence))]
    
    return murderer1, murderer2
    
    