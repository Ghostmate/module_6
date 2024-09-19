import math


class Figure:
    sides_count = 0
    __sides = [0]
    __color = [0, 0, 0]
    filled = False

    def __init__(self, rgb, *args):
        # self.sides_count = sides
        self.set_color(*rgb)
        if len([*args]) == self.sides_count:
            self.set_sides(*args)
        else:
            self.set_sides(*([1] * self.sides_count))

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *rgb):
        if len(rgb) == 3:
            for col in rgb:
                if col not in range(0, 0xff):
                    return False
            return True
        return False

    def set_color(self, *rgb):
        if self.__is_valid_color(*rgb):
            self.__color = [*rgb]

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for side in [*args]:
                if not (isinstance(side, int) and side > 0):
                    return False
            return True
        return False

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        sum = 0
        if isinstance(self.__sides, int):
            sum += self.__sides
        else:
            for side in self.__sides:
                sum += side
        return sum

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]


class Circle(Figure):
    sides_count = 1
    __radius = 0
    def __init__(self, rgb, *args):
        self.sides_count = 1
        a = args
        if len([*args]) > self.sides_count:
            a = [1]
        super().__init__(rgb, *a)
        self.__radius = self.get_sides()[0]/(math.pi * 2)

    def get_square(self):
        return (self.__radius * self.__radius) * math.pi


class Triangle(Figure):
    sides_count = 3
    def __init__(self, rgb, *args):
        self.sides_count = 3
        super().__init__(rgb, *args)

    def get_square(self):
        p = self.__len__() / 2
        sqr = p
        sides = self.get_sides()
        for a in sides:
            sqr *= p - a
        return math.sqrt(sqr)


class Cube(Figure):
    def get_volume(self):
        a = self.get_sides()[0]
        return a * a * a

    def __init__(self, rgb, *args):
        self.sides_count = 12
        if len([*args]) == 1:
            args = [*args] * 12
        super().__init__(rgb, *args)

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
# triangle1 = Triangle((2,3,4),7,6,5)
# print(triangle1.get_sides(),triangle1.get_square(),triangle1.get_color())
# print(circle1.get_square())
