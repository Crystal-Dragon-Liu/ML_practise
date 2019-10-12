# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "LybCrystal@163.com"  # 用户名
mail_pass = "lybcrystal163"  # 口令

sender = 'LybCrystal@163.com'
receivers = ['13270713280@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('you have 2 days(48hours) for make a payment.\nif this does not happen - you will be killed \nAnd so that you do not obstruct me,your device will be locked (also after 48 hours)\nDo not take this frivolously\nThis is the last warning', 'plain', 'utf-8')
message['From'] = '刘育博<LybCrystal@163.com>'
message['To'] = '13270713280@126.com'

subject = 'WARNING MESSAGE'
message['Subject'] = Header(subject, 'utf-8')


smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮箱发送成功")
