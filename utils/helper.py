import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication

def send_email(sender,password,reciever,smtp_server,smtp_port,email_message,subject):
    message = MIMEMultipart()
    message["To"] = Header(reciever)
    message["From"] = Header(sender)
    message["Subject"] = Header(subject)
    message.attach(MIMEText(email_message,"plain","utf-8"))
    
    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.ehlo()
    server.login(sender,password)
    text = message.as_string()
    server.sendmail(sender,reciever,text)
    server.quit()