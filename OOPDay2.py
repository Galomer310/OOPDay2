# 🌟 Exercise 1 : Pets
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# cat_Bengal = Bengal("Bengaly cat", 3)
# cat_Chartreux = Chartreux("Chartreux cat", 4)
# cat_Siamese = Siamese("Siamese cat", 2)
#
#
# all_cats = [cat_Bengal, cat_Chartreux, cat_Siamese]
# sara_pets = Pets(all_cats)
# print(sara_pets.walk())





# 🌟 Exercise 2 : Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        running_speed = int(self.weight / self.age * 10)
        return running_speed

    def fight(self, other_dog):
        self_force = self.run_speed() * self.weight
        other_force = other_dog.run_speed() * other_dog.weight

        print(f"The force {self.name} got is {self_force}")
        print(f"The force {other_dog.name} got is {other_force}")

        if self_force > other_force:
            return f"{self.name} wins!"
        elif self_force < other_force:
            return f"{other_dog.name} wins!"
        else:
            return "It's a tie!"

first_dog = Dog("Rexi", 3, 18)
second_dog = Dog("Luna", 5, 30)

