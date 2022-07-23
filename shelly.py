import sys
import os
import random

sys.path.insert(0, "C:/shelly/components")
from components import *

os.system('cls||clear')

logo()

# ! Setup Command
cmd = []
text = ["How can I be of Service?", "Hi, How can I help you?", "Hey Bhanuka how can I help?", "I'm here, what can I do for You?"]
if len(sys.argv) == 1:
  text = random.choice(text) + " : "
    cmd = list(input(text).split())
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
