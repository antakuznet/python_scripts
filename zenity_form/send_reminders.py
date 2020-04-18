#!/usr/bin/env python3

import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

smtp_server = ''
smtp_port = ''
email_sender = ''
sender_pass = ''

def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("Invocation:")
    print("    send_reminders 'date|meeting title|emails' ")
    return 1

def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")

def message_template(date, title):
    message = MIMEMultipart()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    mail_content = f'''
Hi all!

This is a quick mail to remind you all that we have a meeting about:
"{title}"
the {weekday} {date}.
See you there.
'''
    message.attach(MIMEText(mail_content, 'plain'))
    return message

def send_message(message, emails):
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    #enable security
    smtp.starttls()
    #login with email and password
    smtp.login(email_sender, sender_pass)
    message['From'] = email_sender
    for email in emails.split(','):
        del message['To']
        message['To'] = email
        text = message.as_string()
        smtp.sendmail(email_sender, email, text)
    smtp.quit()
    pass

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)

    except Exception as e:
        print("Failure to send email", file=sys.stderr)



if __name__ == "__main__":
    main()
