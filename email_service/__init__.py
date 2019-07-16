import smtplib
from email.mime.text import MIMEText


class EmailService(object):
    def __init__(self, host, user, password):
        # 第三方 SMTP 服务
        self.host = host  # SMTP服务器
        self.user = user  # 用户名
        self.password = password  # 授权码
        self.sender = user

    def send(self, title, content, receivers):
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = '{}'.format(self.sender)
        message['To'] = ','.join(receivers)
        message['Subject'] = title
        try:
            smtpObj = smtplib.SMTP_SSL(self.host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(self.user, self.password)  # 登录验证
            smtpObj.sendmail(self.sender, receivers, message.as_string())  # 发送
            print('mail has been send successfully.')
            return True
        except smtplib.SMTPException as e:
            print('send email err=>', e)
            return False

# 添加图片、附件、html等 https://blog.csdn.net/leiwuhen92/article/details/83239791





