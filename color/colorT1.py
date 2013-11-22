# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:37:50 2013

@author: Avaziyi
"""
import sys
from termcolor import colored, cprint
print colored('hello', 'red'), colored('world', 'green')

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)

cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

print'fdfdfdf',(colored('Hello, World!', 'green', 'on_red'))
