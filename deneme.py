from smtplib import SMTP

# Simple Mail Transfer Protocol 
# Basit Mail Transfer Protokolü 
try:
    # Mail Mesaj Bilgisi 
    subcjet = "Test"
    message = "Bu bir test mesajıdır!"
    content = "Subject: {0}\n\n{1}".format(subcjet,message)

    # Hesap Bilgileri 
    myMailAdress =  "spacecowboyllimited@gmail.com"
    password = "Alpcan270495"

    # Kime Gönderilecek Bilgisi
    sendTo = "alpcanakdemir@gmail.com "

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)
    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
    print("Mail Gönderme İşlemi Başarılı!")
except Exception as e:
    print("Hata Oluştu!\n {0}".format(e))