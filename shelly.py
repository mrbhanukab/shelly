import sys
import os

os.chdir("C:/shelly/components")
import components

os.system('cls||clear')

logo()

# ! Setup Command
cmd = []
if len(sys.argv) == 1:
    cmd = list(input("How can I be of Service?: ").split())
else:
    cmd = sys.argv
    cmd.pop(0)

# All To Lower Case
cmd = [name.lower() for name in cmd]

# ? call new function
if "new" in cmd:
    new(cmd)
else:
    Open(cmd)
