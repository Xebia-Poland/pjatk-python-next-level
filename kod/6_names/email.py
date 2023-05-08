import smtplib as xxx
me = 'me@example.com'
pwd = 'supersecretpassword1'
mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(me, pwd)
mailer.sendmail(me, 'friend@example.com', 'Hello')
mailer.close()
