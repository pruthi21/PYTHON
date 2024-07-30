class Vehicle:
    def __init__(self, color, wheels):
        self._color = color
        self._wheels = wheels

class Car(Vehicle):
    def __init__(self, color, wheels, doors):
        super().__init__(color, wheels)
        self._doors = doors

    def car_detail(self):
        print(f'Color of Car {self._color}, No. of Wheel {self._wheels}, No. of door {self._doors}')

# Creating objects and using methods
car = Car("red", 4, 4)
car.car_detail()  # Specific to Car

print()

# Accessing protected variable using object
print('Before changing protected variable of wheel:',car._wheels)
car._wheels=10         # Modifying protected value
print('After changing protected variable of wheel:',car._wheels)

print('Number of cars door',car._doors)





class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.__speed = 0  # Private attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        # Add any validation or logic here if needed
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        # Add any validation or logic here if needed
        self.__model = model

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        # Add any validation or logic here if needed
        if speed>15:
            self.__speed = 50


# Creating an instance of the Car class
my_car = Car(make="Toyota", model="Camry")

# Accessing and modifying attributes using setter and getter methods
print("Make:", my_car.get_make())
my_car.set_make("Honda")  # Modifying make using setter
print("Updated Make:", my_car.get_make())

print()

print("Model:", my_car.get_model())
my_car.set_model("Accord")  # Modifying model using setter
print("Updated Model:", my_car.get_model())

print()

print("Speed:", my_car.get_speed())
my_car.set_speed(20)  # Modifying speed using setter
print("Updated Speed:", my_car.get_speed())