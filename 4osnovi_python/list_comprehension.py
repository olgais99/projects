
# greeting = 'hello!'
# # letter_list = []
# # for letter in greeting:
# #     letter_list.append(letter)
# # print(letter_list) 

# мы создаем новый лист. Внутри листа мы пишем переменеую(letter) которая будет добавляться в качестве значений в лист. затем у нас есть for который перебирает строку внутри переменной greeting, записывает в пременную внтри своего for (letter) и добавялет в переменную о которойй мы написали ранее 
# ! (код который выше делает то же самое что этот кож) 
# letter_list = [
#     letter
#     for letter in greeting
#     ]
# print(letter_list) 


# letter_list = [
#     number
#     for number in '0123456789'
#     ]
# print(letter_list) 

# number_list_1 = [num for num in range (0, 10)]
# print(number_list_1)   

# ! в переменной лист перебирается лист который находится в numbr list и если перебираемый элемент больше 0, выведет '+', а в противном случае '-' 
# number_list = [6, 43, -1, 11, -55, -12, 3, 345]
# new_list = [
#     '+' if number > 0 else '-'
#     for number in number_list
#     ] 


# !  создается словарь в котором работает for. for работает таким образом , перебирая number_list знаение закидывает в свою переменную number и записывает в словарь ключ (number): значение (number * 2)
# number_list = [6, 43, -1, 11, -55, -12, 3, 345]
# number_dic = {
#     number: number * 2 
#     for number in number_list}
# print(number_dic) 