import requests
import re
from re import search
from bs4 import BeautifulSoup
file1 = open("D:\dissertation\data\links\IJMRD.txt","r+")
#file2=open("D:\dissertation\data\authors\IJACT_auth.txt","a")
file2 = open("D:\dissertation\data\links\IJMRD authors.txt","a")
# Print the extracted data
#print(remove_tags(HTML_DOC))
for url in file1.readlines():
    #print(link)

    reqs = requests.get('http://www.allsubjectjournal.com/archives/2021/vol8/issue1')
    soup = BeautifulSoup(reqs.text, 'html.parser')
    #print(soup)
    for row1 in soup.find_all('td'):
       c=0
       for row3 in row1.find_all('div',attrs={'class':'body'}):
           c=c+1
           if(c==2):
                #print(row3)
           #if search('\n<em>Author</em>:',str(row3)):
                #k=re.search('\n<em>Author</em>:', str(row3)).span()[1]
                #print(row3)
                row3=str(row3)
                #row3 = row3[k::]
                # print(row3)
                #urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(row3))
                row3 = re.sub("<div[^>]*>", "", str(row3))
                row3 = re.sub("<div class=\"body\">", "", str(row3))
                row3 = re.sub("<div class=\"body\">*", "", str(row3))
                row3 = re.sub("<span style=\"color: #800000;\">*", "", str(row3))
                row3 = re.sub("<span style=\"color: #800000;\"> \(Author\'s:*", "", str(row3))
                row3 = re.sub("<span lang=\"EN-IN\">*", "", str(row3))
                row3 = re.sub("a href=\":*", "", str(row3))
                row3 = re.sub("\(</a>Author's:*", "", str(row3))
                row3 = re.sub('</div>', "", str(row3))
                #row3 = re.sub('*</div>', "", str(row3))
                row3 = re.sub('<span> \(Author\'s:', "", str(row3))
                row3=re.sub('<span>\(Author\'s:','',str(row3))
                row3 = re.sub('\)', "", str(row3))
                row3 = re.sub('\n', "", str(row3))
                row3=re.sub('\(Author\'s:','',str(row3))
                row3=re.sub('</a>*','',str(row3))
                row3=re.sub('</Volume 2/Issue 5/IJESIT201305_61.pdf"> </a>','',str(row3))
                row3=re.sub('&;','',str(row3))
                #row3 = re.sub(' ', "", str(row3))
                for auth in row3.split(','):
                    print(auth)
                    try:
                    #for a in auth.split('and')
                        file2.write(auth)
                        file2.write('\n')
                    except:
                        continue



