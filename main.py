import sys
import os
from components import *

logo()

cmd = ""
if len(sys.argv) == 1:
    cmd = input('How can I be of Service?:')
else:
    cmd = sys.argv

os.chdir('D:\Projects')
os.chdir(cmd[2].capitalize())

if "new" in cmd:
    cmd = input('How can I be of Service?:') #!To be continued
else:
    cmd = sys.argv