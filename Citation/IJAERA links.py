# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import requests
from bs4 import BeautifulSoup


url = 'http://www.jatit.org/volumes.php'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
file1 = open("D:\dissertation\data\links\JATIT.txt","a")
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))
    file1.write('http://ijettjournal.org'+str(link.get('href')))
    file1.write('\n')