import smtplib
from email.message import EmailMessage
from email.utils import formataddr
import os

fromadd = os.getenv('GMAIL_FROM_ADDRESS')
pswd= os.getenv('GMAIL_PASSWORD')

def get_mailing_list():
    """Reads email addresses from mailing_list.txt."""
    with open('mailing_list.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]
 
def send_mail(sub,cont,toadd):
    try:
        mail = EmailMessage()
        mail.set_content(cont)
        mail["Subject"]=sub
        mail["From"]=formataddr(("AJ",fromadd))
        mail['To']=toadd

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(fromadd,pswd)
            smtp.send_message(mail)
        
        return True
    except:
        return False
    
def send_mail_html(sub,cont,toadd):
    try:
        mail = EmailMessage()
        mail.set_content("Your email client does not support HTML content.")
        mail.add_alternative(cont, subtype='html')
        mail["Subject"]=sub
        mail["From"]=formataddr(("AJ",fromadd))
        mail['To']=toadd

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(fromadd,pswd)
            smtp.send_message(mail)
        
        return True
    except:
        return False