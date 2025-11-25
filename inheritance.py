import typing


class Animal:
    def speak(self):
        return "Animal sound"
    
    def calculate_age(self):
        return 0


class Dog(Animal):
    def speak(self):
        return "Woof!"


print(Dog().speak())


# Duck typing
def make_animal_sound(animal:Animal):
    print(animal.speak())

make_animal_sound(Dog())