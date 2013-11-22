# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:40:54 2013

@author: Avaziyi
"""

#from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Fore.RESET + Back.RESET + Style.RESET_ALL)
#print('back to normal now') 


#from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
#init()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))