import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
options = webdriver.ChromeOptions()
b = webdriver.Chrome("C:/Users/Vidhi Bansal/Downloads/chromedriver_win32/chromedriver", chrome_options=options)
data = pd.read_csv("D:/dissertation/data/amity.csv")
for i in range(len(data)) :
    id=data.iloc[i, 1]
    name=data.iloc[i, 0]
    url='https://scholar.google.co.in/citations?user='+id+'&hl=en'
    print(url)
    #url='https://scholar.google.co.in/citations?user=CxAXrBoAAAAJ&hl=en'
    b = webdriver.Chrome("C:/Users/Vidhi Bansal/Downloads/chromedriver_win32/chromedriver", chrome_options=options)
    try:
        b.get(url)
        c = 0
        while c < 200:
            time.sleep(0.0011)
            try:
                btn = b.find_element_by_id('gsc_bpf_more')
                btn.click()
                c = c + 1
                #print('click')
            except NoSuchElementException:
                break
        doc = b.page_source
        b.close()
        soup = BeautifulSoup(doc, 'html.parser')

        #query = 'https://scholar.google.co.in/citations?user=CxAXrBoAAAAJ&hl=en'
        #reqs = requests.get(query)
        #soup = BeautifulSoup(reqs.text, 'html.parser')
        df = pd.DataFrame(columns=['Author_ID', 'Author_Name', 'Paper_Name', 'Paper_authors', 'Year of publication',
                                   'Journal of Publication', 'reference_link', 'Citation_count', 'Citation Information'])
        for r in soup.find_all('tr',attrs={'class':'gsc_a_tr'}):
         try:
            #print(r)
            paper = ''
            authors = ''
            citation_count = ''
            year = ''
            journal = ''
            link = ''
            citation_data = []
            for row1 in r('td',attrs={"class":"gsc_a_t"}):
                for row2 in row1.find_all('a',attrs={'class':'gsc_a_at'}):
                    row2 = re.sub("<a[^>]*>", "", str(row2))
                    row2 = re.sub('</a>', "", str(row2))
                    #print(row2)
                    paper=row2
                    time.sleep(0.001600)
                if(len(row1.find_all('div',attrs={'class':'gs_gray'}))>0):
                    row3 = row1.find_all('div',attrs={'class':'gs_gray'})[0]
                    row3 = re.sub("<div[^>]*>", "", str(row3))
                    row3 = re.sub('</div>', "", str(row3))
                    #print(row3)
                    authors=row3
                    time.sleep(.00200)
                if(len(row1.find_all('div',attrs={'class':'gs_gray'}))>1):
                    row3 = row1.find_all('div',attrs={'class':'gs_gray'})[1]
                    row3 = re.sub("<div[^>]*>", "", str(row3))
                    row3 = re.sub('</div>', "", str(row3))
                    row3 = re.sub("<span[^>]*>", "", str(row3))
                    row3 = re.sub('</span>', "", str(row3))
                    #print(row3)
                    l=[]
                    for auth in row3.split(','):
                        l.append(auth)
                    if(len(l)>1):
                        journal=l[0]
                        year=l[1]
                    time.sleep(.01600)
                for row in row1.find_all('div', attrs={'class': 'gs_gray'}):
                    for row3 in row.find_all('span',attrs={'class':'gs_oph'}):
                        row3 = re.sub("<span class=\"gs_oph\">,", "", str(row3))
                        row3 = re.sub(",", "", str(row3))
                        row3 = re.sub('</span>', "", str(row3))
                        year=row3
                        #print(row3)
                        time.sleep(.0500)
            l = []
            a=[]
            citation_data = []
            for row1 in r.find_all('td',attrs={"class":"gsc_a_c"}):
                for row2 in row1.find_all('a',attrs={'class':'gsc_a_ac gs_ibl'}):
                    link=row2.get('href')
                    s1 = link
                    s2 = 'cites='
                    print(link)
                    start = 0
                    #try:
                        #no = s1[s1.index(s2) + len(s2):]

                        #while start < 20:
                                    #link='https://scholar.google.co.in/scholar?start='+str(start)+'&hl=en&as_sdt=2005&sciodt=0,5&cites='+str(no)+'&scipsc='
                                    #start=start+10
                    row2 = re.sub("<a[^>]*>", "", str(row2))
                    row2 = re.sub('</a>', "", str(row2))
                                    #print(row2)
                    citation_count=row2
                    time.sleep(.06100)
                    url = link
                                    #reqs = requests.get(link)
                    '''
                                    s = BeautifulSoup(c.page_source, 'html.parser')
                                    #print(s)
                                    
                                    bt= c.find_element_by_class_name('recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox')
                                    bt.click()
                                    s = BeautifulSoup(link, 'html.parser')
                                    for r2 in s.find_all('div', attrs={'class': 'gs_a'}):
                                        print(r2)
                                        time.sleep(0.1)
                                        r2 = re.sub("<div class=\"gs_a\">", "", str(r2))
                                        r2 = re.sub('</div>', "", str(r2))
                                        r2 = re.sub("<a[^>]*>", "", str(r2))
                                        r2 = re.sub('</a>', "", str(r2))
                                        citation_data.append(r2)
                                        
                                        
                                        k=[]
                                        for auth in r2.split('-'):
                                            k.append(auth)
                                        print(k)
                                        if (len(k) > 1):
                                            referencing_authors = k[0]
    
                                            for auth in k[1].split(','):
                                                a.append(auth)
    
                                        citation_data.append(k[0])
                                        citation_data.append(a)
    
                                        l.append(r2)
                    '''


            df.loc[len(df.index)] = [id,name,paper,authors,year,journal,link, citation_count, citation_data]
         except Exception:
          continue
    except Exception:
        continue
    df.to_csv('D:/dissertation/data/profile_data_amity.csv', mode='a', index=False, header=False)
                #print(l[0])
                #print(a[0])
                #print(a[1])
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
'''
data = pd.read_csv("D:/dissertation/data/author id.csv")
for id in data['id']:
    query='https://scholar.google.co.in/citations?user='+id+'=en'
    reqs = requests.get(query)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for row1 in soup.find_all('div'):
        print(row1)
        time.sleep(1.600)
'''