"""
### Assignment 3: Adding Methods and Exception Handling
**Required Knowledge**: Class Methods, Basic Exception Handling
**Instructions**:
1. Extend the `Car` class by adding a method named `start_engine`.
2. Inside `start_engine`, raise an exception if the car's `make` is `"Unknown"`. Use the built-in `ValueError`.
3. Catch the exception in a `try...except` block and print an appropriate message.
4. Test this by creating a car with `make="Unknown"` and calling `start_engine`.
"""
class Car:
    def __init__(self,make=None,model=None):
        self.make=make
        self.model=model
    def print_car_info(self):
        try:
            print(f"Make: {self.make}, Model: {self.model}")
        except AttributeError:
            print("Error: Make or Model attribute is not set.")
    def start_engine(self):
        try:
            if self.make == "Unknown":
                raise ValueError("Cannot start engine of an unknown car")
            print("Vroom! Engine started.")
        except ValueError as e:
            print(f"Error: {e}")
            
car1 = Car("Toyota", "Corolla")
car1.print_car_info()  # Output: Make: Toyota, Model: Corolla

car2 = Car()
car2.print_car_info
