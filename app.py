import cherrypy
import os
import sys

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
host = f"{base_dir}/website"

def load(file):
    try:
        with open(os.path.join(base_dir, file)) as f:
            return f.read()
    except FileNotFoundError as e:
        print("fnf")
        return ""


class webui(object):

    @cherrypy.expose
    def portfolio(self):
        return load("bake/portfolio.html")

    @cherrypy.expose
    def index(self):
        return load("bake/index.html")

    @cherrypy.expose
    def stuff(self):
        return load("bake/stuff.html")

    @cherrypy.expose
    def contact(self):
        return load("bake/contact.html")


    @cherrypy.expose
    def Maintenence(self):
        return load("bake/gitserver.html")

    @cherrypy.expose
    def submit(self, honeypot="empty", email="empty", message="empty", pref="", name="",findus=""):
        global contact
        phone = honeypot
        if phone == "empty":
            return load("bake/error.html")
        elif not findus == "":
            with open(f"{base_dir}/botinfo.html", "a") as f:
                cherrypy.response.status = 502
                f.write(f"""
                {{
                    "name": "{name}",
                    "pref": "{pref}",
                    "email": "{email}",
                    "phone": "{phone}",
                    "message": "{message}",
                }},
                """)
            return load("fakegateway.html")
        else:
            with open(f"{base_dir}/contact.html", "a") as f:
                f.write(f"""
                {{
                    "name": "{name}",
                    "pref": "{pref}",
                    "email": "{email}",
                    "phone": "{phone}",
                    "message": "{message}",
                }},
                """)
            return load("bake/submit.html")

    def default(self, attr='abc'):
        return load("bake/404.html")
    default.exposed = True


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    host = f"{base_dir}/website"
    
    # Configuration to serve static files from ./static directory
    config = {
        '/': {
            'tools.staticdir.root': base_dir
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }
    
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',  # Bind to all available network interfaces
        'server.socket_port': 8080,
        'log.screen': True,
    })
    cherrypy.quickstart(webui(), '/', config)