class Dog:
    species = "canine"  # class attribute
    def __init__(self,name,breed,age):
        self.name = name # object attribute
        self.breed = breed
        self.age = age
        

    def eat(self): # self refrencing the object
        print(f"{self.name} is eating")

    def print_species(self): 
        print(f"{Dog.species}")


dog = Dog("scooby","pitbull",20)
print(f"{dog.name} bark loudly ")
dog.eat()
print(Dog.species)
dog.print_species()