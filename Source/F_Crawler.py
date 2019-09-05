from bs4 import BeautifulSoup
import requests
import json
import os
import time
import sys
import re


def CreateDirectory(user_input):
    try:
        if not os.path.exists("resultdir"):
            os.makedirs("resultdir")
        if not os.path.exists("resultdir\\"+user_input):
            os.makedirs("resultdir\\"+user_input)
    except Exception as e :
        print(f"Error in making dir : {e}")
        sys.exit(1)


def URLCrawler(data_list, root_url, i):
    print("start", i, "th Base Crawl")
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
        if "blog.naver.com" not in url:
            print("not naver inclueded")
            continue
        else:
            html = requests.get(target_post['href'])
            soup = BeautifulSoup(html.text, 'lxml')
            area = soup.find(id="mainFrame")

            if area is not None:
                new_url = "https://blog.naver.com" + area.get('src')
            else:
                new_url = url
            data = {
                "title": target_post['title'],
                "href": new_url,
                "contents": "NOT YET"
            }
            datalist.append(data)
    print("finish", i, "th Base Crawl")
    return datalist


def ContentsCrawler(url_list, i, file_oper, BASE_DIR, user_input):
    re_imoji_ptn = re.compile(
        "["u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        "]+", flags=re.UNICODE
    )

    count = 0
    print("start", i, "th contents Crawl")
    BASE_DIR = os.path.dirname(
            os.path.abspath(__file__)
        ) + "\\resultdir" + "\\" + user_input

    for target in url_list:
        count += 1
        file_name = file_oper + str(i*10 + count) + ".json"
        content = ""
        try:
            response = requests.get(target['href'])
        except Exception as e:
            print(f"{e}")
            target['contents'] = ""
        else:
            soup = BeautifulSoup(response.text, 'lxml')
            mainblock = soup.select(".se-main-container")

            if len(mainblock) != 0:
                for item in mainblock:
                    remove_imoji = re.sub(re_imoji_ptn, '', item.get_text())
                    remove_exc_enter = re.sub(
                        '\n+\n\0+\n\0\0+', '\n', remove_imoji
                    )
                    content += re.sub(
                        '[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》;]',
                        '',
                        remove_exc_enter
                    )
                target['contents'] = content

                with open(
                    os.path.join(BASE_DIR, file_name), 'w+', encoding='UTF-8-sig'
                ) as json_file:
                    json_file.write(json.dumps(target, ensure_ascii=False))
                    json_file.close()
            else:
                target['href'] = target['href'][:8] + "m." + target['href'][8:]
                response = requests.get(target['href'])
                soup = BeautifulSoup(response.text, 'lxml')
                mainblock = soup.select(".post_ct  ")
                if len(mainblock) != 0:
                    for item in mainblock:
                        remove_imoji = re.sub(re_imoji_ptn, '', item.get_text())
                        remove_exc_enter = re.sub(
                            '\n+\n\0+\n\0\0+', '\n', remove_imoji
                        )
                        content += re.sub(
                            '[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》;]',
                            '',
                            remove_exc_enter
                        )
                    target['contents'] = content
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
print("Used Time : " , time.time() - start_time, " sec ")
print('FIN')
