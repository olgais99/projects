
# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')

html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_='quote')

#  Как получить только цитаты 

for quote in quotes:
    print(quote.find(class_='text').get_text())

#  Как получить только автора цитаты

    print(quote.find(class_='author').get_text())

#    Как получить только теги к цитатам

    print(quote.find(class_='keywords')['content'])