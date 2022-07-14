import os
from node import *

def logo():
    print('''
 __  __          ____   _                           _          
|  \/  |        |  _ \ | |                         | |          TM
| \  / | _ __   | |_) || |__    __ _  _ __   _   _ | | __  __ _ 
| |\/| ||  __|  |  _ < |  _ \  / _  ||  _ \ | | | || |/ / / _  |
| |  | || |  _  | |_) || | | || (_| || | | || |_| ||   < | (_| |
|_|  |_||_| (_) |____/ |_| |_| \__ _||_| |_| \__ _||_|\_\ \____|
Shelly | Version 1.5
    ''')


def new(cmd):
    if cmd[1] in ["rt", "nxt"]:
        node(cmd)
    elif cmd[1] in ["pr", "ps", "ae", "lr", "xd"]:
        print("Photoshop")
    elif cmd[1] in "py":
        print("Python")
    elif cmd[1] in "go":
        print("Go Lang")
