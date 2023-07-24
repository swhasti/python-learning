class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


class Car(Vehicle):
    def __init__(self, name, color, tires):
        Vehicle.__init__(self, name, color)
        self.tires = tires

    def get_tires(self):
        return self.tires


class Bike(Vehicle):
    def __init__(self, name, color, tires):
        Vehicle.__init__(self, name, color)
        self.tires = tires

    def get_tires(self):
        return self.tires


car = Car("Honda", "Blue", 4)
print("car name={} color={} tires={}".format(car.get_name(), car.get_color(), car.get_tires()))
bike = Bike("Pulsar", "Black", 2)
print("bike name={} color={} tires={}".format(bike.get_name(), bike.get_color(), bike.get_tires()))

print("------------ End -----------")


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


class Apple(Fruit):
    def __init__(self, name, color, seeds):
        Fruit.__init__(self, name, color)
        self.seeds = seeds

    def get_seeds(self):
        return self.seeds


class Banana(Fruit):
    def __init__(self, name, color):
        Fruit.__init__(self, name, color)
        self.color = color

    def get_color(self):
        return self.color


apple = Apple("Apple", "Red", 4)
print("apple name={} color={} seeds={}".format(apple.get_name(), apple.get_color(), apple.get_seeds()))
banana = Banana("Banana", "Yellow")
print("banana name={} color={}".format(banana.get_name(), banana.get_color()))

print("---------- End ----------")


class Vegetable:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


class Tomato(Vegetable):
    def __init__(self, name, color, seeds):
        Vegetable.__init__(self, name, color)
        self.seeds = seeds

    def get_seeds(self):
        return self.seeds


class Carrot(Vegetable):
    def __init__(self, name, color):
        Vegetable.__init__(self, name, color)
        self.color = color

    def get_color(self):
        return self.color


tomato = Tomato("Tomato", "Red", 26)
print("tomato name={} color={} seeds={}".format(tomato.get_name(), tomato.get_color(), tomato.get_seeds()))
carrot = Carrot("Carrot", "Orange")
print("carrot name={} color={}".format(carrot.get_name(), carrot.get_color()))

print("--------------- End --------------")


class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


class Rose(Flower):
    def __init__(self, name, color, leaves):
        Flower.__init__(self, name, color)
        self.leaves = leaves

    def get_leaves(self):
        return self.leaves


class Sunflower(Flower):
    def __init__(self, name, color, leaves):
        Flower.__init__(self, name, color)
        self.leaves = leaves

    def get_leaves(self):
        return self.leaves


rose = Rose("Rose", "Pink", "Countless")
print("rose name={} color={} leaves={}".format(rose.get_name(), rose.get_color(), rose.get_leaves()))
sunflower = Sunflower("Sunflower", "Yellow", "Countless")
print("sunflower name={} color={} leaves={}".format(sunflower.get_name(), sunflower.get_color(), sunflower.get_leaves()))

print("----------- End ------------")

