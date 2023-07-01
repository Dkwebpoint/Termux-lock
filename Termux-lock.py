#!/usr/bin/env python3                                               Termux-Lock.py                                                    Modified
# -*- coding: utf-8 -*-
import os,sys,time,signal
import stdiomask as sm
# coded by Mr.DKwebpoint

flag = True
endc = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magneto = '\033[36m'
os.system('figlet -c -k -f slant Termux-Lock|lolcat')
print ( magneto +'\n\t\t[ ★ Termux - Lock ★ ]\n',endc)

print ( green +'\t\tcoded by - Mr.DK webpoint\n',endc)
def main_menu():
    dash = '-'
    print(blue +'\n'+ dash*15 +'Main-Menu'+ dash*15)
    print(yellow +'''
    1.Login
    2.Exit\n''',endc)
    print(blue +'\n'+ dash*13 +'Select option'+ dash*13)

def check_usr_pass():
    dash = '-'
    global flag,usr,pw
    print(blue +'\n'+ dash*15 +'Login'+ dash*15)
    username = input(yellow + '\n\t[+] Username : ')
    password = sm.getpass(prompt=yellow + '\n\t[*] Password : ',mask='*')
    print(blue +'\n'+ dash*13 +'Completed'+ dash*13)
    '''
    Attention !
    avant d'exécuter ce script vous devez créer une combinaison USER/PASS 
    et enregistrer les dans un fichier de votre choix 
    cd /data/data/com.termux/files/usr/share/
    mkdir termux-user
    cd termux-user
    nano usr_pwd.txt et écrire vos identifiants comme ceci :
    root (la première ligne correspond au utilisateur)
    toor (la deuxième ligne correspond au password)
    '''
    usrpwd = open("/data/data/com.termux/files/usr/share/termux-user/usr_pwd.txt")
    lines = usrpwd.readlines()
    usrpwd.close()
    if(len(lines) >= 2):
        usr = lines[0]
        pwd = lines[1]
        if username+'\n' == usr and password+'\n' == pwd:
            print(green + usr +'Connected Successfully ' ,endc)
            flag = False
        else:
            print(red + '\n\t\t[×] Invalid username or password [×]',endc)
    else:
        print(red +'\n\tYou have removed your lock')

def exit():
    global flag
    print(blue +'\n\tThank you for Using...',endc)
    time.sleep(0.25)
    os.kill(os.getppid(), signal.SIGHUP)


if __name__ == '__main__':
    while flag == True:
        try:
            main_menu()
            menu = {1:check_usr_pass,2:exit}
            options = input(magneto +'\nEnter choice : ')
            if(options == '1'):
                check_usr_pass()
            else:
                print ('')
            if(options == '2'):
                exit()
            else:
                print ('')
            if (options) != 1 or (options) != 2:
                print(red +'\t Choice not allowed...',endc)

        except KeyboardInterrupt:
            print(" Finishing up...Keyboard Interrup\r"),
            time.sleep(0.25)
            print(green +" So, First Login \r",endc)
