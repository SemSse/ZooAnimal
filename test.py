class Reptile:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_habitat(self):
        return self.habitat

# Пример использования класса
snake = Reptile("Python", "Ball Python", "Tropical forests")
print("Name:", snake.get_name())
print("Species:", snake.get_species())
print("Habitat:", snake.get_habitat())