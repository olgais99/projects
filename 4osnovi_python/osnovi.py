
# print - функция которая выводит все что у нее в круглых скобках

from string import whitespace


print('I will be a Phyton developer!')

print(2+2)
print(2-2)
print(2*2)
print(2/2)
print(2**3)
print(3*7)
print(4**3)
print(29/5)

# указанная х является переменной (ячейка памяти) которая хранит в себе цифру 5
x = 5
print(x)
# тут мы перезаписываем переменную х строкой
x = "hello"
# print(x)
x = 'hi'

# type - узнать тип переменной данных
type_of_variable = type(x)
print(type_of_variable)

# разделение букв способом нижнего подчеркивания
car_color = 'orange'

# через переменные х и y можем выводить значения
x = 5
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x**y)
print(x % y)

# Calculating of credit final sum
credit = 9000
credit_rate = 12
number_of_years = 5
final_sum = credit + credit / 100 * credit_rate * number_of_years
print(final_sum)

# Car
Car_model = "Mercedes"
Car_color = "black"
Car_year = 2020
Door_number = 4
print(Car_model)
print(Car_color)
print(Car_year)
print(Door_number)

# Average Age of people
person_1_age = 18
person_2_age = 25
person_3_age = 30
person_4_age = 28
person_5_age = 16
number_of_people = 5
average_age = (person_1_age + person_2_age + person_3_age +
               person_4_age + person_5_age) / number_of_people
print(average_age)

# строки
greeting = "hello!"
first_name = "harry"
last_name = "styles"
print(greeting + first_name + last_name)

# разделить слова в строке
greeting = "hello"
first_name = "harry"
last_name = "styles"
exclamation_sign = "!"
white_space = " "
print(greeting + white_space + first_name +
      white_space + last_name + exclamation_sign)

# escaping \ обратный слеш дает понять пайтону что мы используем кавычку как просто символ внутри строки
some_string = 'I\' m a programmer'
print(some_string)

# переносим строку на новую строку \n
string_with_new_lines = "Hello! \n My name is Harry Styles"
print(string_with_new_lines)

# табуляция \t создает несколько пробелов в строке
numbers = "1\t23\t45\t67"
print(numbers)

# тройные кавычки Tripple quotes (можно вставлять одинарнную кавычку без \)
string_with_tripple_quotes = """This is ' text with "triple quotes" """
print(string_with_tripple_quotes)
