#Author:immortal luo
# -*-coding:utf-8 -*-
import xml.etree.ElementTree as ET

#读取xml内容:
# tree = ET.parse('test.xml')
# root = tree.getroot()
# print(root.tag)
# # 一个节点有tag、attrib、text三个值
# # tag是标签的名字
# # text是标签的内容
# # attrib是标签属性的字典，通过字典的get('key')来获取对应的属性的值
# # 直接for chile in parent 来遍历节点下的子节点
# for child in root:
#     print(child.tag, child.attrib)
#     for elem in child:
#         print(elem.tag, elem.text, elem.attrib)
# # 只遍历year节点
# for node in root.iter('year'):
#     print(node.tag, node.text)

#生成xml内容：
new_xml = ET.Element('namelist')
name = ET.SubElement(new_xml, 'name', attrib={'enrolled': 'yes'})
age = ET.SubElement(name, 'age', attrib={'checked': 'no'})
sex = ET.SubElement(name, 'sex')
sex.text = '33'

name2 = ET.SubElement(new_xml, 'name', attrib={'enrolled': 'no'})
age = ET.SubElement(name2, 'age')
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write('te.xml', encoding='utf-8', xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式

#修改、删除xml内容：
# tree = ET.parse('test.xml')
# root = tree.getroot()
#
# # 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)   # 修改内容
#     node.set("updated", "yes")  # 修改属性
#
# tree.write('tt.xml')
#
#
# # 删除
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
# tree.write('tt1.xml')