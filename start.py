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
    def submit(self,phone="empty",email="empty",message="empty",pref=""):
        if phone == "empty":
            return load("bake/error.html")
        else:
            return load("bake/submit.html")

    def default(self, attr='abc'):
        return "Page not Found!"
    default.exposed = True


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_port': 1232,
        'log.screen': False  
    })
    cherrypy.quickstart(webui())
