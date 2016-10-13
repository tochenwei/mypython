#coding=utf-8
utf8Data = "中华人民共和国"
unicodeData = utf8Data.decode("UTF-8")
gbkData = unicodeData.encode("GBK")
print gbkData

f=open('./content.txt','r')
content = f.readline()
print(content)