import smtplib
from email.message import EmailMessage
from email.utils import formataddr

fromadd = "ajeetha757@gmail.com"
pswd="nzwj gwff sfqi xhno"

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