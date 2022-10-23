from multiprocessing.connection import wait
import socket
import os
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('Proxy.txt').readlines()
bots = len(proxys)

def si():
    print('\x1b[38;2;233;233;233mWelcome to NaSaKi DDos \x1b[38;2;233;233;233mBy TrungHai')
    print("")

def menu():
    sys.stdout.write(f"\x1b]2;NaSaKi DDos By TrungHai")
    clear()
    print('\x1b[38;2;233;233;233mWelcom to Space-DDos \x1b[38;2;233;233;233mBy Trung Hải & AnVu')
    clear()
    print('\x1b[38;2;233;233;233mWelcom to Space-DDos \x1b[38;2;233;233;233mBy Trung Hải & AnVu')
    print(f'''
   \x1b[38;2;255;165;0m                       .▄▄ ·  ▄▄▄· ▄▄▄·  ▄▄· ▄▄▄ .
   \x1b[38;2;255;165;0m                       ▐█ ▀. ▐█ ▄█▐█ ▀█ ▐█ ▌▪▀▄.▀·
   \x1b[38;2;255;165;0m                       ▐▄▀▀▀█▄ ██▀·▄█▀▀█ ██ ▄▄▐▀▀▪▄
   \x1b[38;2;255;165;0m                        ▐█▄▪▐█▐█▪·•▐█▪ ▐▌▐███▌▐█▄▄▌ 
   \x1b[38;2;255;165;0m                         ▀▀▀▀ .▀    ▀  ▀ ·▀▀▀  ▀▀▀ 
              \x1b[38;2;255;140;0m═══════════════\x1b[38;2;255;165;0m╔═══════════════════╦\x1b[38;2;0;212;14m══════════════
                  \x1b[38;2;0;212;14m╔══════════╩═══════════════════╩═════════╗
                  \x1b[38;2;255;140;0m║ \x1b[38;2;255;140;0mCảnh Báo Không Copy Dưới Mọi Hình Thức \x1b[38;2;255;140;0m║
                  \x1b[38;2;255;140;0m║       \x1b[38;2;255;140;0mKhông DDoS Web Có Miền .gov      \x1b[38;2;255;140;0m║  
                  \x1b[38;2;255;140;0m║          \x1b[38;2;255;140;0mDùng Lệnh: space run          \x1b[38;2;255;140;0m║
                  \x1b[38;2;255;140;0m╚════════════════════════════════════════╝
''')

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;255;140;0m===>''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()

# METHODS SPACE

        elif "space" in cnc:
            try:
                run = cnc.split()[1]
                os.system(f'java space.java nil')
            except IndexError:
                print('Dùng Lệnh: space run ')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
            
def login():
    main()

login()
