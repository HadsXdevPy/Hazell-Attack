from os import system
import time
from termcolor import colored

system('pip install termcolor')
system('clear')
logo='''
██╗  ██╗ █████╗ ███████╗██████╗ ██╗     ██╗                     ██║  ██║██╔══██╗╚══███╔╝╚════██╗██║     ██║
███████║███████║  ███╔╝  █████╔╝██║     ██║
██╔══██║██╔══██║ ███╔╝   ╚═══██╗██║     ██║
██║  ██║██║  ██║███████╗██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝
'''
print (colored(logo, 'green'))                                  print()
print(colored("________________________________________", 'red'))
print()
print(colored("Author : Haz", 'green'))                         print(colored("contact: 082289492851 ", 'green'))
print(colored("Thanks : HadsXdev", 'green'))                    print(colored("Team   : NEVER LOST T3AM", 'green'))
print(colored("________________________________________", 'red'))
ajg=input(colored("Masukkan no Target :", 'cyan'))              time.sleep (2)
while True:
  print(colored("Memulai attacking ke Target....", 'red'))
