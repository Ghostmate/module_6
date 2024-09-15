class Animal:
    alive = True
    fed = False
    name = ''

    def set_name(self, name):
        self.name = name


class Plant:
    edible = False
    name = ''

    def set_name(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        self.set_name(name)

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
                return
        self.alive = False


class Predator(Animal):
    def __init__(self, name):
        self.set_name(name)

    def eat(self, food):
        if isinstance(food, Animal):
            self.fed = True
            return
        print(f'{self.name} не стал есть {food.name}')
        self.alive = False


class Flower(Plant):
    def __init__(self, name):
        self.edible = False
        self.set_name(name)


class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.set_name(name)

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)