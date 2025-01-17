import re
def email_sender(file_path):
    with open(file_path) as file:
        content = file.read()
        sender_mail = re.search(sender, content)
        return sender_mail.group(1)

def email_receiver(file_path):
    with open(file_path) as file:
        content = file.read()
        receiver_mail = re.search(receiver, content)
        return receiver_mail.group(1)
    
def email_subject(file_path):
    with open(file_path) as file:
        content = file.read()
        mail_subject = re.search(subject, content)
        return mail_subject.group(1)
def email_body(file_path):
    with open(file_path) as file:
        content = file.read()
        mail_body = re.search(body, content, re.DOTALL)
        return mail_body.group(1)
    
sender = r'From: \w+ \w+ <([\w.-]+@[\w.-]+)>'
receiver = r'To: \w+ \w+ <([\w.-]+@[\w.-]+)>'
subject = r'Subject: (\w+ \w+)'
body = r'(?:\r?\n){2}(.*)'
file_path = 'email.txt'

print(f'Sender: {email_sender(file_path)}')
print(f'Receiver: {email_receiver(file_path)}')
print(f'Subject: {email_subject(file_path)}')
print(f'Body: {email_body(file_path)}')