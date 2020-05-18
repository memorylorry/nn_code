#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "memorylorry@163.com"  # 用户名
mail_pass = "YCNSEAMAMSMUZNGS"  # 口令

sender = 'memorylorry@163.com'
receivers = ['294092869@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('请把今天的事情做一下介绍', 'plain', 'utf-8')
message['From'] = "memorylorry@163.com"
message['To'] = "294092869@qq.com"
# message['cC'] = Header("memorylorry@163.com", 'utf-8')

subject = '今日会议访谈'
message['Subject'] = subject

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("success")
    "邮件发送成功"
except smtplib.SMTPException:
    print("failed")
    "Error: 无法发送邮件"
