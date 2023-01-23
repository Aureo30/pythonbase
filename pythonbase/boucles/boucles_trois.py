# "Mazako, 80 abonnés"
subscribers_count = 80

# il gagne 10% de son audiance chaque mois
months = 0
# on souhaite estimer combien il aura d'abonné(e)s dans 2 ans(24 mois)
while months <= 24:
    # augmenter l'audiance
    subscribers_count *= 1.10

    # afficher le nombre d'abonné(e)s 
    print("Vous avez actuellement {} abonné(e)s".format(subscribers_count))
    # on passe au moins suivant

    months += 1