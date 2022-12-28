# # LISTS Список - это упорядоченная последовательность обьектов которые можно указать в квадратных скобках. Эти обьекты разделяются между собой запятыми
# # number_list = [32, 21, 48, 34.56]
# # print(number_list)
# some_list = [12, 35.334, 'hello']
# # print(some_list)

# # функции len -  узнать количество элементов при (3 элемента в some list)
# # print(len(some_list))

# # вывести нужный элемент (элементы считаются с 0)
# # print(some_list [1])

# #  slicing вырезаем элементы
# another_list = some_list [:2]
# # print(another_list)

# # присваиваем новое значение в строке, так как строки неизменяемы
# some_list[2] = 'hi'
# print(some_list)

# #  конкатенация(совмещение) списков
# new_list = some_list + another_list
# print(new_list)

# # метод append -  мы хотим добавить еще один элемент в список (добавляет элемент в конец списка)
# new_list.append('new item')
# print(new_list)

# # метод insert -  если мы хотим вставить элемент не в конец списка а куда мы хотим (индекс куда хотим вставить, "название")
# new_list.insert(6, 'start')
# print(new_list)

# # метод pop - удаление элементов, вставляем индекс в () который хотим удалить
# new_list.pop(0)
# print(new_list)

# метод sort = сортируем цифры по возрастанию, буквы по алфавиту
# number_list = [45, 12, 3, -455, 22]
# letter_list = ['s', 'w', 't', 'a']
# number_list.sort()
# letter_list.sort()
# print(number_list)
# print(letter_list)

# метод reversed - переворачивает элементы в обратном порядке
# number_list.reverse()
# letter_list.reverse()
# print(number_list)
# print(letter_list)

# метод append - добавить список в список
# number_list.append(letter_list)
# print(number_list)
# print(letter_list)


# iphones = [14, 'x', 6]
# old_iphones = [5, 4, 3, '2g']

# # iphones.append (11)
# # iphones.append (12)
# # iphones.append (13)
# # print(iphones)
# iphones.insert(1, 11)
# iphones.insert(1, 12)
# iphones.insert(1, 13)
# iphones.append(old_iphones)
# print(iphones)


# resoult=[14,13,12,11,'x',6,[5,4,3,'2g']]
