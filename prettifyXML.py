from bs4 import BeautifulSoup as BS

files = open('.\contest.xml','rb')
xml =files.read()
soup=BS(xml,'lxml')
files.close()
files = open('.\contest.xml','wb')
files.write(soup.prettify().encode('utf-8'))
print( xml.decode('utf-8'))