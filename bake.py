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
        <!DOCTYPE html>
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
html = ""
for catogory in os.listdir(f"{os.path.dirname(sys.argv[0])}/card_data"):
    html += f'''
    <div class="glass">
    <h1> {catogory}: </h1>
   <div class="cardcon {catogory}"> '''
    for item in os.listdir(f"{os.path.dirname(sys.argv[0])}/card_data/{catogory}"):
        f = open(f"{os.path.dirname(sys.argv[0])}/card_data/{catogory}/{item}")
        html += f.read()
        f.close()
    html += f'</div> </div>'
path = os.path.dirname(sys.argv[0])
page = f"""
 <!DOCTYPE html>
    <head>
        <title>My Stuff</title>
        <link rel="icon" type="image/x-icon" href="https://carsonmayn.com/static/favicon.png">
        <style>
        {load(f"css/cards.css")}
        {load(f"other/all.css")}
        {load(f"other/nav.css")}
        </style>
    </head>
    <body>
    {load(f"other/nav.html")}
    <br>
    <br>
    <br>
    {html}
    <script>
        console.log("inspect element is not hacking my website")
        {load(f"js/cards.js")}
        </script>
    
    </body>
 """
f = open(f"{path}/bake/cards.html","w")
f.write(page)
f.close()
    
print("----------")
print("done")