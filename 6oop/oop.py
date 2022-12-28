# Обьектно ориентированное программирование = используется для описания при помощи средств языка программирования обьектов из кружающего мира, либо какого то процесса который существует в окружающей нас действительности. Чтобы использовать эту концепцию использютс такие понятия как классы и обьекты.
#  Класс можно рассмотреть как чертеж, либо рецепт изготовления по которой изготавливаются все обьекты этого класса. В классе описываются атрибуты и методы.


# my_list = [1, 2, 3]   # мы создаем обьект класса лист котороый содержит в себе значения
# my_list.append(4)
# print(my_list)


#  создаем собственный класс
# class MyFirstClass:   # название класса пишется с большими буквами
#     pass


# object_of_my_class = MyFirstClass()
# print(type(object_of_my_class))       #<class '__main__.MyFirstClass'>


#  создаем класс описывающий автомобиль, как присваивать значение атрибутам каждого обьекта


# class Car:

#     wheels_number = 4    # создаем атрибут для каждого обьекта класса вне методов

#     # после селф записываем название атрибута который мы хотим поместить в наш класс
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed

# # # создаем обьект класса car

# mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)
# print(mazda_car.name)
# print(mazda_car.is_crashed)
# print(mazda_car.wheels_number)

# bmv_car = Car(name='BMW', color='black', year=2018, is_crashed=False)
# print(bmv_car.name)
# print(bmv_car.year)
# print(bmv_car.wheels_number)


# class Notebook:

#     tracpad = 5
#     keyboard = 20
#     ecran = 25

#     def __init__(self, ssd, os, ram):
#         self.ssd = ssd
#         self.os = os
#         self.ram = ram


# macbook = Notebook(ssd=500, os='mac_os', ram=16)
# print(macbook.ssd)


# # если мы хотим узнать количество колес для нескольких автомобилей
# number_of_wheels_of_3_cars = Car.wheels_number *3
# print(number_of_wheels_of_3_cars)


# Методы класса = это функции который описываются внутри класса и эти функции выполняют какую то функциональность. часто они выполняют действия над атрибутами класса.

# class Car:

#     wheels_number = 4

#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed


#     def drive(self, city):
#         print(self.name + 'is driving to' + city)



# mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)
# print(mazda_car)


# #  создаем метод который будет изменять цвет машины

#   def change_color(self, new_color):
#     self.color = new_color


# opel_car = Car('Opel Tigra ', 'grey', '1999', True)
# opel_car.drive(' London')

# opel_car.change_color('yellow')
# print(opel_car.color)

# print(opel_car.wheels_number)
# print(opel_car.name)
# print(opel_car.color)
# print(opel_car.year)
# print(opel_car.is_crashed)
