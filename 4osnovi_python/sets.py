# # Sets = множество.{}, в отличии от  Dictionaries можно писать только значения. Это неупорядоченная коллекция уникальных элементов, то есть в множестве не может быть двух одинаковых элементов.
#
# rainbow_colors = {'red', 'orange', 'yellow', 'green', 'indigo', 'violet'}
# print(rainbow_colors)
# # Выведем тип переменной <class 'set'>
# print(type(rainbow_colors))

# #Создаем пустое множество неверно
# empty_set = {}
# print(empty_set)
# print(type(empty_set)) #Выводит класс dictionaries <class 'dict'>

# #Нам надо вывести именно пустое множество, для этого есть функция set
# empty_set = set()
# print(empty_set)
# print(type(empty_set))

# # таким образом мы меняем тип данных на set
# number_list = [1, 43, 56]
# text_tuple = ('eye', 'lips', 'eyebrow')
# set_from_list = set(number_list)
# set_from_tuple = set(text_tuple)
# # print(number_list)
# print(text_tuple)
# print(set_from_list)
# print(set_from_tuple)

# если у нас элементы неупорядочены и повторяются , преобразование в set их упорядочит и удалить повторяющиеся элементы, (это относится ко всем типам данных)
# list_num=[1,2,1,2,3,4,5,5,6,7,7,8,9,0,1,2,5,3]
# set_num = set(list_num)
# list_set_num = list(set_num)
# print(list_set_num)

# # # Добавим элементы в множество
# set_from_list.add(777)
# set_from_tuple.add('nose')

# # Метод pop = Удалить cоучайный элемент из множества
# set_from_list.pop()
# #Метод remove = Удалить конкретный элемент из множества
# set_from_list.remove(43) # если элемент уже удален, а мы его удаляем снова код выдаст ошибку
# #Метод discard = Удалить конкретный элемент из множества
# set_from_list.discard(43) # если элемент уже удален, а мы его удаляем снова код не выдаст ошибку, так как видит что элемента и так не было

# #Метод clear = Удалить все элементы
# set_from_list.clear()

# print(set_from_list)
# print(set_from_tuple)

# # #Д/З

# text = 'I have eyes and boobies'
# new_text = set(text)
# print(new_text)
# print(type(new_text))


# # ДЗ по Dictionaries
# people_eyes = {'olga' : 'brown', 'sophia' : 'blue', 'henry' : 'green'}
# print(people_eyes['olga'])

# computer = {
# 'model' : 'Macbook Pro',
# 'color' : 'Silver',
# 'year' : '2020',
# 'memory' : '8 gb'
# }
# print(computer)


# #ДЗ по LISTS
# list = [7, 8.355, 'hello']
# print(list)

# list_1 = [12, 78.678, 'peace', 'hi', 'hey']
# new_list = list_1[:3]
# print(new_list)
