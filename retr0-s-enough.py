from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
r = get("https://raw.githubusercontent.com/D3DSECRETR0/Retr0-s-Enough/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Updating...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
    
while 1:
    system("cls||clear")
    print("""{}
     ______                         _     
    |  ____|                       | |    
    | |__   _ __   ___  _   _  __ _| |__  
    |  __| | '_ \ / _ \| | | |/ _` | '_ \ 
    | |____| | | | (_) | |_| | (_| | | | |
    |______|_| |_|\___/ \__,_|\__, |_| |_|
                               __/ |      
                              |___/      
                            
                        {}by {}@Retr0  
    """.format(Fore.LIGHTCYAN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + "1. Send SMS\n2. Exit\n\n" + Fore.LIGHTYELLOW_EX + "Option: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "ERROR. Try Again.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Write down the phone number without '+90' in the beginning: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Wrong phone number. Try Again.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "How many do you want to send?: "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "ERROR. Try Again.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "How many seconds interval do you want to send?: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "ERROR. Try Again.") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(str(tel_no))
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nTo return to the main menu press 'Enter'..")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Exiting...")
        break
