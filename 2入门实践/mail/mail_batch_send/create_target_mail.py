#coding=utf-8
'''
批量产生用于发送的目标邮箱
'''
import math
def creare_target_mail(offset,length):
    max = offset+ length
    for i in range(offset, max + 1):
        f=open('./target_list.txt','a')
        f.write(str(i)+'@qq.com')
        if i < max:
            f.write('\n')
        f.close()
    return 0
creare_target_mail(600000,3000)
