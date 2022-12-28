# Запись в файл. writer()

import csv

# with open('students.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['First name', 'Last name', 'Age'])
#     csv_writer.writerow(['Jack', 'White', 24])
#     csv_writer.writerow(['Jane', 'Black', 23])

# Нужно считать данные и поместить их в какую то переменную

with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    make_model_list = []
    for car in csv_reader:
        make_model = [car[1], car[2]]
        make_model_list.append(make_model)
        print(make_model_list)

# мы получаем список в списке с маркой и моделью


#  Теперь мы можем записать в файл значения, должен создаться файл cars_make_model.csv в котором будут записаны данные

with open('cars_make_model.csv', 'w') as file:
    csv_writer = csv.writer(file)
    for row in make_model_list:
        csv.writer.writerow(row)
