#coding=utf-8
'刘'.decode('gbk') #用gbk解压成unicode

'刘'.decode('gb2312')#用gb2312解压成unicode
'刘'.decode('gb2312').encode('utf-8')#用gb2312解压成unicode，再压缩成utf-8
'刘'.decode('gb2312').encode('gb2312')#用gb2312解压成unicode，再压缩成gb2312

'刘'.decode('gb2312').encode('gbk')#用gb2312解压成unicode，再压缩成gbk

repr('刘') #刘的gb2312/gbk表示

