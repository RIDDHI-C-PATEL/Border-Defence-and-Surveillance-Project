import smtplib

def send_email():

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login("your_email","password")

    message="Border Alert Detected"

    server.sendmail(
    "your_email",
    "receiver_email",
    message
    )

    server.quit()