#  Область видимости = scope, используется для того чтобы определить в каком месте кода видна переменная

# pi = 'outer pi variable'   # внешняя переменная


# def print_pi():
#     pi = 'inner pi variable'    # присваивается значение
#     print(pi)


# print_pi()
# print(pi)


# # Local Scope локальный уровень

# pi = 'global pi variable'    #во внешнем scope определена переменная пи и присвоено значение
# def inner():          # определена функция иннер , в котороый переменная пи которая находится внутри функции присвоено значение
#     pi = 'inner pi variable'
#     print(pi)     # вызывается метод принт который распечатывает значение которое находится в переменной пи
# inner()


# Enclosed Scope   окружающая функция
# pi = 'global pi variable'

# def outer():    # функция внешняя
#     pi = 'outer pi variable'
#     def inner():
#         # pi = 'inner pi variable'
#         nonlocal pi   # обращение из внутренней функции во внешнюю
#     inner()

# outer()
# print(pi)


# Built-in Scope встроенная область
# from math import pi   # импорт из библиотеки math числа пи

# # pi = 'global pi variable'
nn = 'ff'


def outer():    
    re = 'kk'


    def inner():
        gg = 'll'


# outer()

# Обращение идет сначала с Local Scope, потом в Enclosed Scope, далее Global scope , и самый последний идет к Built-in Scope

    menti = 'ratia'


def podzemnaia_parcovka():
    def tonirovannie_masina_audi(): 
        petea = 'bong'

    def tonirovannie_masina_bmw():
        sereja = 'marihuana'

    def tonirovannie_masina_mercedes():
        roma = 'avtomat'


    ohranic = 'cluchi ot porcovci'




