import random 
# créé une fonction avec les infos du joueur
def players_infos():
    # créé des listes pour les pseudos, les ages et les emails
    pseudo = ["Harry Potter", "DarkCreep", "Downhill13", "Yama", "Alexy", "Azur","minigaming", "Qomentry", "Mouxy", "Lurik", "AzurJust" , "DoctorDramaAnge", "lLikeLikeKinder", "SonRoiSadSad", "QueenEHumanSummer" , "TomatoToutOnlySon"]
    age = [11, 23, 14, 25, 35, 12, 23, 16, 20, 25, 8, 10, 13, 12, 11, 15]
    emails = ["email1@gmail.com", "email2@gmail.com", "email3@gmail.com", "email4@gmail.com", "email5@gmail.com"]
    # bannir email 1 pour cheat
    emails.remove("email1@gmail.com")
    # melanger les listes pseudos, age, emails 
    random.shuffle(pseudo)
    random.shuffle(age)
    random.shuffle(emails)
    # choisir un élément de chacune des listes au hasard
    pseudo_choisi = random.choice(pseudo)
    age_choisi = random.choice(age)
    emails_choisi = random.choice(emails)
    # afficher dans la console toutes les listes
    print("Votre pseudo est : ", pseudo_choisi, "Vous avez", age_choisi, "ans ", "Votre email est : ", emails_choisi)

# éxécuter la fonction
players_infos()