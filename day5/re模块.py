#Author:immortal luo
# -*-coding:utf-8 -*-
import re

#*****************************************
#re.match:从头开始匹配
#re.search:匹配包含
#re.findall:把所有匹配到的字符放到列表中返回
#re.splitall:以匹配到的字符当做列表分隔符
#re.sub:匹配字符并替换
#*****************************************

# print(re.match(".","csk lmm"))#匹配任意除换行符"\n"外的字符(在DOTALL模式中也能匹配换行符)
# print(re.match("c*","csk lmin"))#匹配前一个字符0或多次
# print(re.match("c+","csk lmm"))#匹配前一个字符1次或无限次
# print(re.match("c?","csk lmm"))#匹配一个字符0次或1次
# print(re.match("^c","csk lmm"))#匹配字符串开头。在多行模式中匹配每一行的开头
# print(re.search("k$","csk"))#$匹配字符串末尾，在多行模式中匹配每一行的末尾
# print(re.match("csk|lmm","csk lmm"))#或。匹配|左右表达式任意一个，从左到右匹配，如果|没有包括在()中，则它的范围是整个正则表达式
# print(re.match("c{2}","cccsk lmmm"))#{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次
# print(re.match("a[bcd]e","abe"))#字符集。对应的位置可以是字符集中任意字符。
# print(re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","abcd1234daf@34").groupdict())
# print(re.split("[0-9]+","sd12sd1sf1s1f3sd"))#分割
# print(re.sub("[0-9]+","*","sd12sd1sf1s1f3sd",count=2))#替换
# print(re.search(r"\\","asd\dfd"))
# print(re.search(r"^a","\nasd\nerfd"))
# print(re.search(r"^a","\nasd\nerfd",flags=re.M))