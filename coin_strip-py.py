from random import randint

def creer_bande(taille, nb_pieces):
    t = [0]*taille
    deb = 1
    fin = taille - nb_pieces
    for _ in range(nb_pieces):
        i = randint(deb, fin)
        t[i] = 1
        deb = i+1
        fin = fin + 1
    return t

def est_valide(bande, saisie):
    # True si le coup est jouable
    try:
        index = int(saisie)
    except:
        print("La saisie doit être un nombre entier.")
        return False
    if 0<=index<len(bande):
        if bande[index]==0:
            if 1 in bande[index+1:]:
                return True
            else:
                print("Il n'y a pas de pièce à droite.")
        else:
            print("Il y a déjà une pièce ici.")
    else:
        print("Le numéro saisi est en dehors de la bande.")
    return False

def jouer(bande, saisie):
    # modifie la bande
    index = int(saisie)
    bande[index] = 1
    i = index + 1
    while bande[i]==0:
        i = i+1
    bande[i] = 0

def partie_finie(bande):
    # True si aucun coup jouable
    pass
    
bande = creer_bande(10, 3)
fini = False
while not fini:
    print(bande)
    saisie = input("Que jouez-vous ? ")
    if est_valide(bande, saisie):
        jouer(bande, saisie)
    fini = partie_finie(bande)

print("Fini !")


    
