class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Vehicle: {self.brand}")

    def vehicle(self):
        print(' This is a vehicle class constructor')
class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)      # Calling the constructor base class vehicle (parent class - Vehicle)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()        # Call the display_info method of the base class (parent class - Vehicle)
        print(f"Doors: {self.num_doors}")

    def car(self):
        print(' This is a car class constructor')
class SportsCar(Car):
    def __init__(self, brand, num_doors, top_speed):
        super().__init__(brand, num_doors) # Calling the constructor of the immediate base class i.e (child class -Car)
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()  #Calling the constructor of the immediate base class i.e (child class -Car)
        print(f"Top Speed: {self.top_speed} kph")

    def sportscar(self):
        print(' This is a sports car class constructor')
sports_car = SportsCar(brand="McLaren", num_doors=2, top_speed=350)

sports_car.display_info()

# Accessing sportscar method
sports_car.sportscar()

# Accessing car method through Grand Child class (sportscar)
sports_car.car()

# Accessing vehicle method through Grand Child class (sportscar)
sports_car.car()