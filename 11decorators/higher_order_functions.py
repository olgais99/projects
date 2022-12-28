# Higher order functions

# Функция высшего порядка которая принимает другие функции в качестве аргументов

from random import choice


def product(n, func):
    result = 1
    for number in range(1, n):
        result += func(number)
    return result


def summ(x):
    return x + x


print(product(3, summ))


# Мы можем передавать в качетсве элемента какую то встроенную функцию Пайтона

def my_function(a, b, func):
    result = func([a, b])
    return result


print(my_function(7, 3, sum))


#  Использование вложенной функции


def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    result = get_color() + ' ' + thing
    return result


print(colorize('apple'))


# Функция высшего порядка которая возвращает другие функции. В данном случае get_color возвращается из make_color


def make_color():
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    return get_color


first_color = make_color()
print(first_color())

second_color = make_color()
print(second_color())

third_color = make_color()
print(third_color())


# Мы можем получать доступ из внутрнеей функции к параметру внешней функции. Внутренние функции могут иметь доступ к области видимости внешней функции


def colorize1(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color()


print(colorize1('apple'))
colorized_dog = colorize1('dog')
print(colorized_dog)
