#  Наследование, полифоризм

# class Car:

#     wheels_number = 4

#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')

#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)

#     def change_color(self, new_color):
#         self.color = new_color
#         print('Color is changed to ' + new_color)

#         #  Например мы хотим создать класс грузовик, в которм нам бы тоже пригодились методы drive и  change color, мы можем создать потомка нашего класса car. когда мы создаем наследника мы можем пользоваться всеми методами и атрибутами предка. Также мы можем преопределять и создавать свои методы.


# class Truck(Car):

#     wheels_number = 6

#     def __init__(self, name, color, year, is_crashed):  # мы передаем аргументы
#         # инициализируется обьект класса предка Car в котором тоже будут инициализироваться эти атрибуты
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')

#     def drive(self, city):     # переопределяем метод
#         print('Truck ' + self.name + ' is driving to ' + city)


# # Также мы можем в потомке создавать метод которого нет в предке


#     def load_cargo(self, weight):
#         print('The cargo is loaded. Weight is ' + str(weight))


# man_truck = Truck('Man', 'white', 2015, False)

# man_truck.drive('New york')

# print(man_truck.wheels_number)

# man_truck.change_color('red')

# man_truck.load_cargo(2000)


# # Полиморфизм = многообразный, много форм.

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(self.name + ' is saying woof')


# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(self.name + ' is saying meow')


# class Mouse:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(self.name + ' is saying pee-pee')


# spike = Dog('Spike')

# tom = Cat('Tom')

# jerry = Mouse('Jerry')


# pet_list = [spike, tom, jerry]   # создаем список домашних животных

# for pet in pet_list:
#     pet.speak()
