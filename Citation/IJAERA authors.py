import requests
import re
from re import search
from bs4 import BeautifulSoup
file1 = open("D:\dissertation\data\links\IJETT.txt","r+")
#file2=open("D:\dissertation\data\authors\IJACT_auth.txt","a")
file2 = open("D:\dissertation\data\links\galgotia authors.txt","a")
# Print the extracted data
#print(remove_tags(HTML_DOC))

#for url in file1.readlines():

    #print(url)

reqs = requests.get('https://www.galgotiasuniversity.edu.in/school-engineering-technology-socse-cse-faculty.asp')
soup = BeautifulSoup(reqs.text, 'html.parser')
    #print(soup)
    #for row1 in soup.find_all('td'):
for row3 in soup.find_all('td'):

    for a in row3.find_all('a'):
            a = re.sub("<a[^>]*>", "", str(a))
            a = re.sub('</br>', "", str(a))
            a = re.sub('</a>', "", str(a))
            print(a)

            file2.write(a)
            file2.write('\n')



