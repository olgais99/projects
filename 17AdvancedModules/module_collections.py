
# Модуль collections. Counter = ЭТО ВСТРОЕННЫЙ В ПАЙТОН МОДУЛЬ, он импромитирует специальные контейнерные типы данных которые предоставляют альтернативы общим встроенным контейнерам языкам пайтон такие как dict, list, set, tuple

#  Код выведет ключи и значения сколько раз повторяется ключ в данном списке

# from collections import Counter 

# number_list = [1, 1, 1, 4, 4, 5, 77, 77, 3, 3, 3, 3]

# string = 'dddddkkkkkeeeeeeooooooiiiiiiiiiii'

# sentence = 'Hello, how are you doing? Hello, im fine. How do you do? Hey Hey Hey'

# c = Counter(sentence.split(' '))    # узнаем сколько слов в предложении
# print(sum(c.values()))

# print(Counter(number_list))
# print(Counter(string))
# print(Counter(sentence.split(' ')))

# print(list(c))      # все элементы предложения будут в виде списка
# print(set(c))      # все элементы предложения будут в виде сета
# print(dict(c))      # все элементы предложения будут в виде словаря

# print(c.items())    # мы получаем список из пар элементов и колво сколько раз встречаетсяи все это в списке

# print(c.most_common)   # выдает самые часто втречающиеся элементы





# Модуль collections. defaultdict Это модуль который вызывает заводскую функцию чтобы предоставить отсутствующие значения

# from collections import defaultdict

# my_dict = defaultdict(object)
# my_dict[1] = 'a'

# print(my_dict[2])    # defaultdict если у нас нет такого  индекса просто выдает то что у нас в переменной, не выдает ошибку





# Модуль collections. namedtuple()

# С данным модулем становится меньше вероятность того чтобы перепутать какой то индекс

from collections import namedtuple

jake = ('Jake', 'Smith', 19, 'male')
jim = ('Jim', 'Blade', 23, 'male')
lane = ('Lane', 'Morison', 20, 'female')


Person = namedtuple('Person', 'name surname age gender')
jake = Person(name = 'Jake', surname = 'Smith', age = 19, gender = 'male')

print(jake.name)
print(jake.age)
print(jake.surname)