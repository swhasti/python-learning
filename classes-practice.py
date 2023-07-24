class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight

    def is_over_weight(self):
        if self.weight > 100.0:
            return True
        return False

    def is_under_weight(self):
        if self.weight <= 100.0:
            return True
        return False


persons = []
tom = Person("Tom", 84.2)
persons.append(tom)
jerry = Person("Jerry", 170.0)
persons.append(jerry)

for person in persons:
    print("name={} weight={}".format(person.name, person.weight))
    print("is {} overweight? {}".format(person.get_name(), person.is_over_weight()))
    print("is {} underweight? {}".format(person.get_name(), person.is_under_weight()))

print("------- End ----------")


class Animal:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def get_name(self):
        return self.name

    def get_height(self):
        return self.height

    def set_name(self, name):
        self.name = name

    def set_height(self, height):
        self.height = height

    def is_short_height(self):
        if self.height > 8.0:
            return True
        return False

    def is_tall_height(self):
        if self.height <= 8.0:
            return True
        return False

animals = []
lion = Animal("lion", 420.0, 4)
animals.append(lion)
fox = Animal("fox", 14, 8)
animals.append(fox)
tiger = Animal("tiger", 400.2, 3)
animals.append(tiger)

for animal in animals:
    print("name={} weight={} height={}".format(animal.name, animal.weight, animal.height))
    print("is {} shortheight? {}".format(animal.get_name(), animal.is_short_height()))
    print("is {} tallheight? {}".format(animal.get_name(), animal.is_tall_height()))

print("----------- End ----------")


class Fruit:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
         self.name = name

    def set_price(self, price):
        self.price = price

    def is_expensive(self):
        if self.price > 30.19:
            return True
        return False


fruits = []
apple = Fruit("apple", 6.4, 31.19)
fruits.append(apple)
banana = Fruit("banana", 4.2, 15.6)
fruits.append(banana)
orange = Fruit("orange", 3.47, 6.44)
fruits.append(orange)
orange.weight = 4.10

for fruit in fruits:
    print("name={} weight={} price={}".format(fruit.name, fruit.weight, fruit.price))
    print("is {} expensive? {}".format(fruit.get_name(), fruit.is_expensive()))
print("--------- End -------")


class Flower:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
         self.name = name

    def set_price(self, price):
         self.price = price

    def is_expensive(self):
        if self.price > 10.25:
            return True
        return False


flowers = []
rose = Flower("rose", 15.25)
flowers.append(rose)
lotus = Flower("lotus", 30)
flowers.append(lotus)
sunflower = Flower("sunflower", 8.99)
flowers.append(sunflower)

for flower in flowers:
    print("name={} price={}".format(flower.name, flower.price))
    print("is {} expensive? {}".format(flower.get_name(), flower.is_expensive()))
print("----------- End ----------")


class Tiffin:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def is_expensive(self):
        if self.price > 40.66:
            return True
        return False


tiffins = []
idli = Tiffin("idli", 46.66)
tiffins.append(idli)
dosa = Tiffin("dosa", 15)
tiffins.append(dosa)

for tiffin in tiffins:
    print("name={} price={}".format(tiffin.name, tiffin.price))
    print("is {} expensive? {}".format(tiffin.get_name(), tiffin.is_expensive()))
print("--------- End ----------")


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def is_expensive(self):
        if self.price > 46890.0:
            return True
        return False


cars = []
honda = Car("honda", 23800)
cars.append(honda)
tesla = Car("tesla", 46990)
cars.append(tesla)

for car in cars:
    print("name={} price={}".format(car.name, car.price))
    print("is {} expensive? {}".format(car.get_name(), car.is_expensive()))
print("-------- End ---------")

maxName = ''
maxWeight = 0
for person in persons:
    if maxWeight < person.weight:
        maxWeight = person.weight
        maxName = person.name
print("MaxName={} MaxWeight={}".format(maxName, maxWeight))
print("-------- End Names ---------")

maxWeightAnimal = ''
maxWeight = 0
maxHeightAnimal = ''
maxHeight = 0
for animal in animals:
    if maxWeight < animal.weight:
        maxWeight = animal.weight
        maxWeightAnimal = animal.name

    if maxHeight < animal.height:
        maxHeight = animal.height
        maxHeightAnimal = animal.name
print("maxWeightAnimal={} maxWeight={} maxHeightAnimal={} maxHeight={}".format(maxWeightAnimal, maxWeight, maxHeightAnimal, maxHeight))
print("--------- End Animals ---------")

maxName = ''
maxPrice = 0
for car in cars:
    if maxPrice < car.price:
        maxPrice = car.price
        maxName = car.name
print("MaxName={} MaxPrice={}".format(maxName, maxPrice))
print("-------- End Cars ----------")

maxTiffin = ''
maxPrice = 0
for tiffin in tiffins:
    if maxPrice < tiffin.price:
        maxPrice = tiffin.price
        maxTiffin = tiffin.name
print("MaxTiffin={} MaxPrice={}".format(maxTiffin, maxPrice))
print("-------- End Tiffins ---------")

maxFlower = ''
maxPrice = 0
for flower in flowers:
    if maxPrice < flower.price:
        maxPrice = flower.price
        maxFlower = flower.name
print("MaxFlower={} MaxPrice={}".format(maxFlower, maxPrice))