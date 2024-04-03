import pygame
import time

def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    time.sleep(2)  # Добавляем задержку в 5 секунд
    pygame.mixer.music.stop()


class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, species, age, feather_color):
        super().__init__(name, species, age)
        self.feather_color = feather_color

    def make_sound(self):
        print(f"{self.name} кричит- УУ УУУУУУ")


    # def main():
    #     print("Сова кричит УУ УУУ")
    #     play_sound('sound/owl.mp3')
    #
    # if __name__ == "__main__":
    #     main()

    def eat(self):
        print(f"{self.name} питется мелкими грызунами")

    def describe(self, keeper, vet):
        print(f"Птица {self.name} - Вид: {self.species}, Возраст: {self.age}, Цвет перьев: {self.feather_color}")
        self.make_sound()
        self.eat()
        keeper.feed_animal(self)
        vet.heal_animal(self)

    def sound():
        print("Сова кричит УУ УУУ")
        play_sound('sound/owl.mp3')
    if __name__ == "__main__":
        sound()

class Mammal(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name,species, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Рычат, кричат")

    def eat(self):
        print("Питаются растениями или мясом")

class Reptile(Animal):
    def __init__(self, name, species, age, scale_color):
        super().__init__(name, species, age)
        self.scale_color = scale_color

    def make_sound(self):
        print("Шипят")

    def eat(self):
        print("Рептилии питаются мелкими животными")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

class ZooKeeper:
    def feed_animal(self, animal):
        print(animal.name, ":кормит сотрудник зоопарка", )

class Veterinarian:
    def heal_animal(self, animal):
        print(animal.name, ":осматривает и лечит ветеринар", )

# Пример использования классов
owl = Bird("Сова", "Филин", "10 лет", "желтовато-коричневый")
zoo = Zoo()
zookeeper = ZooKeeper()
vet = Veterinarian()

zoo.add_animal(owl)

# Выведем все данные о сове сразу
owl.describe(zookeeper, vet)
