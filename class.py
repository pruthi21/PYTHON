class   Car:
    def __init__(self,make,model,year):
        self.make =make
        self.model =model
        self.year = year

    def start(self):
        print(f'the {self.make}{self.model}{self.year}')
        
    def display_info(self):
        print(f'\nCar Infomation:\n'
                f'make:{self.make}\n'
                f'model:{self.model}\n'
                f'year:{self.year}\n')
            

ford =Car(make='ford', model='kia', year=2024)
ford.display_info()
ford.start()
