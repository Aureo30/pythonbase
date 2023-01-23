
text = input("Entrer une chaine de la forme (email-pseudo-motdepasse) ").split("-")
print(text)

print("Salut {}, ton email {}, ton mot de passe {}".format(text[1], text[0], text[2]))