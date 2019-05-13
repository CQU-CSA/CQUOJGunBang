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
url = 'http://acm.cqu.edu.cn/contest_show.php?cid=293#standing'


driver = webdriver.Chrome(chromePath)
driver.get(url)
#等待网页打开
time.sleep(1)
#登陆
mens =driver.find_element_by_class_name('btn-navbar')
try:
    mens.click()
except:
    pass
time.sleep(0.5)
login=driver.find_element_by_id('loginbutton')
login=login.find_element_by_tag_name('a')
login.click()
time.sleep(0.5)
username = driver.find_element_by_id('username')
username.send_keys('cqupc19f55')
time.sleep(0.5)
password = driver.find_element_by_id('password')
password.send_keys('MNcH7d3h')
time.sleep(0.5)
login=driver.find_element_by_id('logindialog')
login=login.find_element_by_name('login')
login.click()
time.sleep(4)
settings=driver.find_element_by_id('cset_a')
settings.click()
time.sleep(0.5)
settings=driver.find_element_by_name('shownum')
settings.click()
time.sleep(0.5)
login=driver.find_element_by_id('csetform')
login=login.find_element_by_name('login')
login.click()
time.sleep(0.5)
#初始化
nickname=[]
username=[]


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