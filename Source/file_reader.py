
from __future__ import print_function
from lexrankr import LexRank
import os
import json
import pandas as pd


def create_dic_file(BASE_DIR, target_category):
    if os.path.isfile(BASE_DIR+"\\"+target_category+".csv"):
        print("tttt")
        os.remove(BASE_DIR+"\\"+target_category+".csv")
    csv_file = open(BASE_DIR+"\\"+target_category+".csv", 'w')
    csv_file.write("test")
    csv_file.close

# Main start


dic_titles = []
dic_urls = []
dic_raw_contents = []
dic_summaries = []
dic_keywords = []
dic_locates = []
dic_scores = []

lexrank = LexRank()
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\resultdir"
dir_list = os.listdir(BASE_DIR)

for directory in dir_list:
    create_dic_file(BASE_DIR, directory)
    local_dir = BASE_DIR + "\\" + directory
    print(local_dir)
    file_list = os.listdir(local_dir)
    print(file_list)
    for file in file_list:
        print("\n\nFile:"+file+"\n\n")
        with open(local_dir+"\\"+file, encoding="utf-8-sig") as json_file:
            datas = json.load(json_file)
        json_file.close()
        print(datas)
        inted_contents = datas['contents']
        lexrank.summarize(inted_contents)
        summaries = lexrank.probe(None)
        print("\n\n 요약문 :::\n")
        for summary in summaries:
            print("\n" + summary)
            dic_titles.append(datas['title'])
            dic_urls.append(datas['href'])
            dic_raw_contents.append(datas['contents'])
            dic_summaries.append(summaries)
            keywords = ""
            locate = ""
            score = ""
            dic_keywords.append(keywords)
            dic_locates.append(locate)
            dic_scores.append(score)
    dic_frames = {"title": dic_titles, "url": dic_urls, "raw_contents": dic_raw_contents, "summary": dic_summaries, "keywords": dic_keywords, "locate": dic_locates, "score": dic_scores}
    dic = pd.DataFrame(dic_frames)
    print(dic)
        # data = {
        #     "title": datas['title'],
        #     "url": datas['url'],
        #     "raw_contents": datas['contents'],
        #     "summary": summaries,
        #     "keywords": "",
        #     'locate' : "",
        #     'score': ""
        # }
    

