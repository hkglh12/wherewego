from urllib.request import urlopen
from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
import json
import os
import time


def get_link(target, routine):
    for i in range(routine):
        print(i, "번째 Start (+10개단위)")
        url = "https://search.naver.com/search.naver"

        params = {
            "where": "post",
            "query" : target,
            "date_from": "20180101",
            "date_to": "20190101",
            "date_option" : '8',
            "start":(i-1) * 10 + 1
        }

        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        area = soup.select(".sh_blog_title")
        datalist = []
        for tag in area:
            modiurl = tag['href']
            data = {
                "title" : tag['title'],
                "href" : tag['href'],
                "content" : "NOT YET"
            }
            datalist.append(data)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>.1차가공종료")
    for target in datalist:
        url=target['href']
        html_temp = requests.get(url)
        soup_temp = BeautifulSoup(html_temp.text, 'html.parser')
        area_temp = soup_temp.find(id='mainFrame')
        if area_temp is not None:
            target['href'] = "https://blog.naver.com" + area_temp.get('src')
        else :
            target['href'] = "https://blog.naver.com" + target['href']
    print(">>>>>>>>>>>>>>>>>>>>>>>>>2차가공종료")
    return datalist

def get_content(datalist):
    for target in datalist:
        count += 1
        fileoper = str(count)
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
                content += a.get_text()

            target["content"] = content
        with open(os.path.join(BASE_DIR, fileoper), 'a+', encoding='UTF-8-sig') as json_file:
            json_file.write(json.dumps(datalist, ensure_ascii=False))
            json_file.close()


target = input("검색 키워드?:")
routine = int(input("Routine?:"))

try:
    if not os.path.exists("resultdir"):
        os.makedirs("resultdir")
except:
    print("Error in making dir")
    raise

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\resultdir"

count = 0
start_time = time.time()
pool = Pool(processes=16)
pool.map(get_content, get_link(target, routine))
print("FIN")
print("---- %s seconds ----" % (time.time()-start_time))