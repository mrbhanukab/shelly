import sys
import os
from components import *

os.system('cls||clear')

logo()

# ! Setup Command
cmd = []
if len(sys.argv) == 1:
    cmd.insert(0, input('How can I be of Service?:'))
    cmd.insert(1, input('How can I be of Service?:'))
    cmd.insert(2, input('How can I be of Service?:'))
    print(cmd)
else:
    cmd = sys.argv
    cmd.pop(0)

# All To Lower Case
cmd = [name.lower() for name in cmd]

# ? call new function
new(cmd)
