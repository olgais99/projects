# Парсить = Распознавать при помощи пакета BeautifulSoup,

from bs4 import BeautifulSoup

html_string = '''
    <!DOCTYPE html> 
<html> 
<head> 
    <title>Web Development Page</title>
    <style type="text/css">

        h1{
            color: white;
            background: red;
        }   

        li{
            color:red;
        }

        #css-li{
            color: blue;
        }

        .green{
            color: green;
        }
                
    </style>


</head>
<body>    
    <h1>Web development</h1>   
    <h1 class="green">Web</h1>    
    <h3>Programming Languages</h3>    

    <ol>   
        <li>HTML</li> 
        <li id="css-li">CSS</li>
        <li class="green">JavaScript</li>
        <li class="green">Python</li> 
    <ol>

</body>
</html>

'''


# указываем что мы распознаем html
parsed_html = BeautifulSoup(html_string, 'html.parser')

# print(parsed_html)
# print(type(parsed_html))

# у нас уже находится обьект этого класса, а не просто строка и теперь мы можем использовать разные методы этого обьекта для получения переменных

# print(parsed_html.body)    # мы получаем только раздел body
# print(parsed_html.find('li'))    # ищет параметр который мы задаем
# print(parsed_html.find_all('li'))    # ищет все одинаковые параметры
# print(parsed_html.find(id="css-li"))   # мы получаем именно этот элемент
# print(parsed_html.select('#css-li')[0])
# print(parsed_html.find_all(class_="green"))
# print(parsed_html.select(".green")[1])   # селект всегда будет выдавть список
# print(parsed_html.select("li")[3])
# html_elem = parsed_html.select("li")[0]
# print(html_elem.get_text())


# Мы хотим получить только текст этого элемента

# print(html_elem.get_text())

# Получить список всех элементов li

# html_elem_list = parsed_html.select('li')

# for html_elem in html_elem_list:
#   print(html_elem.get_text())