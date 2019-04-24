#python 3.7

import re
import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

chromePath = './chromedriver'
url = 'http://acm.cqu.edu.cn/contest_show.php?cid=243#status'
arrans=[]


driver = webdriver.Chrome(chromePath)
driver.get(url)
#等待网页打开
time.sleep(1)
while True:
    #获取网页
    elements = driver.page_source
    #bs4处理网页
    soup = BeautifulSoup(elements,'html.parser')
    #排版
    html = soup.prettify()
    #删除空字符，方便正则表达式搜索
    html=html.replace('\n','')
    #找到干扰标签对
    arr = re.findall(r'<tr>.*</tr>',html)
    #删除干扰标签对
    for i in arr:
        html = html.replace(i,'')
    #查找所需标签对
    arr = re.findall(r'<tr class="odd">.+</tr>',html)

    files = open('.\log.html','wb')
    #合并为一个字符串
    data = ''
    for i in arr:
        data=data+i
    #    files.write(i.encode('utf-8'))
    #bs4处理标签对
    data = BeautifulSoup(data,'html.parser')
    #排版保存
    files.write(data.prettify().encode('utf-8'))
    files.close()
    
    #遍历bs4 data ,找到最底层所需数据，保存到数组
    for ch in data.descendants:
        #print(ch)
        if ch.name is None:
            continue
        #print(len(ch.contents))
        if(len(ch.contents)==1):
            arrans.append(ch.string.strip())
    if soup.find(attrs={'class':'next disabled'}):
        break
    buttun=driver.find_element_by_class_name('next')
    buttun.find_element_by_tag_name('a').click()
    time.sleep(1)
print(len(arrans))
root=ET.Elements('contest')
driver.close()
