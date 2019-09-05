#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import ast
import json
from konlpy.tag import Okt
from konlpy.tag import Kkma
string = "서울 여행"
okt = Okt()
word_dic = {}

fp = open("서울 여행1.json", "r", encoding="utf-8-sig").read()

atr = json.loads(fp)
ts = atr['contents']


lines = ts.split("\n")
new = ""
#target_string = "오늘따라 서울여행이 떙겨서 다녀와봤어요\n 서울에는 많은게 있더라구요 \n 그중에서도 저는 광화문에 다녀왔습니다 \n 휴..광화문 스타벅스는 언제봐도 사람이 정말 많아요\n 스타벅스에서 아메리카노 한잔 마시고 경복궁으로 들어갔습니다\n 한복은 언제봐도 반짝반짝하네요 ㅎㅎ \n 그뒤에 저는 아내와 함께 제주도 밀면국수집 다녀왔어요 ㅎㅎ \n 비빔국수가 일품인 곳 이에요"
for line in lines:
    if line == "\n":
        line.replace("\n", "\t")
        new.append(line)
target_string = new.split("\n")

for line in target_string:
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





malist = okt.pos(target_string, norm=True, stem=True)

print(malist)