'''
打开文件过程中用到了‘r’这个参数，在文件打开过程中还会用到很多操作方法，
都有不同的参数来表示。'r'读模式、'w'写模式、'a'追加模式、'b'二进制模式、'+'读/写模式。
'''
f=open('./test.txt','w')
f.write('hello')
f.write('\r\n')
f.write('world')
f.close()


f=open('./test.txt','r')
content = f.readline()
print(content)

