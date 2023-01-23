import random
import itertools #importe le module pour les combinaisons

# créé une liste de pseudo d'utilisateur
pseudo_liste = ["Harry Potter", "DarkCreep", "Downhill13", "Yama", "Alexy", "Azur","minigaming", "Qomentry", "Mouxy", "Lurik", "AzurJust" , "DoctorDramaAnge", "lLikeLikeKinder", "SonRoiSadSad", "QueenEHumanSummer" , "TomatoToutOnlySon"]
random.shuffle(pseudo_liste)
#print("Le pseudo est : {}".format(pseudo_liste[:1]))
#print (" , " .join(pseudo_liste))   le join permet de retirer les crochets affichés
# code permettant de générer toutes les combinaisons possibles avec des nombres donnés (n) et une quantité précise (ici, 4)
n = "0123456789"
combinaisons = ["".join(i) for i in itertools.permutations(n, 4)]
# print(combinaisons)
# choisis une combinaison au hasard :
combinaisonChoisie = random.choice(combinaisons)

print("Votre pseudo est : {}#{}".format(" ".join(pseudo_liste[:1]), combinaisonChoisie))