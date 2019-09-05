#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import ast
import json
from konlpy.tag import Okt

string = "서울 여행"
okt = Okt()
word_dic = {}
for i in range(8):
    t = 0
    t = t+i+1
    fp = open(string+str(t)+".json", "r", encoding="utf-8-sig").read()

    atr = json.loads(fp)
    ts = atr['contents']

    # Text 가져오기 #

    

    # 선언부 #

    lines = ts.split("\n")


    for line in lines:
        print(line)
        malist = okt.pos(line)
        print(malist)
        for word in malist:
            if word[1]=="Noun":
                if not (word[0] in word_dic):
                    word_dic[word[0]] = 0
                word_dic[word[0]] +=1
    print("=======adadad======")
    print(word_dic)
    keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
    print("============")
    for word, count in keys[:50]:
        print("{0}({1})". format(word, count), end="")
    print()





    malist = okt.pos(ts, norm=True, stem=True)

    print(malist)