# запись текстовых файлов

# Создаем новый файл и помещаем в него наш список. 'w' означает writing, записывать.

# colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'dark green']


# with open('/Users/guest123/Desktop/rainbow_colors.txt', 'w') as rainbow_colors:
#     for color in colors_list:
#         print(color, file=rainbow_colors)


# #  Как получить содержимое файла где указаны знаки перехода на новую строку так как он содержится в файле. 'r' read

# colors_list = []

# with open('/Users/guest123/Desktop/rainbow_colors.txt', 'r') as rainbow_colors:
#     for color in rainbow_colors:
#         # метод strip('\n') он убирает символы перехода на новую строку в коде
#         colors_list.append(color.strip('\n'))

# print(colors_list)


# # Добавить текст в существующий файл. Параметр 'a' append, добавлять.

# with open('/Users/guest123/Desktop/rainbow_colors.txt', 'a') as rainbow_colors:
#     print('dark green', file=rainbow_colors)
#     print('dark blue', file=rainbow_colors)

