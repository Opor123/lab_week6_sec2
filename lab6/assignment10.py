import threading
import time

class Car:
    def __init__(self, make, model, fuel_level=100, speed=0):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level
        self.speed = speed

    def diagnostics(self):
        while True:
            print(f"Make: {self.make}, Model: {self.model}, Fuel Level: {self.fuel_level}, Speed: {self.speed}")
            time.sleep(1)

    def drive(self):
        while self.fuel_level > 0:
            self.speed += 10
            print(f"Driving... Speed: {self.speed} km/h")
            self.fuel_level -= 1
            time.sleep(2)
            if self.fuel_level <= 0:
                print("Out of fuel!")
                break

my_car = Car("Toyota", "Corolla")
diagnostics_thread = threading.Thread(target=my_car.diagnostics)
drive_thread = threading.Thread(target=my_car.drive)

diagnostics_thread.start()
drive_thread.start()

diagnostics_thread.join()
drive_thread.join()
