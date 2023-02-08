from unittest import result

import lxml
import requests
import json
from bs4 import BeautifulSoup

# def get_all_data():
#     url = ("https://cbr.ru/currency_base/daily/")
#
#     responce = requests.get(url, verify=False)
#     soup = BeautifulSoup(responce.text, "lxml")
#     return soup
#
# def get_all_courses():
#     result = []
#     data =  get_all_data ()
#     list_data = data.find_all('td')
#
#     for dt in list_data[1:]:
#         temp_data = dt.find_all('tr')
#         result.append(
#             {
#                 'code': temp_data[3].text.strip(),
#                 'union': temp_data[4].text.strip(),
#             }
#         )
#         print(temp_data)
#
#     return result
#
#
# def main():
#     get_all_courses()
#     with open('book.json', 'w', encoding='utf-8') as file:
#         json.dump( file, indent=4, ensure_ascii=False)
#
# url = "https://cbr.ru/currency_base/daily/"
#
# headers = dict(
#  accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9")
# req = requests.get(url, headers=headers)
# src= req.text
# print (src)
#
# with open("index.html","w") as file:
#      file.write(src)
with open("index.html") as file:
    src = file.read()

result = []
soup = BeautifulSoup(src, "lxml")
all_courses = soup.find_all("tr")

for tr in all_courses[1:]:
    courses_data = tr.find_all('td')

    result.append(
        {
            'code': courses_data[3].text.strip(),
            'union': courses_data[4].text.strip(),

        }
    )

print(result)
with open("result.json.json", "w", encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

result.jsonstr = '[{"a":1, "b":2}, {"c":3, "d":4}]'
aList = json.loads(result.jsonstr)
# print(aList[0]['b'])
print(type(aList))