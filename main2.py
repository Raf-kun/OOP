class Car:
    def __init__(self, model, age, proizvoditel, volume, color, price):
        self.model = model
        self.__age = age
        self.proizvoditel = proizvoditel
        self.volume = input("Введите объём двигателя: ")
        self.color = color
        self.__price = price

    def get_age(self):
        return self.__age
    
    def get_price(self):
        return self.__price

    def self_color(self):
        color = input("Введите цвет: ")
        self._color = color
    def get_color(self):
        return self._color
    

car = Car("Tesla", "2015", "Musk", "White", "10000")
print(car.model, car.proizvoditel, car.volume)

car.set_color()
print(car.get_car(), car.get_color(), car.get_price())
