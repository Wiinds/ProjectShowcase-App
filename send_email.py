import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jeremyabraham17@gmail.com"
    password = "dzzo bpur yxyv caie"
    receiver = "jeremyabraham17@gmail.com"
    context = ssl.create_default_context()
    #message = """\
    #Subject: Email from your ProjectShowcase App
    #Test test
    #"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



