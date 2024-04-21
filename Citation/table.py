import json

import numpy
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
# importing the required module
import matplotlib.pyplot as plt
import string
import seaborn as sns
unescape_xml_entities = lambda s: unescape(s, {"&apos;": "'", "&quot;": '"', "&nbsp;":" "})

stripper = (anyOpenTag | anyCloseTag).suppress()

#print(unescape_xml_entities(stripper.transformString(source)))
data = pd.read_csv(r"D:\\dissertation\\data\\profile_data_self_citations2.csv",encoding='ISO-8859-1')
author_first_name=''
total=0
li=[]
c=0
kk=[]
k=1
for i in range(len(data)):
    k=data.loc[i, 'total citations']
    m=data.loc[i, 'year']
    if k==1:
        if(m>0):
            kk.append(m)
            print(m)
            c=c+1
data=numpy.array(kk)
sns.distplot(data,bins=np.arange(data.min(), data.max()+1),kde=False,hist_kws={"align" : "left"})
x=[53,58,59,72]
y=[1,1,3,2]
#plt.bar(x,y)
#plt.xlim([0,60])
#plt.xticks([50,53,55,58,59,60,70,72])
plt.xlabel("Total citations")
plt.ylabel("Frequency")
plt.title("Frequency distribution >=30 % and <50% self citations", fontsize=7)
#plt.savefig("D:\\dissertation\\data\\Frequency distribution of greater than 30 % self citations.png",dpi=300)
plt.show()
print(c)