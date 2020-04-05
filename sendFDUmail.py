
import smtplib
from email.mime.text import MIMEText
from email.header import Header



def sendmai(mail_host, mail_user, mail_password, sender, receiver, subject, message):
    message['From'] = Header('刘之源', 'utf-8')
    message['To'] = Header('刘之源', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    server = smtplib.SMTP()
    server.connect(mail_host, port)  # 25 为 SMTP 端口号
    server.login(mail_user, mail_password)
    server.sendmail(sender, receiver, message.as_string())

mail_host = r'mail.fudan.edu.cn'
port = 25
username = str(input('请输入学号')) + r'@fudan.edu.cn'
mail_user = username
mail_password = input('请输入邮箱密码')
sender = username
subject = input('请输入主题')
content = input('请输入内容')
message = MIMEText(content, 'plain', 'utf-8')
r = str(input('请输入收件人地址'))
rn = input('请输入收件人姓名')
message['To'] = Header('刘之源', 'utf-8')
receiver = ['16307110071@fudan.edu.cn', r]
sendmai(mail_host, mail_user, mail_password, sender, receiver, subject, message)
