def node(cmd):
    app = ""
    if cmd[1] == "rt":
        app = f"pnpx create-react-app {cmd[2]}"
    elif cmd[1] == "next":
        app = f"pnpx create-next-app@latest {cmd[2]}"
    # os.system(app)
    # os.system("code .")
    print(app)