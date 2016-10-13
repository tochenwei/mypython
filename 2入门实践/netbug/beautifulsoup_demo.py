#coding:utf-8
#demo http://cuiqingcai.com/1319.html
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print soup.prettify()

print soup.title
#<title>The Dormouse's story</title>
print soup.head.name
print soup.p.attrs
#{'class': ['title'], 'name': 'dromouse'}
print soup.p.string

print soup.head.contents

content = soup.head.title.string
for parent in  content.parents:
    print parent.name


print soup.p.next_sibling
#       实际该处为空白
print soup.p.prev_sibling
#None   没有前一个兄弟节点，返回 None
print soup.p.next_sibling.next_sibling

soup.find_all('b')
# [<b>The Dormouse's story</b>]
print soup.find_all('a')
#---------------------------css selector----------------------------------
print soup.select('title')
print soup.select('a')
print soup.select('b')
print soup.select('.sister')
print soup.select('#link1')
print soup.select('p #link1')
print soup.select('a[class="sister"]')
print soup.select('a[href="http://example.com/elsie"]')

