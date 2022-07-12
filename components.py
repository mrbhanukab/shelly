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


def node(cmd):
    app = ""
    if cmd[2] == "react":
        app = "pnpx create-react-app " + cmd[3]
    elif cmd[2] == "next":
        app = "pnpx create-next-app@latest " + cmd[3]
    os.system(app)
    os.system("code .")
