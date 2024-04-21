import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
data = pd.read_csv("D:/dissertation/data/profile_data3.csv")
data['citation_data'] = data['citation_data'].astype(object)
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

#b = webdriver.Chrome("C:/Users/Vidhi Bansal/Downloads/chromedriver_win32/chromedriver", chrome_options=options)
for i in range(len(data)):
        try:
            citation_count = data.iloc[i, 7]
            link = data.iloc[i, 6]
            citation_data=[]
            a=[]
            if citation_count<11:
                time.sleep(random.uniform(0,1))
                url = link
                # = webdriver.Chrome("C:/Users/Vidhi Bansal/Downloads/chromedriver_win32/chromedriver", chrome_options=options)
                #b.get(url)

                reqs = requests.get(link)
                s = BeautifulSoup(reqs.text, 'html.parser')
                for r2 in s.find_all('div', attrs={'class': 'gs_a'}):
                    time.sleep(random.uniform(0, 1))
                    r2 = re.sub("<div class=\"gs_a\">", "", str(r2))
                    r2 = re.sub('</div>', "", str(r2))
                    r2 = re.sub("<a[^>]*>", "", str(r2))
                    r2 = re.sub('</a>', "", str(r2))
                    k = []
                    a=[]
                    for auth in r2.split('-'):
                        k.append(auth)
                    if (len(k) > 1):
                        referencing_authors = k[0]
                        for auth in k[1].split(','):
                            a.append(auth)
                    citation_data.append(k[0])
                    citation_data.append(a)
            else:
                s1 = link
                s2 = 'cites='
                print(link)
                start = 0
                try:
                    no = s1[s1.index(s2) + len(s2):]

                    while start<(citation_count+10):
                        link = 'https://scholar.google.co.in/scholar?start=' + str(start) + '&hl=en&as_sdt=2005&sciodt=0,5&cites=' + str(no) + '&scipsc='
                        start = start + 10
                        time.sleep(random.uniform(0,1))
                        url=link
                        #b = webdriver.Chrome("C:/Users/Vidhi Bansal/Downloads/chromedriver_win32/chromedriver", chrome_options=options)
                        #b.get(url)
                        #reqs = requests.get(link)
                        #s = BeautifulSoup(b.page_source, 'html.parser')
                        reqs = requests.get(link)
                        s = BeautifulSoup(reqs.text, 'html.parser')
                        for r2 in s.find_all('div', attrs={'class': 'gs_a'}):
                         time.sleep(random.uniform(0, 1))
                         r2 = re.sub("<div class=\"gs_a\">", "", str(r2))
                         r2 = re.sub('</div>', "", str(r2))
                         r2 = re.sub("<a[^>]*>", "", str(r2))
                         r2 = re.sub('</a>', "", str(r2))
                         k=[]

                         a = []
                         for auth in r2.split('-'):
                             k.append(auth)
                         if (len(k) > 1):
                             referencing_authors = k[0]
                             for auth in k[1].split(','):
                                 a.append(auth)
                         citation_data.append(k[0])
                         citation_data.append(a)

                except Exception:
                                     continue
            print(citation_data)
            data.loc[i, 'citation_data'] =''
            data.at[i, 'citation_data'] = citation_data
            #time.sleep(random.uniform(300, 500))
        except Exception:
            continue
data.to_csv("D:/dissertation/data/profile_data5.csv",mode='a', index=False)