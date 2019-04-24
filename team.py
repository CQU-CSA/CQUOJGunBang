import xml.etree.ElementTree as ET
from NameToId import NameToId
 

root = ET.Element('contest')

for i in range(30):
    a=ET.SubElement(root,'team')
    st='*cqupc18_team{0}'.format(i+1)
    ET.SubElement(a,'external-id').text=NameToId(st)
    ET.SubElement(a,'id').text=NameToId(st)
    ET.SubElement(a,'name').text='xxx{0}'.format(i+1)
    ET.SubElement(a,'region')
    ET.SubElement(a,'university').text=st
    ET.SubElement(a,'university-short-time')
    
for i in range(60):
    a=ET.SubElement(root,'team')
    st='cqupc18_team{0}'.format(i+1)
    ET.SubElement(a,'external-id').text=NameToId(st)
    ET.SubElement(a,'id').text=NameToId(st)
    ET.SubElement(a,'name').text='sss{0}'.format(i+1)
    ET.SubElement(a,'region')
    ET.SubElement(a,'university').text=st
    ET.SubElement(a,'university-short-time')

tree = ET.ElementTree(root)
tree.write("team.xml")