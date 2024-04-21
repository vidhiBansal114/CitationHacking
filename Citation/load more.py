import numpy as np
import requests
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
options=Options()
b=webdriver.Chrome("C:/Users/Vidhi Bansal/Downloads/chromedriver_win32/chromedriver",options=options)
url='https://scholar.google.co.in/citations?user=CxAXrBoAAAAJ&hl=en'
b.get(url)
c=0
while c<10:
    time.sleep(1)
    try:
        btn=b.find_element_by_id('gsc_bpf_more')
        btn.click()
        c=c+1
        print('click')
    except NoSuchElementException:
        break
doc=b.page_source
#print('click')
b.close()
#print('closed')

soup = BeautifulSoup(doc, 'html.parser')
print(soup)
for r in soup.find_all('tr',attrs={'class':'gsc_a_tr'}):
        for row1 in r('td',attrs={"class":"gsc_a_t"}):
            for row2 in row1.find_all('a',attrs={'class':'gsc_a_at'}):
                row2 = re.sub("<a[^>]*>", "", str(row2))
                row2 = re.sub('</a>', "", str(row2))
                print(row2)
                #paper=row2
                time.sleep(0.1600)