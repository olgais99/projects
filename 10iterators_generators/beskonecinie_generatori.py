# Бесконечные генераторы

# def create_patterns():
#     max_patterns_number = 100
#     patterns = ('Firts pattern', 'Second pattern',
#                 'Third pattern', 'Forth pattern')
#     i = 0
#     result_list = []
#     while len(result_list) < max_patterns_number:
#         if i >= len(patterns):
#             i = 0
#         result_list.append(patterns[i])
#         i += 1
#     return result_list


# print(create_patterns())


# Таким способом мы добьемся чтобы можно было бесконечно выводить код без ошибки что он закончен

# def get_current_pattern():
#     patterns = ('Firts pattern', 'Second pattern',
#                 'Third pattern', 'Forth pattern')
#     i = 0
#     while True:
#         if i >= len(patterns):
#             i = 0
#         yield patterns[i]
#         i += 1


# current_pattern = get_current_pattern()
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())
# print(current_pattern.__next__())
