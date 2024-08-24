import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port=2525
    smtp_server='smtp.mailtrap.io'
    login='95a39ed8f69bb6'
    password='a6ae1af9f44d7e'
    message=f"<h3>New feedback submission</h3><ul><li>Customer:{customer}</li><li>Dealer:{dealer}</li></ul>"
    sender_email='aryendratomar@gmail.com'
    receiver_email='aryendrasingh@gmail.com'
    msg=MIMEText(message,'html')
    msg['Subject']='Lexus feedback'
    msg['From']=sender_email
    msg['To']=receiver_email


    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
