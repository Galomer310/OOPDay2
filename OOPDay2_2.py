
from OOPDay2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *other_dogs):
        all_dogs = [self.name] + [dog.name for dog in other_dogs]
        print(f"{', '.join(all_dogs)} all play together!")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")

new_dog = PetDog("Boxer", 4, 23)
new_dog.train()
new_dog.play(Dog("Rexi", 3, 18), Dog("Luna", 5, 30))
new_dog.do_a_trick()
