# Знакомство с декораторами

def simple_function():
    print('Simple function code')

# simple_function()


# ТЕПЕРЬ ПРОДЕЛАЕМ ТО ЖЕ САМОЕ ТОЛЬКО С ДЕКОРАТОРОМ

def decorator_function(original_function):      # Мы передаем original_function
    def wrap_function():                        # определяем еще одну функцию
        print('Some code before the old code')
        original_function()
        print('Some code after the old code')
    return wrap_function


decorated_function = decorator_function(simple_function)

decorated_function()


# Иногда нужно отключать код, для этого нам нужна запись с @, закоментировать строку с @ add и код будет выдавать старую функциональность

@decorator_function
def simple_function():
    print('Simple function code')


simple_function()


# def make_compliment(func):
#     def wrapper(name):
#         print('Nice to meet you!')
#         func(name)
#         print('You look great!')
#     return wrapper


# @make_compliment
# def ask_name():
#     print('What is your name?')


# ask_name()


# @make_compliment
# def say_name(name):
#     print('My name is ' + name)


# say_name('Jack')
