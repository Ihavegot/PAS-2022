import smtplib

user = 'test4pas1@gmail.com'
password = 'zaq1@WSX'

send_from = user
send_to = ['pastest2@interia.pl']

message = f"""From: From <{send_from}>
To: To <{send_to}>
MIME-Version: 1.0
Content-type: text/html
Subject: This is a test subject

Email send wtih python smtplib\n\n

<h1>This is headline text</h1>
<b>This is bold text</b>
<i>This is italic text</i>
"""

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(send_from, send_to, message)
    server.close()
    print('Email sent')
except Exception as e:
    print(f'Error: {e}')
