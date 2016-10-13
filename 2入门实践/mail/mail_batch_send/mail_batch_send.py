#coding=utf-8
'''
群发邮件功能
'''
import sys, smtplib, os
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.iterators
import email.generator
from email import Encoders
import random
import sys



#############
#读取邮件列表
file_object = open('target_list.txt')
try:
    all_the_text = file_object.readlines( )
finally:
    file_object.close( )
#读取配置文件
mailto_list = all_the_text
'''
随机使用一个发件箱的配置
'''
set_index = str(random.randint(1,5))
#print('mail_set'+set_index+'.txt')
#sys.exit()
file_object = open('mail_set'+set_index+'.txt')
try:
    all_the_text = file_object.readlines( )
finally:
    file_object.close( )
set_list = all_the_text


#########格式化配置文件#############
def get_mail_fomat(index):
    return_str = set_list[index]
    return_str = return_str.replace("\n","")
    return_str = return_str.split('=')[1]
    return return_str

##########发送邮件############
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    #msg['To'] = ";".join(to_list)
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    send_succeed_num = 0
    send_fail_num = 0
    #####################
    #设置服务器，用户名、口令,邮箱的后缀以及标题和内容
    mail_host = get_mail_fomat(0)
    mail_user = get_mail_fomat(1)
    mail_pass = get_mail_fomat(2)
    mail_postfix = get_mail_fomat(3)
    mail_subject = get_mail_fomat(4)
    mail_content = get_mail_fomat(5)

    for i in mailto_list:
        if send_mail(i,mail_subject,mail_content):
            send_succeed_num +=1
            print "%s-->发送成功"%i
        else:
            send_fail_num +=1
            print "%s-->发送失败"%i
    print "\n-------------发送成功%d条" %send_succeed_num
    print "\n-------------发送失败%d条" %send_fail_num
