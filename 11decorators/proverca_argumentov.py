# Проверка аргументов

from functools import wraps


def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Keyoword arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper


@prohibit_kwargs
def print_hello(name):
    print(f'Hello {name}')


print_hello('Jack')
