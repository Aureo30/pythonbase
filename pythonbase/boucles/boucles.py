
# lister les emails

# blackslist
blacklist = ["test@gmail.com"]

emails = ["test@gmail.com", "test2@gmail.com", "test3@gmail.com"]
# pour chacune des valeur j'affiche "email envoyé à :"
for emails in emails:
    if emails in blacklist:
        print("L'email {} est blacklisté ! envoi impossible".format(emails))
        continue
    print("Email envoyé à : ", emails)