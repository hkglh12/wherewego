from __future__ import print_function
# from lexrankr import LexRank
from konlpy.tag import *

import os
import json
import pandas as pd


def create_dic_dir(base_directory):
    dic_directory_path = base_directory+"\\dic_dir"
    if not os.path.exists(dic_directory_path):
        print("Create dic dir")
        os.mkdir(dic_directory_path)
    return dic_directory_path

# Main start

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
result_root_dir = BASE_DIR+"\\resultdir"
dictionary_directory_path = create_dic_dir(BASE_DIR)
result_list = os.listdir(BASE_DIR+"\\resultdir")
okt = Okt()
kkma = Kkma()
# Kkma 활용 : https://ssoonidev.tistory.com/88
for result_directory in result_list:
    dic_titles = []
    dic_urls = []
    dic_raw_contents = []
    dic_summaries = []
    dic_keywords = []
    dic_locates = []
    dic_scores = []

    target_category_path = result_root_dir+"\\"+result_directory
    category_file_list = os.listdir(target_category_path)

    for file in category_file_list:
        target_file = target_category_path+"\\"+file
        print("target file:" + target_file)
        with open(target_file, encoding="utf-8-sig") as json_file:
            file_datas = json.load(json_file)
        json_file.close()
        print(file_datas['contents'])
        target_contents_nouns = kkma.nouns(file_datas['contents'])
        print(target_contents_nouns)
        
        dic_titles.append(file_datas['title'])
        dic_urls.append(file_datas['href'])
        dic_raw_contents.append(file_datas['contents'])
        dic_summaries.append("")
        dic_keywords.append(target_contents_nouns)
        dic_locates.append("")
        dic_scores.append("")
    dic_frames = {
        "title": dic_titles,
        "url": dic_urls,
        "raw_contents": dic_raw_contents,
        "summary": dic_summaries,
        "keywords": dic_keywords,
        "locate": dic_locates,
        "score": dic_scores
    }
    dic = pd.DataFrame(dic_frames)
    print(dic)
    # pandas dataframe to csv : https://buttercoconut.xyz/74/
    dic.to_csv(dictionary_directory_path+"\\"+result_directory+".csv", mode='w', encoding="utf-8-sig")