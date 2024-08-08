class OverSpeedError(Exception):
    pass

class Car:
    def __init__(self, make, model, speed=0):
        self.make = make
        self.model = model
        self.speed = speed

    def accelerate(self, increase):
        self.speed += increase
        if self.speed > 120:
            raise OverSpeedError(f"Speed {self.speed} exceeds the limit!")

try:
    my_car = Car("Toyota", "Corolla")
    my_car.accelerate(130)  # Should raise OverSpeedError
except OverSpeedError as e:
    print(e)
