import json

import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
import ast
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from pyparsing import anyOpenTag, anyCloseTag
from xml.sax.saxutils import unescape as unescape
import string
unescape_xml_entities = lambda s: unescape(s, {"&apos;": "'", "&quot;": '"', "&nbsp;":" "})

stripper = (anyOpenTag | anyCloseTag).suppress()

#print(unescape_xml_entities(stripper.transformString(source)))
data = pd.read_csv(r"D:\\dissertation\\data\\profile_data_self_citations.csv",encoding='ISO-8859-1')
author_first_name=''
total=0
li=[]
for i in range(len(data)):
    c=0
    try:
        c=0
        k=ast.literal_eval(data.loc[i,'author_dict'])
        #print(k)
        m=data.loc[i, 'author_dict']
        t=m=data.loc[i, 'total citations']
        #print(m)
        authors = data.loc[i, 'authors']
        authors_list = []

        for author in authors.split(','):
                author = " ".join(author.split())
                authors_list.append(author)

        i=0
        #print(m)
        for x in authors_list:
            yy = x.split(' ')
            #print(yy)
            #if len(yy)>1:
            authors_list[i]=yy[0][0]+' '+yy[1]
            #print(authors_list[i])
            i=i+1
        #print(m)
        #k = ast.literal_eval(data.loc[i, 'author_dict'])
        #print(k)
        c=0
        for y in k:
                #print(y)
                xx=y.split(' ')
                xxx=xx[0][0]+' '+xx[1]
                #print(xxx)
                if k[y]>=0.2*(float(t)) and k[y]<0.5*(float(t)) and xxx not in authors_list and t>=5:
                    print(y)
                    c=c+1



        print(c)
        li.append(c)
        data.loc[i, 'retitive_cit_without_author having more than 80 % citations'] = ''

        data.loc[i, 'retitive_cit_without_author having more than 80 % citations'] = c
        #data.to_csv("D:/dissertation/data/profile_data_self_citations3.csv", mode='a', index=False)
    except Exception:
        li.append(c)
        continue
df = pd.DataFrame(li)
df.to_csv("D:/dissertation/data/profile_data_self_citations3.csv",mode='a',index=False)