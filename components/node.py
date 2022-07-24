import os

os.chdir('D:\Projects')


def node(cmd):
    os.chdir(cmd[1])
    app = ""
    if cmd[1] == "react":
      if "-npm" in cmd:
        app = f"npx create-react-app@latest {cmd[2]}"
      else:
        app = f"pnpx create-react-app@latest {cmd[2]}"
    elif cmd[1] == "next":
        if "-npm" in cmd:
        app = f"npx create-next-app@latest {cmd[2]}"
      else:
        app = f"pnpx create-next-app@latest {cmd[2]}"
    os.system(app)
    os.chdir(cmd[2])
    os.system("code .")
