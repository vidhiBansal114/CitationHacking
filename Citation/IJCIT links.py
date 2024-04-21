# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


url = 'http://ijcsn.org/publications.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
file1 = open("D:\dissertation\data\links\IJCSSE.txt","a", encoding='utf-8')
#for k in soup.find_all('font'):

import re
file2 = open("D:\dissertation\data\links\IJCSSE author.txt","a")

for link in soup.find_all('a'):
        numbers = []
        k=str(link.get('href'))
        print(k)
        temp = re.findall(r'\d+', k)
        res = list(map(int, temp))
        print(res)
        if(len(res)>1 and res[0] not in [8,4] and res[1] not in [5,3]):
                url='http://ijcsse.org/published/volume'+str(res[0])+'/issue'+str(res[1])+'/index.php'
                reqs = requests.get(url)
                soup = BeautifulSoup(reqs.text, 'html.parser')

                for row1 in soup.find_all('span', attrs={'class': 'style7'}):
                        for row3 in row1.find_all('font'):
                                print(row3)
                                row3 = re.sub("<font[^>]*>", "", str(row3))
                                row3 = re.sub('</font>', "", str(row3))
                                row3 = re.sub('\t', "", str(row3))
                                row3 = re.sub('\n', "", str(row3))
                                #row3 = re.sub(' ', "", str(row3))
                                for auth in row3.split(','):
                                    print(auth)
                                    file2.write(auth)
                                    file2.write('\n')



