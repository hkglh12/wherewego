from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
import json
import os
import time

user_input = input("검색키워드 ?:")
routine = int(input("Routine?:"))
file_oper = user_input
datalist = []
try:
    if not os.path.exists("resultdir"):
        os.makedirs("resultdir")
    if not os.path.exists("resultdir\\"+user_input):
        os.makedirs("resultdir\\"+user_input)
except:
    print("Error in making dir")
    raise

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\resultdir" + "\\" + user_input
BASE_URL = "https://search.naver.com/search.naver"

start_time = time.time()
count = 0
for i in range(routine):
    print(i, "번째 단위")
    
    params = {
        "where": "post",
        "query" : user_input,
        "date_from": "20180101",
        "date_to": "20190101",
        "date_option" : '8',
        "start":(i-1) * 10 + 1
    }

    response = requests.get(BASE_URL, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    area = soup.select(".sh_blog_title")
    for tag in area:
        URL = tag['href']
        print(URL)

        if "blog.naver.com" not in URL:
            print("not naver : " + URL)
            continue
        else:
            data = {
                "title": tag['title'],
                "href": tag['href'],
                "content": "NOT YET"
            }
            datalist.append(data)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>1차가공종료")

    for target in datalist:
        modiurl = target['href']
        html = requests.get(modiurl)
        soup = BeautifulSoup(html.text, 'html.parser')
        area = soup.find(id='mainFrame')

        if area is not None:
            target['href'] = "https://blog.naver.com" + area.get('src')
        else :
            target['href'] = "https://blog.naver.com" + modiurl
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>URL 가공종료")

    for target in datalist:
        count+=1
        file_name = file_oper + str(count)
        contents = " "
        url = target['href']

        try:
            response = requests.get(url)
        except:
            target['content'] = "E"
            print("problem in get")
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            contents_area = soup.select(".se_textView")
            for a in contents_area:
                contents += a.get_text()

            target["content"] = contents
        
        with open(os.path.join(BASE_DIR, file_name), 'a+', encoding='UTF-8-sig') as json_file:
            json_file.write(json.dumps(datalist, ensure_ascii=False))
            json_file.close()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>데이터 가공 종료")
print("FIN")
print("---- %s seconds ----" % (start_time - time.time()))