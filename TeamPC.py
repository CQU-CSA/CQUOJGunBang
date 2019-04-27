#python 3.7
# -*- coding: UTF-8 -*-

import re
import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import sys

from NameToId import NameToId

chromePath = './chromedriver'
url = 'http://acm.cqu.edu.cn/contest_show.php?cid=287#standing'
nickname=[]
username=[]

driver = webdriver.Chrome(chromePath)
driver.get(url)
#等待网页打开
time.sleep(1)
#获取网页
elements = driver.page_source

soup = BeautifulSoup(elements,'html.parser')

search=soup.find_all('td',attrs={'class':'tnickname'})
for td in search:
    nickname.append(td.a.string)
search=soup.find_all('td',attrs={'class':'tusername'})
for td in search:
    username.append(td.a.string)

root = ET.Element('contest')

length=len(nickname)

for i in range(length):
    a=ET.SubElement(root,'team')
    ET.SubElement(a,'external-id').text=NameToId(username[i])
    ET.SubElement(a,'id').text=NameToId(username[i])
    ET.SubElement(a,'name').text=nickname[i]
    ET.SubElement(a,'nationality').text='xxx'
    ET.SubElement(a,'region')
    ET.SubElement(a,'university').text=nickname[i]
    ET.SubElement(a,'university-short-time')

tree = ET.ElementTree(root)
tree.write("teamPC.xml")
driver.close()