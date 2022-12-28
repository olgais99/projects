# Чтение файлов. reader()

# Как читать в коде нашу таблицу

import csv

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     for car in csv_reader:
#         print(car)


#  Как читать только марку, модель и цену

        # print(f'{car[0]} {car[1]} costs {car[3]}')

# Как получить данные списка в списке

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     data_list = list(csv_reader)
#     print(data_list)




# Чтение файлов. DictReader()

with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)           # используется для того чтобы не выходила 1 строка
    for car in csv_reader:
        print(car)
        print(f'{car["Make"]} {car["Model"]} costs {car["Price"]}')
