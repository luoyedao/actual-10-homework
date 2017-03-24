# coding:utf-8
#from poplib import POP3
#from smtplib import SMTP
#from time import sleep

#SMTPSVR = SMTP('smtp.yeah.net')
#POPSVR = POP3('pop3.yeah.net')
#
#who = 'yaoliang83@yeah.net'
#body = '''\From: %(who)s\r\nTo: %(who)s\r\nSubject: test msg\r\nHello World!''' %{'who': who}
#
#sendSvr = SMTPSVR
#sendSvr.login('yaoliang83@yeah.net','890iop*()')
#errs = sendSvr.sendmail(who,[who],body)
#sendSvr.quit()
#assert len(errs)==0,errs
#sleep(10)
#
#recvSvr = POPSVR
#recvSvr.user('yaoliang83')
#recvSvr.pass_('890iop*()')
#rsp,msg,siz = recvSvr.retr(recvSvr.stat()[0])
##sep = msg.index('')
##recvBody = msg[sep+1:]
##assert body==recvBody
#print msg


from smtplib import SMTP

# 'who'是email格式，data为字典格式
# data['work']为标题，data['operate']为正文

def mymail(from_email,passwd,to_email,data):
    SMTPSVR = SMTP('smtp.yeah.net')
    data['from'] = from_email
    data['to'] = to_email

    body = '''\From: %(from)s\r\nTo: %(to)s\r\nSubject: %(work)s\r\n\r\nOperate: %(operate)s\r\n''' % data

    sendSvr = SMTPSVR
    sendSvr.login(from_email,passwd)
    errs = sendSvr.sendmail(from_email,[to_email],body)
    sendSvr.quit()
