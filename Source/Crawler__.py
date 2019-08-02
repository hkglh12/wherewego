from urllib.request import urlopen
from itertools import count
from collections import OrderedDict
from bs4 import BeautifulSoup
import requests
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
rooturl = "https://search.naver.com/search.naver"
hdr = {"User-Agent": "Mozilla/5.0", 'referer': 'http://naver.com'}

datalist = OrderedDict()
userinput = input("검색 키워드? :")
for page in count(1, 2):

    params = {
        "where": "post",
        "query": userinput,
        "date_from": "20180101",
        "date_to": "20190605",
        "start": (page-1) * 10 + 1
    }

    response = requests.get(rooturl, params=params, headers=hdr)

    soup = BeautifulSoup(response.text, 'html.parser')
    area = soup.select(".sh_blog_title")

    for target in area:
        url = target['href']
        if "daum" in url or "tistory" in url or "blog.me" in url:
            print("not naver searched")
            continue
        else:
            html_temp = requests.get(url)
            soup_temp = BeautifulSoup(html_temp.text, 'html.parser')
            area_temp = soup_temp.find(id='mainFrame')

            if area_temp is not None:
                data = {
                    "title": target['title'],
                    "href": "https://blog.naver.com" + area_temp.get('src'),
                    "content": "NOT YET",
                    "pending": "\t"
                }
            else:
                data = {
                    "title": target['title'],
                    "href": target['href'],
                    "content": "NOT YET",
                    "pending": "\t"
                }
    datalist.update(data)
    print("updating")
print("updatefinised")

for target in datalist:
    url = target['href']
    try:
        response = requests.get(url)
    except:
        target['content'] = "Problem Occured"
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        temp = soup.select(".se_textView")
        for a in temp:
            content += a.get_text()
        target["content"] = content
print("Crawling finished")
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(datalist, json_file, ensure_ascii=False)
