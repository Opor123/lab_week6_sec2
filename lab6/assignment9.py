import time

class Car:
    def __init__(self, make, model, fuel_level=100, speed=0):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level
        self.speed = speed

    def diagnostics(self):
        print(f"Make: {self.make}, Model: {self.model}, Fuel Level: {self.fuel_level}, Speed: {self.speed}")

    def start_diagnostics(self):
        while True:
            self.diagnostics()
            time.sleep(1)

my_car = Car("Toyota", "Corolla")
my_car.start_diagnostics()
