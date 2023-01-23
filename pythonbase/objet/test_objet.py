import random

# créé un objet player
class Player:
    # défini une fonction __init__ qui est la première fonction utilisé dans un objet, et défini le paramètre self et tous les autres qui permet d'avoir une sorte de bdd pour chaque utilisateur
    def __init__(self, pseudo, health, attack):
        # défini les attributs en fonction des paramètres
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        # créé un message récupéré sois a partir du self.[le_parametre] ou directement avec le paramètre en question
        print("Bienvenue au joueur", self.pseudo, "/ points de vies", self.health, "/ points d'attaques", self.attack)

    def attaque(self, player):
        player.health -= random.randint(1,2)*self.attack
        self.attack += 1

# créé deux intents d'objet avec deux joueurs pour appeler plus tard l'objet
player1 = Player("Joueur1", 20, 3)
player2 = Player("Joueur2", 20, 3)

print(player1.attack, player2.health)

player1.attaque(player2)

print(player1.attack, player2.health)