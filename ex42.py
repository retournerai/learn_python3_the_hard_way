## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self, name, friends):
        self.name = name        
        self.friends = []
            
# Dog is-a animal
class Dog(Animal):

        

    def __init__(self, name, friends, rase):
        # a class Dog has-a init that takes self, and name params.
        self.name = name
        self.rase = rase
        
        self.
            
    def test():
        print("test")
                
        print(friend[1])
        
## a class Cat is-a 'Animal' and have a class relationship with the class Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a init that takes self, and name params.
        self.name = name
        
## a class Person has-a pet
class Person(object):

    def __init__(self, name, pet, age):
       ## Person has-a init that takes self and name params.
       self.name = name
       
       ## Person has-a pet of some kind
       self.pet = pet
       self.age = age
       
## class Employee is-a 'Person' and have a class relationship with the class Person
class Employee(Person):

    def __init__(self, name, pet, age, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name, pet, age)
        ## Employee has-a salary of some kind
        self.salary = salary
        
## a Fish has-a color
class Fish(object):
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
## a empty class Salmon with "fish" as an object
class Salmon(Fish):
    
    def __init__(self, name, dish, wine):
        self.name = name
        self.dish = dish
        self.wine = wine
    
## Halibut is-a Fish and have a class relationship with the class Fish
class Halibut(Fish):
    
    def __init__(self, name, water):
        self.name = name
        self.water = water
    
    
## rover is-a Dog
rover = Dog("Rover", "Dalmo")
# Rover got 3 friends
rover.friends = Andre, Piet, Joke

## satan is-a Cat
satan = Cat("Satan")

## mary is a Person of 36 years old
mary = Person("Marry", "bird", "36")

## Mary has-a pet called Satan
mary.pet = satan

## Frank is-a Employee called Frank making 120000
frank = Employee ("Frank", "Rover", "36", 120000)

## Frank has-a pet called rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish("Harry", "Green")

## crouse is-a Salmon
crouse = Salmon("John", "Diner", "White wine")

## harry is-a Halibut
harry = Halibut("Harry", "sweet-water")    
harry = Salmon ("Harry", "Entry", "Red Wine")    

Dog.test()
print("Rover talk to friends" )
