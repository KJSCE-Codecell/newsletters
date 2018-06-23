import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "codecell.engg@somaiya.edu"
subject = "Monthly Newsletter Test"
filename = "newsletter.html"

html_file = open('Newsletter.html','r').read()   #.encode('utf-8')

f = open("subs.txt",'r')
subs = ['nishchith.s@somaiya.edu']
'''
for i in f.readlines():
    subs.append(i[:-1])
'''

def send_text_mail(toaddr):
    msg = MIMEMultipart()
    msg['From'] = "KJSCE CodeCell"
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(html_file,'html'))     # params body_text : html_file , 'plain' : 'html'

    #server = smtplib.SMTP('smtp.gmail.com', 465) #465 or 587 open
    #server.starttls()
    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.login(fromaddr, "GDScodecell123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Text email sent successfully to :"+toaddr)
    server.quit()


for to in subs:
    send_text_mail(to)
