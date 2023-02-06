# ------------- je me suis inspirer de google et j'ai quasiment tout modifié le code pour l'adapter a la consigne et le comprendre ---------------- #

import hashlib

boucle = True

while boucle==True:

    mdp = input ("Veuillez entrez un mot de passe : " )

    if not len(mdp) > 8 :
        print ("Votre mot de Passe est trop court ! " )
    #pour que le mot de passe a au moins 8 caractère 
    

    if sum(1 for x in mdp if x.isalpha()) :
        alpha_present = True
    else:
        print ("Il vous manque une miniscule ")
        
    if sum(1 for x in mdp if x.isupper()) :
        maj_presente = True
    else:
        print ("Il vous manque une majuscule ")
    
    if sum(1 for x in mdp if x.isdigit()) :
        digit_present = True
    else:
        print ("Il vous manque un chiffre ")

    if sum(1 for x in mdp if x.isdecimal()) :
        punctuation_present = True
    else:
        print ("Il vous manque un caractère spécial ") 
    #boucle qui vérifie que toutes les conditions sont remplies
    #la fonction sum sert a ajoutez la valeur de départ à la suivante 

    if len(mdp) > 8 and alpha_present == True and maj_presente == True and digit_present == True and punctuation_present == True:
        y = hashlib.sha256 (mdp.encode('utf-8')).hexdigest()
        print ("Bravo ! Voici votre mot de passe crypté : ", y)
        #crypter le mot de passe avec Hashlibz
        break   

