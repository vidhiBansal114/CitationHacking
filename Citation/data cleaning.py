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
for i in range(len(data)):
    k=ast.literal_eval(data.loc[i,'citation_data'])

    author_dict = dict()
    author_self_dict = dict()
    c=0
    f=0
    total=0
    for j in k:


        if (c%2)==0:
            if isinstance(j, str) and j!='[]':
                #print(j)
                j = unescape_xml_entities(stripper.transformString(j))
                j=re.sub("<span[^>]*>", "", str(j))
                j = re.sub("</span[^>]*>", "", str(j))
                j = re.sub("â€", "", str(j))
                j = re.sub("</span[^>]*>", "", str(j))
                j = re.sub(r"\xa0", "", str(j))
                j = re.sub(r'\xa0â€', '', j)
                j = re.sub(r'[^\x00-\x7f]', '', j)
                j=" ".join(j.split())
                '''
                j=re.sub(r'[^\x00-\x7f]',r'', j)
                j = re.sub(r'[^\xa0]', r'', j)
                j = re.sub(r'â€', r'', j)
                j = re.sub(r'\xa0â€', r'', j)
                '''

                #print(j)
                for m in j.split(','):
                    m = unescape_xml_entities(stripper.transformString(m))
                    m=re.sub("<i[^>]*>", "", str(m))
                    m = re.sub("</i[^>]*>", "", str(m))
                    m=re.sub("<span[^>]*>", "", str(m))
                    m = re.sub("</span[^>]*>", "", str(m))
                    m = re.sub("â€", "", str(m))
                    m = re.sub("</span[^>]*>", "", str(m))
                    m = re.sub(r"\xa0", "", str(m))
                    m = re.sub(r'\xa0â€', '', m)
                    m = re.sub(r'[^\x00-\x7f]', '', m)
                    m=" ".join(m.split())

                    z=m.split(' ')

                    for x in authors_list:
                        yy=x.split(' ')
                        if len(z)>1:

                            if z[1] in yy and z[0][0] in yy:
                                f=1
                                if x in author_self_dict.keys():
                                    author_self_dict[x]=author_self_dict[x]+1
                                else:
                                    author_self_dict[x] = 1

                            elif len(z[0])>2:
                                if z[0] in yy and z[1][0] in yy:
                                    f=1
                                    if x in author_self_dict.keys():
                                        author_self_dict[x]=author_self_dict[x]+1
                                    else:
                                        author_self_dict[x] = 1

                    if len(z)>1:
                        if len(z[0])>2:
                            l_name=z[0]
                            f_name=z[1][0]
                        else:
                            l_name=z[1]
                            f_name=z[0][0]
                        author_name=f_name+' '+l_name
                    if m in author_dict.keys():
                        author_dict[m]=author_dict[m]+1
                    else:
                        author_dict[m]=1
        if f == 1:
            total = total + 1
            f = 0
        c=c+1


    data.loc[i, 'author_self_dict'] =''
    data.at[i, 'author_self_dict'] = author_self_dict
    data.loc[i, 'author_dict'] =''
    data.at[i, 'author_dict'] = author_dict
    data.loc[i, 'total_self_citation'] =''
    data.at[i, 'total_self_citation'] = total


data.to_csv("D:/dissertation/data/profile_data_self_citations2.csv",mode='a', index=False)
