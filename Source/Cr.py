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

datalist = []
user_input = input("키워드? :")

params = {
    "where": "post",
    "query": user_input,
    "date_from": "20180101",
    "date_to": "20190605",
    "start": 1
}

response = requests.get(rooturl, params=params, headers=hdr)

soup = BeautifulSoup(response.text, 'html.parser')
area = soup.select(".sh_blog_title")

for target in area:
    url = target['href']
    if "blog.naver.com" not in url :
        print("not naver inclueded")
        continue
    else:
        data = {
            "title": target['title'],
            "href": target['href'],
            "contents": "NOT YET"
        }
        datalist.append(data)

print("Finished")
print(datalist)
content = ""
for target in datalist:
    thtml = requests.get(target['href'])
    tsoup = BeautifulSoup(thtml.text, 'html.parser')
    tarea = tsoup.find(id="mainFrame")
    print(tarea)
    if tarea is not None:
        #print(tarea.get('src'))
        url = "https://blog.naver.com" + tarea.get('src')
        print(url)
        try:
            html_temp = requests.get(url)
            print(html_temp)
        except:
            target['contents'] = "E"
        else:
            soup_temp = BeautifulSoup(html_temp.text, 'html.parser')
            area_temp = soup_temp.select(".se_textView")
            print(area_temp)
            for a in area_temp:
                print(a.get_text())
                content+= a.get_text()
            target["contents"] = content
            target["href"] = url
    # if tarea is None:
    #     print("none")
    #     context = tsoup.select(".se_textview")
    #     for a in context:
    #         target['contents'] += a
    # else:
    #     print("else")
    #     url = "https://blog.naver.com"+tarea.get('src')
    #     try:
    #         response = requests.get(url)
    #     except:
    #         target['contents'] = "ERROR"
    
    #     csoup = BeautifulSoup(response.text, 'html.parser')
    #     ctarget = csoup.select(".se_textView")
    #     for a in ctarget:
    #         print(a.get_text())
    #         target['contents'] += a.get_text()
print("Crawling Finished\t")
print(datalist)