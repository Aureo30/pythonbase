# on demande l'age de la personne
age = int(input("Quel est votre age ? "))
# on vérifie si la personne à moins de 18 ans dans ce cs le prix est de base à 7€
if age <= 18:
    pop_corn_request = 0
    price_total = 5
    # on demande si la personne veux du pop corn
    pop = input("Voulez vous du pop-corn ? ")
    # si la personne répond oui on lui ajoute 5€
    if pop == "oui":
        price_total += 5
        #on affiche le prix final
        print("ça vous fera {}€ ".format(price_total))
    else:
        print("d'accord ça fera", price_total, "€")
        # sinon si l'âge est en dessous de 18
elif age >= 18:
    print("D'accord cela vous fera 5 euros ")
else: 
        print("D'accord cela vous fera 12 euros ")
        prix_total = 12
        pop_corn_request_deux = 0
        pop_corn_deux = input("Voulez vous du pop-corn ? ")
if pop_corn_request == "oui":
    prix_total += 5
    print(prix_total)