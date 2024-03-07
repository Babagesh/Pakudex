# Import Pakuri class
from pakuri import Pakuri

# Pakudex Class
class Pakudex:
    # List with all the Pakuri objects in it
    species_list = []
    # Constructor for Pakudex class
    def __init__(self, capacity=20):
        self.capacity = capacity
    # Return size of species_list
    def get_size(self):
        return len(self.species_list)
    # Get maximum capacity of list from instance variable
    def get_capacity(self):
        return self.capacity
    # Returns a type string array of species names if array has objects in it
    def get_species_array(self):
        species_names = []
        if len(self.species_list) == 0:
            return None
        else:
            for specie in self.species_list:
                species_names.append(specie.get_species())
            return species_names
    # Gets the stats of the specific specie in the species_list
    def get_stats(self, species):
        stats = []
        found = False
        for specie in self.species_list:
            if specie.get_species() == species:
                found = True
                temp = specie
        if found:
            stats.append(temp.get_attack())
            stats.append(temp.get_defense())
            stats.append(temp.get_speed())
            return stats
        else:
            return None
    # Sorts the species_list by Lexicographical ordering
    def sort_pakuri(self):
        species_names = []
        for specie in self.species_list:
            species_names.append(specie.get_species())
        species_names.sort()
        temp = []
        for i in range(len(species_names)):
            for j in range(len(self.species_list)):
                if self.species_list[j].get_species() == species_names[i]:
                    temp.append(self.species_list[j])
        for i in range(len(temp)):
            self.species_list[i] = temp[i]

    # Adds a pakuri object to list if it doesn't exist already
    def add_pakuri(self, species):
        for specie in self.species_list:
            if specie.get_species() == species:
                return False
        pakuri = Pakuri(species)
        self.species_list.append(pakuri)
        return True
    # Evolves an existing pakuri object in species_list
    def evolve_species(self, species):
        for specie in self.species_list:
            if specie.get_species() == species:
                specie.evolve()
                return True
        return False