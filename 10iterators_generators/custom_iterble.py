# Custom iterable = создаем свои собственные iterable

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = start  # текущее положение в этой последовательности это первый элемент

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.end:
#             number = self.current
#             self.current += 1
#             return number
#         raise StopIteration


# first_range = MyRange(20, 30)
# for number in first_range:
    # print(number)
