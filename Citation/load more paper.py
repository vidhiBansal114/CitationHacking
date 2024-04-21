import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

start=10
#url='https://scholar.google.co.in/scholar?start=10&hl=en&as_sdt=2005&sciodt=0,5&cites=15460634098026837122&scipsc=
url='https://scholar.google.co.in/scholar?start=0&hl=en&as_sdt=2005&sciodt=0,5&cites=15460634098026837122&scipsc='

c=0
url = 'https://scholar.google.com/citations?user=yeEjlCYAAAAJ&hl=en'
        #url = 'https://scholar.google.co.in/scholar?oi=bibs&hl=en&oe=ASCII&cites=15460634098026837122'
        #url = 'https://scholar.google.co.in/scholar?start='+str(start)+'&hl=en&as_sdt=2005&sciodt=0,5&cites=15460634098026837122&scipsc='
reqs = requests.get(url)
start=0
soup = BeautifulSoup(reqs.text, 'html.parser')
for i in ['f']:
    time.sleep(1)
    try:

        # print(soup)
        l = []
        a = []
        citation_data = []
        #print(soup)
        for r in soup.find_all('tr', attrs={'class': 'gsc_a_tr'}):
          for row1 in r.find_all('td', attrs={"class": "gsc_a_c"}):

            for row2 in row1.find_all('a', attrs={'class': 'gsc_a_ac gs_ibl'}):
                link = row2.get('href')
                print(link)
                s1=link
                s2='cites='
                try:
                        no=s1[s1.index(s2) + len(s2):]
                        while start < 20:
                                link='https://scholar.google.co.in/scholar?start='+str(start)+'&hl=en&as_sdt=2005&sciodt=0,5&cites='+str(no)+'&scipsc='
                                start=start+10
                                row2 = re.sub("<a[^>]*>", "", str(row2))
                                row2 = re.sub('</a>', "", str(row2))
                                #print(row2)
                                citation_count = row2
                                time.sleep(.2600)
                                url = link
                                reqs = requests.get(link)
                                s = BeautifulSoup(reqs.text, 'html.parser')
                                #print(link)
                                #print(s)
                                for r2 in s.find_all('div', attrs={'class': 'gs_a'}):
                                    #print(r2)
                                    time.sleep(1.1)
                                    r2 = re.sub("<div class=\"gs_a\">", "", str(r2))
                                    r2 = re.sub('</div>', "", str(r2))
                                    r2 = re.sub("<a[^>]*>", "", str(r2))
                                    r2 = re.sub('</a>', "", str(r2))
                                    #print(r2)
                                    k=[]
                                    for auth in r2.split('-'):
                                        k.append(auth)
                                        #print(auth)
                                    #print(l)

                                    if (len(k) > 1):
                                        referencing_authors = k[0]
                                        #print(referencing_authors)

                                        for auth in k[1].split(','):
                                            a.append(auth)

                                        # referencing_journal = a[0]

                                        # referencing_year = a[1]
                                    citation_data.append(k[0])
                                    citation_data.append(a)
                                    l.append(k)
                except Exception:
                             continue
        print(l)

    except NoSuchElementException:
                break
                           