
import random
text = input("Entrer une chaine de charactère sous la forme mot1/mot2/mot3/mot4/mot5 ").split("/")
random.shuffle(text)

print(text)
# variable qui récupère la quantité d'entrées dans la liste
nombreDentrees = len(text)

# si le nombre d'élements de cette liste est inferieur a 10 alors afficher les deux premiers mots, si le nombre est égal ou suppèrieur à 10 alors mettre les 3 derniers mots
if nombreDentrees < 10 :
    #affiche les 2 premieres entrées de la liste
    print("La phrase est : {}".format(text[:2]))
elif nombreDentrees >= 10:
    # affiche les 3 dernieres entrées de la liste
    print("La phrase est : {}".format(text[-3:]))