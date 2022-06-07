import smtplib

user = 'test4pas1@gmail.com' # skad wysyłany jest mail, gmail najlepiej tylko trzeba odblokowac w ustawieniach maila opcje 'less secured apps'
password = 'zaq1@WSX' # haslo do konta gmail

send_from = user # nadawca
send_to = ['pastest2@interia.pl'] # odbiorca

# wiadomosc
message = f"""From: Mikrosoft
To: You
MIME-Version: 1.0
Content-type: text/html
Subject: Mikrosoft support

<h1>Your computer has been virused</h1>

<p>Its Rajem from Mikrosoft support.</p>

<p><b>Please</b>

give us your credit card info.</p>

<p><i>This is not a scam.</i></p>
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
