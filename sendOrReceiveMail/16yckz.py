#coding: gbk
#Զ�̿��ƿ��ػ���Ŀ
import time
import os
import sys
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email

def guanji():
    #�˺��������͹ػ��ı��⣨��guan��������
    sent=smtplib.SMTP('smtp.sina.com') 
    sent.login('qq372777648@sina.com','12345678')
    to=['qq372777648@sina.com']
    content = MIMEText('')
    content['Subject']='guan'
    content['From']='qq372777648@sina.com'
    content['To']=','.join(to)
    sent.sendmail('qq372777648@sina.com',to,content.as_string())
    sent.close()

def chongqi():
    #�˺�����������������chong���ı��������
    sent=smtplib.SMTP('smtp.sina.com') 
    sent.login('qq372777648@sina.com','12345678')
    to=['372777648@qq.com']
    content = MIMEText('')
    content['Subject']='chong'
    content['From']='qq372777648@sina.com'
    content['To']=','.join(to)
    sent.sendmail('qq372777648@sina.com',to,content.as_string())
    sent.close()
def chongzhi():#����
    sent=smtplib.SMTP('smtp.sina.com')
    sent.login('weiweihappy321@sina.com','aA123456789')
    to=['weiweihappy321@sina.com']
    content = MIMEText('')
    content['Subject']='reflash'
    content['From']='weiweihappy321@sina.com'
    content['To']=','.join(to)
    sent.sendmail('weiweihappy321@sina.com',to,content.as_string())
    sent.close()


def read():
    #�˺��������ȡ�ʼ��е�ָ�ָ��Ϊguan����0��ָ��Ϊchong����1
    read=poplib.POP3('pop.sina.com')
    #pop.qq.com 372777648@qq.com afqelhxbpakvbhdd  pop.sina.com qq372777648@sina.com 12345678
    read.user('qq372777648@sina.com')
    read.pass_('12345678')
    tongji=read.stat()#�����������ͳ����Ϣ
    str = read.top(tongji[0], 0)  #����������ʼ���Ϣ
    str2=[]
    for x in str[1] : #���������
                try:  
                    str2.append(x.decode())  
                except:  
                    try:  
                        str2.append(x.decode('gbk'))  
                    except:  
                        str2.append((x.decode('big5')))
    msg = email.message_from_string('\n'.join(str2))#��String���ʼ�ת����email.messageʵ��  
    biaoti = decode_header(msg['subject'])
    print  biaoti
    if biaoti[0][1]:   #����еڶ���Ԫ�أ�˵���б�����Ϣ
           biaoti2 = biaoti[0][0].decode(biaoti[0][1])  
    else:  
           biaoti2= biaoti[0][0]
    #OK,��ʱ�ɹ���ȡ�����һ���ʼ����⣬��biaoti2
    if biaoti2=="guan":
        return 0
    if biaoti2=="chong":
        return 1
    read.quit()

if __name__ == '__main__':  #�����д˳����ʱ�򣬶�ȡ�ʼ�
   # chongqi()
    while True:
        time.sleep(2)
        res=read()
        if res==0:
            #os.system('shutdown -s -t 10')
            print "---------------shutdown"
            #chongzhi()
            break
        if res== 1:
            #os.system('shutdown -r')
            print "---------------restart"
            # chongzhi()
            break
        print "none"

