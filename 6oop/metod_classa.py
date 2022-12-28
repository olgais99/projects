# Метода класса

# class Gamer:

#     active_gamers = 0

#     @classmethod
#     def gamer_from_string(cls, data_string):
#         nickname, age, level, points = data_string.split(',')
#         return cls(nickname, age, level, points)

#     def __init__(self, nickname, age, level, points):
#         self.nickname = nickname
#         self.age = age
#         self.level = level
#         self.points = points
#         Gamer.active_gamers += 1

#     def get_nickname(self):
#         return self.nickname

#     def get_age(self):
#         return self.age

#     def get_level(self):
#         return self.level

#     def get_points(self):
#         return self.points

#     def is_adult(self):
#         return self.age >= 18

#     def get_adult_level_permission(self):
#         if self.is_adult():

#             print('You can go to adult level')
#         else:

#             print('You cant go to adult level')


# print(Gamer.active_gamers)


# gamer_1 = Gamer('hell_boy', 23, 5, 13)

# gamer_2 = Gamer('sici', 13, 7, 34)

# print(gamer_1.get_age())
# print(gamer_1.get_adult_level_permission())


# print(gamer_2.get_age())
# print(gamer_2.get_adult_level_permission())

# print(Gamer.active_gamers)


# james = Gamer.gamer_from_string('James, 34, 2, 45')

# jane = Gamer.gamer_from_string('Jane, 24, 3, 5')

# print(james.get_age())
# print(jane.get_level())


# # Метод класса словарь dict, мы можем создать из 2 последоватльностей какой то словарь

# # Мы присваиваем каждому ключу присваиваем 2 параметр одинковый для всех ключей

# my_dict = dict.fromkeys((1, 2, 3), ('apple', 'orange', 'banana'))
# print(my_dict)


# #  Наследование, полифоризм

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
