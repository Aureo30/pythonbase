from objet import Player
from objet import weapon

knife = weapon("Couteau", 4)
# créé deux fonction avec deux joueurs pour appeler plus tard l'objet
player1 = Player("Joueur1", 20, 3)
player2 = Player("Joueur2", 20, 3)

player1.attack_player(player2)
print(player1.get_pseudo(), "à attaqué ", player2.get_pseudo()) 
