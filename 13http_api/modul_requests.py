
#HTML запрос через терминал при помощи файла пайтон

import requests 

url = 'https://www.google.com/'
response = requests.get(url)
print(f'Requests to {url}. Status code is {response.status_code}')

# Requests to https://www.google.com/. Status code is 200 код выдве

# Можно вывести весь html текст на этой странице
print(response.text)




# https://earthquake.usgs.gov/fdsnws/event/1/query?
# format=geojson&
# starttime=2014-01-01&
# endtime=2014-01-02