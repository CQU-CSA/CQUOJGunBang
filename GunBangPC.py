#python 3.7

import re
import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

from NameToId import NameToId

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


rMap={
    'Accepted':'AC',
    'Wrong Answer':'WA',
    'Compile Error':'CE',
    'Time Limit Exceed':'TLE',
    'Runtime Error':'RE',
    'Memory Limit Exceed':'MLE',
    'Output Limit Exceed':'OLE',
    'Presentation Error':'PE',
    'Restricted Function':'RF'
}

statime=1527397200

len1=len(arrans)
len2=9
print(len1)
root=ET.Element('contest')
for i in range(len1):
    if i%9==0:
        a=ET.SubElement(root,'run')
        ET.SubElement(a,'team').text=NameToId(arrans[i])
    elif i%9==1:
        ET.SubElement(a,'id').text=arrans[i]
    elif i%9==2:
        ET.SubElement(a,'problem').text=str(ord(arrans[i])-ord('A')+1)
    elif i%9==3:
        ET.SubElement(a,'result').text=rMap[arrans[i]]
        ET.SubElement(a,'judged').text='true'
        ET.SubElement(a,'solved').text='true' if rMap[arrans[i]]=='AC' else 'false'
        ET.SubElement(a,'penalty').text='false' if rMap[arrans[i]]=='AC' else 'true'
    elif i%9==4:
        ET.SubElement(a,'language').text=arrans[i]
    elif i%9==5:
        pass
    elif i%9==6:
        pass
    elif i%9==7:
        ET.SubElement(a,'status').text='done'
    elif i%9==8:
        timearr=time.strptime(arrans[i], "%Y-%m-%d %H:%M:%S")
        ET.SubElement(a,'time').text=str(int(time.mktime(timearr))-statime)
        ET.SubElement(a,'timestamp').text=str(int(time.mktime(timearr)))

tree = ET.ElementTree(root)
tree.write("run.xml")
driver.close()
