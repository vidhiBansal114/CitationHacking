import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
import numpy as np
goog_search ='https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=niyati+baliyan&btnG='
#r = requests.get(goog_search)

#soup = BeautifulSoup(r.text, "html.parser")
#k=re.search('user=', str(soup)).span()[1]
#soup=str(soup)
#soup=soup[k::]
#print(soup[0:12])
#journals=['IJACT','IJAera','IJCIT','IJCSSE']
#journals=['ijesi']
#journals=['IJMRD']
journals=['ipu']
dict={'Name':[],'id':[]}

df = pd.DataFrame(dict)
for jname in journals:
    file_name=jname+' authors.txt'
    file = open("D:/dissertation/data/authors/"+file_name, "r+")
    for author in file.readlines():
        try:
            #print(author)
            author=" ".join(author.split())
            query=''
            for auth in author.split(' '):
                #print(auth)
                query=query+'+'+str(auth)
            #print(query)
            if(query[0]=='+'):
                query=query[1::]
            #print(query)

            goog_search = 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors='+query+'&btnG='
            r = requests.get(goog_search)

            soup = BeautifulSoup(r.text, "html.parser")
            #print(soup)
            if(str(soup)!=''):
                k = re.search('user=', str(soup)).span()[1]
                soup = str(soup)
                soup = soup[k::]
                id=soup[0:12]
                print(soup[0:12])
                if(soup[0:12]!=''):
                    df.loc[len(df.index)] = [author,id]
                    time.sleep(.600)

        except:
            continue
print(df)
df.to_csv('D:/dissertation/data/ipu.csv')
