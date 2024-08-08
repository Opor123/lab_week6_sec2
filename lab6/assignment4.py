"""
### Assignment 4: Fuel Check and Basic Exception Handling
**Required Knowledge**: Class Methods, Basic Exception Handling
**Instructions**:
1. Extend the `Car` class by adding an attribute `fuel_level` that represents the car’s current fuel level.
2. Add a method named `check_fuel` that raises a `ValueError` if `fuel_level` is less than 5.
3. Implement a method named `drive` that reduces the `fuel_level` by a certain amount and calls `check_fuel`.
4. Test this by driving the car and catching the `ValueError` if the fuel level gets too low.
"""
class Car:
    def __init__(self, make, model, fuel_level):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level

    def check_fuel(self):
        if self.fuel_level < 5:
            raise ValueError("Fuel level is too low!")

    def drive(self, amount):
        self.fuel_level -= amount
        self.check_fuel()
        print(f"Driving... Fuel level: {self.fuel_level}")

my_car = Car("Toyota", "Corolla", 10)

try:
    my_car.drive(3)  # Should be fine
    my_car.drive(4)  # Should be fine
    my_car.drive(3)  # Should raise ValueError
except ValueError as e:
    print(e)
