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
userinput = input("검색 키워드? :")

for page in count(1,10):
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