class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog('Scooby', 20)
cat = Cat('Jerry', 30)
print(dog.age)
cat.eat()