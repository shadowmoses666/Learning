from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))
# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com' #为了方便，默认成了QQ邮箱SMTP服务器

# 输入收件人地址:
to_addr_list = []
to_addr = input('请输入收件人邮箱地址To: ')
to_addr_list.append(to_addr)
    
while True:    
    to_addr = input('请继续输入收件人邮箱地址To，直接发送请按n: ')
    if to_addr != 'n':
        to_addr_list.append(to_addr)
        continue
    else:
        print('发送邮箱地址列表是：',to_addr_list)
        break
    
content = '''
亲爱的学员朋友：
    你好！
    恭喜大家学习坚持到现在!
    开课吧只为赋能人才，小课让学习更轻松！
'''

msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr_list)
msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr_list, msg.as_string())
server.quit()