class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = None

    def read_color_from_file(self, filepath):
        try:
            with open(filepath, "r") as file:
                self.color = file.read().strip()
            print(f"Car color: {self.color}")
        except FileNotFoundError:
            print(f"Error: The file at {filepath} was not found.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

my_car = Car("Toyota", "Corolla")
my_car.read_color_from_file("color.txt")
my_car.read_color_from_file("non_existent_file.txt")
