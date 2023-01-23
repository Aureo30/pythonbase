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
        # créé une méthode de type quetteur pour récup des infos
    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    # créé une méthode de type mutateur pour modifier des valeurs
    def attaque(self, damage):
            self.health -= damage
            print("Âie..vous venez de subir", damage, "dêgats !")
    def attack_player(self, target_player):
        target_player.damage(self.attack)

    
