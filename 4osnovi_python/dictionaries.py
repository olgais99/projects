# #Dictionaries {} поиск значения как в словаре, ключ = название автомобиля, значение = цена. Словарь не может иметь одинаковых ключей, ключи это уникальный элемент каждой пары, который определяет эту пару  
# # car_prices = {'opel':5000, 'toyota': 7000, 'bmw':10000}
# # # print(car_prices)

# # # # получить доступ к какому то элементу словаря и узнать значение
# # print(car_prices['toyota'])

# # # #добавить новый элемент в словарь 
# # car_prices['mazda'] = 4000 
# # print(car_prices)

# # # # команда del - удалить значение 
# # del car_prices['toyota']
# # print(car_prices)

# # # метод clear - удаляет весь словарь 
# # car_prices.clear()
# # print(car_prices)
# #еще один способ удаления словаря
# # car_prices = {}
# # print(car_prices)

# # По ключу может содержаться целый список
# person = {
#   'first name': 'Jack',
#   'last name': 'Brown',
#   'age': 43,
#   'hobbies': 
#   [
#     'football', 'singing', 'photo'], 
#   'children': 
#   {
#     'son': 'Michael', 'daughter': 'Pamela'}
# }
# # print(person['age'])
# # print(person ['hobbies'])

# # # Если нам нужно вывести определенное хобби из списка [индекс] 
# # print(person['hobbies'][2])
# # print(person['children']['son'])

# # # Добавить в структуру списка еще позиции 
# person['car'] = 'Mazda'
# # print(person)

# # # Поменять элемент в списке
# person['hobbies'][0] = 'dancing'
# # print(person)

# # # Метод keys - показывает все существующие ключи в словаре (первого уровня глубины)
# # print(person['children'].keys())

# # # Метод values - показывает все значения в словаре (первого уровня глубины)
# # print(person.values())

# # # Метод items - показывает все существующие элементы в списке
# print(person.items())

# per = person ['hobbies'][2]
# print(per)



yazan = { 
    'age' : 23,
    'íphone' : 11,
    'macbooc': 2015,
    'last_name' : 'darwish',
    'work': [9, 18],
    'money': {'50 euro' : 10, '100 euro' : 4}
}
olga = { 
    'age' : 23,
    'samsung' : 's21',
    'macbooc': 2017,
    'last_name' : 'ischimji',
    'work': [9, 18],
    'money': {'100 euro' : 8}

}
another = {}

##########################################
# тут мы достаем значение
yazan_age = yazan ['age']
olga_phone = olga ['samsung']
olga_macbooc = olga ['macbooc']
yazan_macbooc = yazan ['macbooc']
yazan_phone = yazan ['íphone']
yazan_last_name = yazan ['last_name']
olga_last_name = olga ['last_name']
olga_work = olga ['work']
yazan_euro = yazan ['money']


# тут мы добавляем значения в пустй словарь под названием another
another['age'] = yazan_age
another['samsung'] = olga_phone
another['macbooc1'] = olga_macbooc
another['macbooc2'] = yazan_macbooc
another['iphone'] = yazan_phone
another['work'] = olga_work
another['money'] = yazan_euro


#  создали пустой лист и добавили в него наши фамилии
last_names = []
last_names.append(yazan_last_name)
last_names.append(olga_last_name)
# записали в словарь ласт нэйм и в значении ключа добавили лист с фамилиями
another['last_names'] = last_names
# в словаре язан мы стучим по ключу mоney и там у нас другой словарь и в вложенном словаре мы стучим по ключу 100 евро так же делаем и с ольгой
yazan_money = yazan['money']['100 euro']
olga_money = olga['money']['100 euro']
# тут мы складываем наши по 100 евро
euro_100 = yazan_money + olga_money
# так как мы берем за шаблон словарь яязана money(строка 103) то мы у него переписываем наши сложенные по 100 евро
another['money']['100 euro'] = euro_100



print(another)




# another = { 
#     'age' : 23,
#     'samsung' : 's21',
#     'macbooc1': 2017,
#     'íphone' : 11,
#     'macbooc2': 2015,
#     'last_name' : ['darwish','ischimji'],
#     'work': [9, 18],
#     'money': {'50 euro' : 10, '100 euro' : 12}
# }
