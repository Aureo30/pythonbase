# créé une liste de pseudos pour simler un jeu en ligne
# ThePogo360, Yoshi, Ajin


online_players = ["ThePogo360", "Yoshi", "Ajin"]

print(online_players)

# en ajouter d'autres
# on imagine que un joueur "full pub mp" se connecte

online_players.append("full pub mp")

# on imagine cette fois que plusieyurs joueurs se connecte

online_players.extend(["best joueur", "titouandu69", "lavictime"])
# on imagine cette fois que Thepogo360 se déconecte
del online_players [0]

# modifier "Yoshi" -> l'escargot_de_mer

online_players[1] = "l'escargot_de_mer"
# modifier l'éescargot_de_mer en Leconquiperttjrsesmdp et modifier "ajin" en "test"
online_players[1:2] = ["Leconquiperttjrsesmdp", "TEST"]

# on veut ban "TEST" pour des raid
online_players.remove("TEST")
# la partie c'est fini
finish = input("la partie c'est fini voulez vous rejouer ? ")
if finish == "oui":
    print("d'accord")
elif finish == "non":
    print("d'accord au revoir ")
    online_players.clear()
else:
    print("il y à une erreur ! ")
    online_players.clear()
