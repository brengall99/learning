
# Okay, lets write a class for cars. 
cars = [
    ['Ford Explorer', 5.5, 190, 0, 100,000.00],
    ['Nissan Micra', 1.0, 85, 0, 32,000.00],
    ['Hyundai Kona', 3.0, 200, ]

]

class Cars:
    def __init__(self, brand: str, engine_size: float, horsepower: int, electric: bool, price: float):
        self.brand = brand
        self.engine_size = engine_size
        self.horsepower = horsepower
        self.electric = electric
        self.price = price

class ElectricCar(Cars):
    def __init__(self, brand: str, horsepower: int, price: float, battery_range: int, battery_capacity: float):
        # Call the parent class's __init__ to set the inherited attributes
        super().__init__(brand, engine_size=0.0, horsepower=horsepower, electric=True, price=price)
        self.battery_range = battery_range
        self.battery_capacity = battery_capacity




# We want to use the CarModels class on a car
# Were going to have brand, engine size, horsepower, electric y/n, and price > 100,000