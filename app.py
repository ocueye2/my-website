import cherrypy
import os
import sys

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

def load(file):
    try:
        with open(os.path.join(base_dir, file)) as f:
            return f.read()
    except FileNotFoundError as e:
        print("fnf")
        return ""


class webui(object):

    @cherrypy.expose
    def index(self):
        return load("bake/index.html")

    @cherrypy.expose
    def projects(self):
        return load("bake/projects.html")

    @cherrypy.expose
    def contact(self):
        return load("bake/contact.html")

    @cherrypy.expose
    def servers(self):
        return load("bake/servers.html")

    @cherrypy.expose
    def submit(self,phone="empty",email="empty",message="empty",pref="",name=""):
        global contact
        if phone == "empty":
            return load("bake/error.html")
        else:
            f = open(f"{base_dir}/contact.html","a")
            f.write(f"""
            {{
                "name":"{name}",
                "pref":"{pref}",
                "email":"{email}",
                "phone":"{phone}",
                "message":"{message}",
            }},
            """)
            f.close()

            return load("bake/submit.html")
            

    def default(self, attr='abc'):
        return load("bake/404.html")
    default.exposed = True



if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',  # Bind to all available network interfaces
        'server.socket_port': 8080,
        'log.screen': True  ,
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }

    })
    cherrypy.quickstart(webui())
