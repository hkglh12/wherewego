import urllib.request as req

from bs4 import BeautifulSoup
import requests
import json
import os
import time

user_input = input("키워드? :")
routine =  int(input("Routine?:"))
file_oper = user_input

try:
    if not os.path.exists("resultdir"):
        os.makedirs("resultdir")
    if not os.path.exists("resultdir\\"+user_input):
        os.makedirs("resultdir\\"+user_input)
except:
    print("Error in making dir")
    raise


BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\resultdir" + "\\" + user_input

rooturl = "https://search.naver.com/search.naver"

datalist = []
count = 0
start_time = time.time()
for i in range(routine):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>", i , "<<<<<<<<<<<<<<<<<<<<<<<<<<")
    params = {
        "where": "post",
        "query": user_input,
        "date_from": "20180101",
        "date_to": "20190605",
        "start": i * 10 + 1
    }
    print(params['start'])
    response = requests.get(rooturl, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')
    area = soup.select(".sh_blog_title")

    for target in area:
        url = target['href']
        if "blog.naver.com" not in url:
            print("not naver inclueded")
            continue
        else:
            data = {
                "title": target['title'],
                "href": target['href'],
                "contents": "NOT YET"
            }
            datalist.append(data)
    #############################1차 : 검색결과 긁어오기 ####################
    #############################네이버블로그만##############################
    for urlveri in datalist:
        html = requests.get(urlveri['href'])
        soup = BeautifulSoup(html.text, 'html.parser')
        area = soup.find(id="mainFrame")
        
        if area is not None:
            new_url = "https://blog.naver.com" + area.get('src')
        else:
            new_url = urlveri['href']
        
        urlveri['href'] = new_url

print("DONE")
# print(datalist)

############################URL가공까지 종료##########################
for target in datalist:
    pass
    print(target['href'] + '\t')
url = datalist[0]['href']
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# area = soup.find_all(".se-module se-module-text")
# print(area)
#############################성공코드
# res = req.urlopen(url)
# soup = BeautifulSoup(res, 'lxml')
# contents = soup.select(".se-main-container")

# text = ""
# for item in contents:
#     text += item.get_text()

# print(text)
#############################성공코드
for target in datalist:
    count+=1
    file_name = file_oper+str(count)
    content = ""
    url = target['href']
    try:
        response = requests.get(url)
        
    except:
        target['contents'] = "Problem in Getting Contents"
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        text = ""
        contents = soup.select(".se-main-container")

        if len(contents) !=0:
            print("OUT")
            for item in contents:
                text += item.get_text()
        else:
            print("IN")
            contents = soup.select(".postListBody")
            print(contents)
            for item in contents:
                text += item.get_text()
        target['contents'] = text
    with open(os.path.join(BASE_DIR, file_name), 'w+', encoding='UTF-8-sig') as json_file:
        json_file.write(json.dumps(target, ensure_ascii=False))
        json_file.close()
    print("본문 가공 완료 <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    

print('FIN')
print(datalist)