class Animal:
    """This is the parent class named Animal. This serves as the blueprint for the child classes (Lion, Elephant, and Monkey). Its data field is the name, meanwhile its methods are eat() and make_sound()."""
    def __init__(self, name:str):
        self._name = name

    def eat(self):
        print(f"{self._name} is eating.")

    def make_sound(self):
        print(f"{self._name} makes a sound.")

class Lion(Animal):
    """This is the Lion child class of the Animal class. It overrides both the parent's class' methods eat() and make_sound(). """
    def make_sound(self):
       print(f"{self._name} roars loudly!")
    
    def eat(self):
        print(f"{self._name} eats fresh meat.")

class Elephant(Animal):
    """This is the Elephant child class of the Animal class. It overrides both the parent's class' methods eat() and make_sound(). """
    def make_sound(self):
        print(f"{self._name} trumpets!")

    def eat(self):
        print(f"{self._name} eats grass and fruits.")

class Monkey(Animal):
    """This is the Monkey child class of the Animal class. It overrides both the parent's class' methods eat() and make_sound(). """
    def make_sound(self):
        print(f"{self._name} chatters!")

    def eat(self):
        print(f"{self._name} eats bananas.")

# Instantiates the child classes of the Animal class
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey ("George")

# Calls the methods of the child classes using for loops by using a list then unpacking it (it explicitly said in the instructions to use it, but the sample input doesn't use it.)animals = [lion, elephant, monkey]
animals = [lion, elephant, monkey]
for oneanimal in animals:
  oneanimal.make_sound()
  oneanimal.eat()
  print("-----")