#  файловый ввод/вывод   input/output

# input
# x = input('Input something')
# # output
# print('Output something')


# Разделитель слов двоеточием 1:2:3
# print(1, 2, 3, sep=':')


# значение функции open,  далее мы указываем путь файла. При помощи этой команды мы открываем этот файл и помещаем его в переменную


# lorem_ipsum_text = open('/Users/guest123/Desktop/sample (1).txt')
# for line in lorem_ipsum_text:  # выводим построчно файл
#     print(line)


# lorem_ipsum_text.close()         # обязательно закрыть командой close


# Мы можем выводить строки в которых есть слово которое мы хотим

# lorem_ipsum_text = open('/Users/guest123/Desktop/sample (1).txt')
# for line in lorem_ipsum_text:
#     if 'let' in line.lower():
#         print(line)
# lorem_ipsum_text.close()


# В версии пайтон 2.6 появилась возможность открывать файл при помощи оператора with. В данном случае нам не нужно закрывать файл, оператор with когда видит что работа с файлом закочена автоматически закрывает его

# with open('/Users/guest123/Desktop/sample (1).txt') as lorem_ipsum_text:
#     for line in lorem_ipsum_text:
#         if 'let' in line.lower():
#             print(line)


# Как работать с методом readline который читает построчно из файла. Метод readline читает одну строку. В случае с большими текстами лучше всего использовать построчныйй метод чтобы не перегружать пямять компьютера.

# with open('/Users/guest123/Desktop/sample (1).txt') as lorem_ipsum_text:
#     line = lorem_ipsum_text.readline()
#     while line:
#         # end='' выведет код без пустых строк между текстом
#         print(line, end='')
#         line = lorem_ipsum_text.readline()


# Получить доступ к строкам в виде листа. Метод = readlines читает содержимое всего файла и помещает в список

# with open('/Users/guest123/Desktop/sample (1).txt') as lorem_ipsum_text:
#     lines = lorem_ipsum_text.readlines()
# print(lines)

# # Переставим текст в обратном порядке

# for line in lines[::-1]:
#     print(line)


# Метод read читает весь файл и выводит весь текст в коде

# with open('/Users/guest123/Desktop/sample (1).txt') as lorem_ipsum_text:
#     text = lorem_ipsum_text.read()
# print(text)
