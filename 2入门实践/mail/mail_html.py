#coding:utf-8
'''
发送html文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib  
from email.mime.text import MIMEText  
mailto_list=["e200800@qq.com"] 
mail_host="smtp.163.com"  #设置发件箱服务器
mail_user="tochenwei@163.com"    #发件箱用户名
mail_pass="workanddream"   #发件箱口令 
mail_postfix="163.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:
        '''这是ssl链接格式的'''
        #s = smtplib.SMTP_SSL( mail_host, 465 )
        '''普通登录邮件服务器'''
        s = smtplib.SMTP()  
        s.connect(mail_host)
        
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(mail_user, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"尊敬的亲","今日加班时间安排表"):  
        print "发送成功"  
    else:  
        print "发送失败"
