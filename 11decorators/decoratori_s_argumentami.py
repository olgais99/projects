
# Декораторы с аргументами

from functools import wraps


# во внешней части мы передаем значения которые мы будем проверять
def check_if_first_arg_is(value):
    def inner_dec(func):     # передаем функцию которую будем декорировать
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@check_if_first_arg_is('red')
def print_rainbow_colors(*colors):
    print(colors)

#  Если убрать из списка red, декоратор будет выдавать что первым аргументов долдна быть красный


print_rainbow_colors('orange', 'yellow', 'green', 'blue', 'indigo', 'violet')


# Создаем декоратор который будет приводить к нужному типу аргументы


def enforce(*types):
    def inner_dec(func):
        @wraps
        def wrapper(*args, **kwargs):
            new_args = []        # пустой массив
            for a, t in zip(args, types):   # zip создает из 2 последовальностей новую последовательность
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', 3)

# *args - ('Hi!', '3')
# *types - (str, int)
# zip(args, types) - ('Hi!', str) ('3', int)
