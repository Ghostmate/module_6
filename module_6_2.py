class Vehicle:
    owner = 'ООО Рога и небитые некрашеные машины'
    __model = 'base'
    __engine_power = 100500
    __color = 'black'
    # __COLOR_VARIANTS = ['black','black 1','black 2','any color you like as long as it\'s black']
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f'Модель: {self.__model}\n'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}\n'

    def get_color(self):
        return f'Цвет: {self.__color}\n'

    def set_model(self,model):
        self.__model = model

    def set_horsepower(self, power):
        self.__engine_power = power

    def print_info(self):
        print(self.get_model(),self.get_horsepower(),self.get_color(),f'Владелец: {self.owner}')

    def set_color(self,color):
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            print(f'Нельзя сменить цвет на {color}')

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5
    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.set_model(model)
        self.set_color(color)
        self.set_horsepower(power)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()