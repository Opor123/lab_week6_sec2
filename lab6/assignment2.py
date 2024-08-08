"""
### Assignment 2: Basic Exception Handling
**Required Knowledge**: Basic Exception Handling, Try-Except Block
**Instructions**:
1. Modify the `Car` class to include a method named `print_car_info()` that prints the car's make and model.
2. Add exception handling in the `print_car_info()` method using a try-except block to handle potential errors (e.g., if the attributes are not set using AttributeError to handle exception).
3. Test the method by:
   
Creating a `car1` object with valid `make` and `model` attributes and calling `print_car_info()`.
   
Creating a `car2` object without setting the attributes (or by setting them to `None`) and calling `print_car_info()` to see how the exception is handled.
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

# Test the method
car1 = Car("Toyota", "Corolla")
car1.print_car_info()  # Output: Make: Toyota, Model: Corolla

car2 = Car()
car2.print_car_info