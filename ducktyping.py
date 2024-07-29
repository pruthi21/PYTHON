'''The term "duck typing" comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." 
Duck typing means that the type or class of an object is determined by its behavior (methods and properties) rather than its explicit inheritance or type declarations.
Eg. int type can hold only integer values
'''


class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def make_sound(animal):
    return animal.speak()

# Instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# Calling the function with different objects
print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!
print(make_sound(duck))  # Output: Quack!