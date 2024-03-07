# Pakuri class
class Pakuri:
    # Class variables
    attack = 0
    defense = 0
    speed = 0
    # Constructor for Pakuri Class
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13
    # Returns the species(String)
    def get_species(self):
        return self.species
    # Returns the attack of the Pakuri instance
    def get_attack(self):
        return self.attack
    # Returns the defense of the Pakuri instance
    def get_defense(self):
        return self.defense
    # Returns the speed of the Pakuri instance
    def get_speed(self):
        return self.speed
    # Sets the attack variable of an instance with argument passed in function
    def set_attack(self, new_attack):
        self.attack = new_attack
    # Evolves the stats of a Pakuri Object
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3