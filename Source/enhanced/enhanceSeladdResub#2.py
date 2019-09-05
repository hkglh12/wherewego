import urllib.request as req

from bs4 import BeautifulSoup
import requests
import json
import os
import time
import sys
import re


# 결과를 저장할 최상위 폴더를 만듭니다.
def CreateDirectory(user_input):
    try:
        if not os.path.exists("resultdir"):
            os.makedirs("resultdir")
        if not os.path.exists("resultdir\\"+user_input):
            os.makedirs("resultdir\\"+user_input)
    except:
        print("Error in making dir")
        sys.exit(1)


# 본문을 가져오기 위해 포스트에 해당하는 URL을 가져오고
# 만약 그 URL이 본문을 가져오기 위해 동적으로 다른곳으로 리다이렉트된다면
# 해당 URL을 저장합니다.
def URLCrawler(data_list, root_url, i):
    print(i, "번째 URL Crawling Start")
    params = {
        "where": "post",
        "query": user_input,
        "date_from": "20160101",
        "date_to": "20190605",
        "st": "sim",
        "start": i * 10 + 1
    }

    response = requests.get(root_url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    area = soup.select(".sh_blog_title")

    for target_post in area:
        url = target_post['href']
        # 만약 URL이 naver 예하가 아니라면 태그가 달라지기 때문에
        # 망설임 없이 스킵합니다.
        if "blog.naver.com" not in url:
            print("not naver inclueded")
            continue
        # URL이 blog.naver 예하라면 그곳으로 접속해봅니다
        else:
            html = requests.get(target_post['href'])
            soup = BeautifulSoup(html.text, 'lxml')
            area = soup.find(id="mainFrame")
            # 만약 본문 소스에 mainFrame이 있다면 다른곳으로 redirect하게됩니다.
            # 따라서 mainFrame을 담은 area가 None이 아니라면

            if area is not None:
                new_url = "https://blog.naver.com" + area.get('src')

            # redirect 된다고 판단하고, 아니라면 원본 URL을 본문을 긁어올 대상으로 지정합니다.
            else:
                # 수정 사항 : 원래는 urlveri['href'] 였음. 못가져온다면 이부분을 중심으로 분석
                new_url = url
            data = {
                "title": target_post['title'],
                "href": new_url,
                "contents": "NOT YET"
            }
            datalist.append(data)
    print(i, "번째 URL Crawling End")
    # 이 datalist가 ContentsCrawler에서 url_list로 쓰입니다. 아직 Url 만 담고있어서요
    return datalist


# 각 Post의 실 내용을 긁어오는 부분입니다.
def ContentsCrawler(url_list, i, file_oper, BASE_DIR, user_input):
    print(i, "번째 URL Contents Start")
    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    ) + "\\resultdir" + "\\" + user_input
    count = 0

    for target in url_list:
        count += 1
        file_name = file_oper + str(i*10 + count) + ".json"
        content = ""

        try:
            response = requests.get(target['href'])
        except:
            target['contents'] = " "
        else:
            # lxml이 파싱 속도가 빠르대서 lxml 씁니다.
            soup = BeautifulSoup(response.text, 'lxml')
            text = ""
            # post의 실 내용을 담고있는 mainblock을 가져옵니다.
            mainblock = soup.select(".se-main-container")

            if len(mainblock) != 0:
                # 일단 특수문자들을 제거합니다.
                for item in mainblock:
                    #remove_sp = re.sub('(^\0\W+)', '', item.get_text())
                    removeenter = re.sub('\n+', '\n',item.get_text())
                    
                    content += re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》;]', '', removeenter)
                    
                target['contents'] = content

                with open(os.path.join(BASE_DIR, file_name), 'w+', encoding='UTF-8-sig') as json_file:
                    json_file.write(json.dumps(target, ensure_ascii=False))
                    json_file.close()    
            else:
                target['href'] = target['href'][:8] + "m." + target['href'][8:]
                response = requests.get(target['href'])
                soup = BeautifulSoup(response.text, 'lxml')
                mainblock = soup.select(".post_ct  ")
                if len(mainblock) != 0:
                    for item in mainblock:
                        text += re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》;]', '', item.get_text())
                    target['contents'] = text
                    with open(os.path.join(BASE_DIR, file_name), 'w+', encoding='UTF-8-sig') as json_file:
                        json_file.write(json.dumps(target, ensure_ascii=False))
                        json_file.close()
                else:
                    print("Can't Crawl Contents")
                    continue
    print(i, "번째 Contents Crawling Ended")
    return url_list

user_input = input("키워드? :")
routine = int(input("Routine?:"))
file_oper = user_input
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\resultdir" + "\\" + user_input

count = 0

root_url = "https://search.naver.com/search.naver"
CreateDirectory(user_input)


start_time = time.time()

for i in range(routine):
    datalist = []
    url_list = URLCrawler(datalist, root_url, i)
    datalist = ContentsCrawler(url_list, i, file_oper, BASE_DIR, user_input)
print("Used Time : " , time.time() - start_time , " sec ")
print('FIN')
