from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import os

url = "https://search.naver.com/search.naver"

params = {
    "where": "post",
    "query" : "여행 추천",
    "date_from": "20180101",
    "date_to": "20190101",
    "date_option" : '8'
}

response = requests.get(url, params=params)
soup = BeautifulSoup(response.text, 'html.parser')

area = soup.select(".sh_blog_title")

for tag in area:
    print(tag['href'])