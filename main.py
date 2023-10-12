import imaplib
import email
from email.header import decode_header

username = "USERNAME"
password = "PASSWORD"
imap_server = "imap." + username.split("@")[1]

def extract_subject(msg):
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        return subject.decode(encoding or 'utf-8')
    return subject

def main():
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, password)
    _, messages = imap.select("INBOX")
    messages = int(messages[0])
    N = 20
    for i in range(messages, messages - N, -1):
        mail_number = str(i)
        _, msg = imap.fetch(mail_number, "(BODY.PEEK[HEADER])")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = extract_subject(msg)
                if "*****SPAM*****" in subject:
                    print("Deleting:", subject)
                    imap.copy(mail_number, "INBOX.Trash")
                    imap.store(mail_number, "+FLAGS", "\\Deleted")
    imap.close()
    imap.logout()

main()