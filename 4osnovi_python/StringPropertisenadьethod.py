# Строки  являются неизменяемыми 
first_name = "Moldtelecom"
last_name = "f"
past_name = "n"
# print(first_name[2])
# first_name[2] = 'p'



x = first_name [4:8] # tele
print(x)
y = x + 'f' + first_name[9] + 'n'
print(y)

# можно умножать строки * YumYumYum
yummy = 'Yum'
print(yummy * 3)

# upper с большими буквами пишется код YUM
print(yummy.upper())
# lower с большими буквами пишется код yum
print(yummy.lower()) 


# split строка разбивается на слова This', 'is', 'the', 'long', 'string' \ если вставить в скобы бувку s код бyдет выводитcя без букв s
long_string = 'This is the long string'
print(long_string.split('s'))

