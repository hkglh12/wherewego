from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import os

def GetContent(targetlist):
    for target in targetlist:
        print(targetlist)
        print()
        print(target)
        url = target["link"]
        print(url)
        contentresponse = requests.get(url)
        Chtml = response.text
        Csoup = BeautifulSoup(Chtml, 'html.parser')


        print("<<<<<<<<<<<<<<<<<<<<<<<<<<DIVS")
        # a = Csoup.select("div", class_="se-main-container")
        a = Csoup.select("div", class_="se-component se-text se-l-default", id="SE-0acef6fc-5c7e-4699-83d9-3f298ddb077c")
        print("ONLY P")
        print(a)
       
        with open('result.json', 'w', encoding='utf-8') as file :
            json.dump(Csoup, file, ensure_ascii=False, indent='\t')
        # print("+++++++++++++++++++++++++++Csoup")
        # print(Csoup)
        # post = Csoup.find("div", {"id" : "se-main-container"})

        # print("/////////////////////////////////////////container")
        # print(post)
        #content = post.find("div", {"class": "se_component_wrap sect_dsc __se_component_area"})

        #target['things'] = content

        return targetlist

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
url = "https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%EC%97%AC%ED%96%89+%EC%B6%94%EC%B2%9C"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(response.text, 'html.parser')

targetarea = soup.select(".sh_blog_title")
resultlist = []

for target in targetarea:
    title = target.text
    link = target['href']
    result = {
            "title": title,
            "link": link,
            "things": "None yet"
        }
    resultlist.append(result)

docs = GetContent(resultlist)
print("FINAL RESULT")
print(docs)



# targetarea = soup.find_all("dl")
# # print(targetarea)
# print("=============================")
# print("=============================")
# print("=============================")

# for target in targetarea :
#     titles = target
#     # print(titles)
#     if 'href' in target.attrs :
#     #url = target.find("a", {"class" : "url"})
#         url = target.attrs['href']
#     print (titles , " : " , url)   #>>이거됌
#     print("=================================")





# my_titles = soup.select("dt")

# for title in my_titles :
#     print(title.text)


# my_titles = soup.select("dt")
# area = soup.find_all('dd', attrs={'class' : 'txt_block'})

# for target in area :
#     tef = target.find("a", pr{"class" :"url"})
#     print(tef)

# # print(area)
# data = {}

# for title in my_titles:
#     # Tag안의 텍스트
#     print(title.text)
#     # Tag의 속성을 가져오기(ex: href속성) 


# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)

# url = 'https://section.blog.naver.com/Search/Post.nhn'
# # hrd = {'User-Agent' : "Mozilla/5.0", "referer" : "http://naver.com"}
# # response = requests.get(url)
# # print(response)

# param = {
#     'pageNo' : 1,
    
#     'rangeType' : "ALL",
#     "orderBy" : "sim",
#     'keyword' : '여행 추천'
# }

# response = requests.get(url,params=param)
# html = response.text
# print(response)
# print(response.url)
# print(response.text)
# soup = BeautifulSoup(html, 'html.par ser')
# print(soup)





# targeturl = 'https://section.blog.naver.com/Search/Post.nhn'
# # targeturl = requests.get('https://section.blog.naver.com/Search/Post.nhn')
# hrd = {'User-Agent' : 'Mozilla/5.0', 'referer' : 'http://naver.com'}
# DIR = os.path.dirname(os.path.abspath(__file__))
# html = targeturl.text
# soup = BeautifulSoup(html, 'html.parser')


# param = {
#     "keyword" : "여행 추천"
# }

# response = requests.get(targeturl)
# print(response)
# soup = BeautifulSoup(response.text, 'html.parser', headers=hrd)

# area = soup.find("div", {"class":"blog section _blogBase"}).find_all("a", {"class" :"url"})

# for tag in area:
#     url_1 = tag.get('href')
#     print("{:}".format(url_1))


# print(body)
# titles = soup.select("dt")
# data = {}
# for title in titles :
#     print(title.text)
#     print(title.get('href'))
#     print(soup.select('div > div > div.info_post > div > a.desc_inner'))
#     print(soup.select("a"))
#     if 'href' in link.attrs: # 내부에 있는 항목들을 리스트로 가져옵니다 ex) {u'href': u'//www.wikimediafoundation.org/'}
#         print (link.attrs['href'])
#     data[title.text] = soup.select('a.desc_inner')

# # with open(os.path.join(DIR, 'result.json'), 'w+') as json_file:
# #     json.dump(data, json_file)
# #     #content > section > div.area_list_search > div:nth-child(1) > div > div.info_post > div > a.desc_inner