import hashlib
import re

boucle = True

while boucle:

    mdp = input ("Veuillez entrez un mot de passe (contenant minimum une majuscule, une minuscule, un chiffre et un caractère spécial ): " )

    if not len(mdp) > 8 :
        print ("Votre mot de Passe est trop court ! " )
    #pour que le mot de passe à au moins 8 caractère 
    

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

    if re.search("[!;/.@#$%^&*]", mdp): 
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
    else:
        print ("Le mot de passe renseigner n'est pas valide .")