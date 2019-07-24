from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
import json
import os



url = "https://blog.naver.com/PostView.nhn?blogId=jeju8253&logNo=221265912050&from=search&redirect=Log&widgetTypeCall=true&directAccess=false"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
temp = soup.select(".se_textView")

print(soup)

print("#######")
print(temp)
for a in temp:
    print(a.get_text())