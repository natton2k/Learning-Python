import smtplib
import imaplib
import email


def sent_email():
    smt_object = smtplib.SMTP('smtp.gmail.com', 587)
    smt_object.ehlo()
    smt_object.starttls()
    from_email = 'practice.email.10112000@gmail.com'
    password = 'pxryknlocmmskhzg'
    smt_object.login(email, password)
    to_email = 'info@thegoldbugs.com'
    subject = 'Hey'
    message ='Please reply'
    msg = 'Subject: '+subject+'\n'+message
    smt_object.sendmail(from_email, to_email, msg)
    smt_object.quit()


def receiving_mail():
    M = imaplib.IMAP4_SSL('imap.gmail.com')
    mail = 'practice.email.10112000@gmail.com'
    password = 'pxryknlocmmskhzg'
    M.login(mail, password)
    M.select('inbox')
    typ, data = M.search(None, 'FROM info@thegoldbugs.com')
    email_id = data[0]
    result, email_data = M.fetch(email_id, '(RFC822)')
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')


    email_messange = email.message_from_string(raw_email_string)
    for part in email_messange.walk():
        if part.get_content_type() == 'text/html':
            body = part.get_payload(decode=True)
            print(body)


receiving_mail()

