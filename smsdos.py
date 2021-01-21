import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

emailAddr = ""
phoneNumber = ""
password = ""
s = smtplib.SMTP('smtp.gmail.com', 587)  # This may be different for your email address

carriers = {
    "verizon": "vtext.com",
    "att": "txt.att.net",
    "sprint:": "sprintpaging.com",
    "tmobile": "tmomail.net",
    "virgin": "vmobl.com"
}

attempts = 3


def send_message(sender, recipient):

    msg = MIMEMultipart()

    msg['From'] = ""

    body = "This is a Text Message."

    msg.attach(MIMEText(body, 'plain'))

    ts = smtplib.SMTP('smtp.gmail.com', 587)

    ts.starttls()

    ts.login(sender, password)

    text = msg.as_string()

    ts.sendmail(sender, recipient, text)

    ts.quit()


def unknown():
    for x in range(attempts):
        # print("Attempting Verizon text message..")
        send_message(emailAddr, "<{0}@vtext.com>".format(phoneNumber))
        # print("Attempting AT&T text message..")
        send_message(emailAddr, "<{0}@txt.att.net>".format(phoneNumber))
        # print("Attempting Spring text message..")
        send_message(emailAddr, "<{0}@sprintpaging.com>".format(phoneNumber))
        # print("Attempting Tmobile text message..")
        send_message(emailAddr, "<{0}@tmomail.net>".format(phoneNumber))
        # print("Attempting Virgin Mobile text message..")
        send_message(emailAddr, "<{0}@vmobl.com>".format(phoneNumber))


def known(carrier):
    lower_carrier = carrier.lower()  # makes input not case sensitive
    for x in range(attempts):

        print("Sending {0} text to {0}....".format(carrier, phoneNumber))
        send_message(emailAddr, "<{0}@txt.att.net>".format(phoneNumber))


unknown()

