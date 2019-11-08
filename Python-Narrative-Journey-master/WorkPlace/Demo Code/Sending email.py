import smtplib


smtb_object = smtplib.SMTP('smtp.gmail.com', 587)  # PORT =587: encrypt with TLS
print(smtb_object.ehlo())  # establish the connection
print(smtb_object.starttls())  # need this for TLS
#email = getpass.getpass('Email: ') #only work in cmd
#password = getpass.getpass('Password: ')
email = 'practice.email.10112000@gmail.com'
password = 'pxryknlocmmskhzg' # this was made by gmail app password
smtb_object.login(email, password)
to_email = 'ironlegionrocks@gmail.com'
from_email = email
subject = input('Enter subject:')
message = input('Enter messange')
msg = 'Subject: ' + subject + '\n' + message
smtb_object.sendmail(from_email, to_email, msg)
smtb_object.quit()