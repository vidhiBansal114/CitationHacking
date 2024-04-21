import requests
import re
from bs4 import BeautifulSoup
file1 = open("D:\dissertation\data\links\IJCSSE.txt","r+")
#file2=open("D:\dissertation\data\authors\IJACT_auth.txt","a")
file2 = open("D:\dissertation\data\links\IJCSSE author.txt","a")
# Print the extracted data
#print(remove_tags(HTML_DOC))
for url in file1.readlines():
    #print(link)

    reqs = requests.get('http://ijcsse.org/published/volume8/issue3/index.php')
    soup = BeautifulSoup(reqs.text, 'html.parser')
    print(soup)
    for row3 in soup.find_all('span',attrs={'class':'style7'}):

        print(row3)
        #urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(row3))
        row3 = re.sub("<div[^>]*>", "", str(row3))
        row3 = re.sub('</div>', "", str(row3))
        row3 = re.sub('\t', "", str(row3))
        row3 = re.sub('\n', "", str(row3))
        #row3 = re.sub(' ', "", str(row3))
        for auth in row3.split(','):
            print(auth)
            #file2.write(auth)
            #file2.write('\n')



