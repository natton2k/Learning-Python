import imaplib

# looking at email inbox
M = imaplib.IMAP4_SSL('imap.gmail.com')  # establish
email = 'practice.email.10112000@gmail.com'
password = 'pxryknlocmmskhzg'
M.login(email, password)
# print(M.login(email, password))
# print(M.list())
# print(M.select('INBOX'))
M.select('INBOX')
typ, data = M.search(None, 'FROM ironlegionrocks@gmail.com')
#print(data)
email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
#print(email_data)
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
#print(raw_email_string)

# display the email's contain
import email

email_messange = email.message_from_string(raw_email_string)
for part in email_messange.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)