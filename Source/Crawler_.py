from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url = "https://search.naver.com/search.naver"
target = input("검색 키워드?:")
params = {
    "where": "post",
    "query" : target,
    "date_from": "20180101",
    "date_to": "20190101",
    "date_option" : '8'
}

###################################1차가공

response = requests.get(url, params=params)
soup = BeautifulSoup(response.text, 'html.parser')

area = soup.select(".sh_blog_title")
datalist = []
for tag in area:
    # print(tag['title'])
    # print(tag['href'])
    modiurl = tag['href']
    data = {
        "title" : tag['title'],
        "href" : tag['href'],
        "content" : "NOT YET"
    }
    datalist.append(data)

print("resultdict")
print(datalist)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>.1차가공종료")
###################################################2차가공부
for target in datalist:
    url=target['href']
    html_temp = requests.get(url)
    soup_temp = BeautifulSoup(html_temp.text, 'html.parser')
    area_temp = soup_temp.find(id='mainFrame')
    if area_temp is not None:
        target['href'] = "https://blog.naver.com" + area_temp.get('src')
        # print("modified addr\n")
        # print(target['href'])
    else :
        target['href'] = "https://blog.naver.com" + target['href']
        # print("NonModified")
        # print(target['href'])

####################################################2차가공 종료

for target in datalist:
    content = " "
    url = target['href']
    try:
        response = requests.get(url)
    except:
        target['content'] = "blog.naver.com/ 형식이 아님. 현재내용을 읽어올 수 없음."
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        temp = soup.select(".se_textView")
        for a in temp:
            print(a.get_text())
            content += a.get_text()

        target["content"] = content
print(datalist)
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(datalist, json_file, ensure_ascii=False)

