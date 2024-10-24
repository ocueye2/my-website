import os
import sys
import time

def load(file):
    path = os.path.dirname(sys.argv[0])
    try:
        f = open(f"{path}/{file}")
        out = f.read()
        f.close()
        return out
    except:
        return ""

def bake():
    path = os.path.dirname(sys.argv[0])
    of = len(os.listdir(f"{path}/html"))
    for n,i in enumerate(os.listdir(f"{path}/html")):
        print(f"makeing {i} ({n + 1}/{of})")
        name = i.split(".")[0]

        out = f"""
        <html>
    <head>
        <title>{i.split(".")[0]}</title>
        <link rel="icon" type="image/x-icon" href="https://carsonmayn.com/static/favicon.png">
        <style>
        {load(f"css/{name}.css")}
        {load(f"other/all.css")}
        {load(f"other/nav.css")}
        </style>
    </head>
    <body>
    {load(f"other/nav.html")}
    {load(f"html/{name}.html")}
    <script>
        console.log("inspect element is not hacking my website")
        {load(f"js/{name}.js")}
        </script>
    
    </body>
        """
        try:
            f = open(f"{path}/bake/{name}.html","x")
        except:
            print(f"overwriteing {i}")
            f = open(f"{path}/bake/{name}.html","w")
        f.write(out)
        f.close()



print("starting")
print("----------")
bake()
print("----------")
print("done")