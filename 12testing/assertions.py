
# Assertions
# Тестирование это написание тестового кода который проверяет баги в нашем коде

assert 2 + 2 == 4
assert 2 + 2 == 5, '2 + 2 must be 4'  # AssertionError: 2 + 2 must be 4


def divide(a, b):
    assert b != 0, 'b must not be 0'
    return a / b


print(divide(2, 2))
print(divide(2, 0))


def multiplay_positive_numbers(a, b):
    assert a > 0 and b > 0, 'a and b must be positive'
    print(a * b)


multiplay_positive_numbers(3, 5)
multiplay_positive_numbers(3, -5)  # AssertionError: a and b must be positive


def get_access(password):
    password_list = [111, 222, 333]
    assert int(password) in password_list, 'Password is invalid'
    print('You can make dangerous stuff')


# password_1 = input('Please input the password')
# get_access(password_1)

# если вводим неправильный пароль - Assertion
