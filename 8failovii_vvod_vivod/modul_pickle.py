# Модуль pickle  = этот способ позволяет сереализировать обьект со всеми его данными, помещать в двоичный файл, а затем извлекать и восстанавливать все его данные и состояние в первоначальном виде.


# import pickle


# honda = (
#     'civic',
#     'grey',
#     '2009',
#     (
#         (1, 'James Brown'),
#         (2, 'Jane White'),
#         (3, 'Jake Green')

#     )

# )


# # 'wb' = записываем двочный файл

# with open('honda.pickle', 'wb') as honda_file:
#     pickle.dump(honda, honda_file)


# Извлечь обьект при помощи метода load

# with open('honda.pickle', 'rb') as honda_retrieved:
#     honda_from_file = pickle.load(honda_retrieved)

# print(honda_from_file)


# model, color, year, owner_list = honda_from_file

# print(model)
# print(color)
# print(year)


# for owner in owner_list:
#     owner_number, owner_name = owner
#     print(owner_number, owner_name)
