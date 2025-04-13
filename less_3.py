class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f"Car {self.model} is driving")

    def __str__(self):
        return f"Model: {self.__model}, Year: {self.__year}, Color: {self.__color}"

class FuelCar(Car):
    def __init__(self, model, year, color, fuel_bank):
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank

    def drive(self):
        print(f"Car {self.model} is driving by fuel.")

    def __str__(self):
        return super().__str__() + f" Fuel Bank: {self.__fuel_bank}"

class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    def drive(self):
        print(f"Car {self.model} is driving by electricity.")

    def __str__(self):
        return super().__str__() + f" Battery: {self.__battery}"

class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color,fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


toyota_car = FuelCar("Toyota Camry", 2021, "red", 80)
byd_car = ElectricCar("BYD 350", 2021, "blue", 15000)
chevrolet_car = HybridCar("Chevrolet Volt", 2023, "white", 70, 10000)
# some_car = Car("Toyota Camry", "2020", "red")
print(toyota_car)
print(byd_car)
print(chevrolet_car)
chevrolet_car.drive()
print(HybridCar.mro())


