#python 3.7

import re
import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

chromePath = './chromedriver'
url = 'http://acm.cqu.edu.cn/contest_show.php?cid=243#status'



driver = webdriver.Chrome(chromePath)
driver.get(url)
time.sleep(1)
elements = driver.page_source
soup = BeautifulSoup(elements,'html.parser')

html = soup.prettify()

html=html.replace('\n','')

arr = re.findall(r'<tr>.*</tr>',html)

for i in arr:
    html = html.replace(i,'')

arr = re.findall(r'<tr class="odd">.+</tr>',html)

files = open('.\log.html','wb')


data = ''
for i in arr:
    data=data+i
#    files.write(i.encode('utf-8'))

data = BeautifulSoup(data,'html.parser')

files.write(data.prettify().encode('utf-8'))
files.close()

arr.clear()


for ch in data.descendants:
    print(ch)
    if ch.name is None:
        continue
    print(len(ch.contents))
    if(len(ch.contents)==1):
        arr.append(ch.string.strip())
print(arr)
driver.close()
