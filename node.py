import os

os.chdir('D:\Projects')


def node(cmd):
    os.chdir(cmd[1])
    app = ""
    if cmd[1] == "react":
        app = f"pnpx create-react-app@latest {cmd[2]}"
    elif cmd[1] == "next":
        app = f"pnpx create-next-app@latest {cmd[2]}"
    os.system(app)
    os.chdir(cmd[2])
    os.system("code .")
