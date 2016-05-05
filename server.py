__author__ = 'daniel.nuriyev'

import cherrypy

from cherrypy.lib import auth_basic

# this is an http server that maps urls to methods that handle them

def validate_password(realm, username, password):

    if username == 'hacker':
        return True
    else:
        return False

# controller for handling http requests
class Controller(object):

    # will return a 200 with text 'ok'
    def test(self):
        return 'ok'

if __name__ == '__main__':

    # get port number from the command line
    port = int(input("port:"))

    # methods in this class will handle http requests
    controller = Controller()

    # using routes: https://routes.readthedocs.org/en/latest/
    # using routes to map urls to methods
    routes = cherrypy.dispatch.RoutesDispatcher()
    routes.mapper.explicit = True

    # method test of the controller object will handle url: http://<ip or host>:port/test
    routes.connect('test',  '/test',    controller=controller, action='test')
    routes.connect('admin', '/admin',   controller=controller, action='test')

    # setting the port
    cherrypy.config.update({
            'server.socket_host': '0.0.0.0',    # listens to all IPs and domain names. Without this will only respond to 127.0.0.1 and localhost
            'server.socket_port': port,
        })

    # telling cherrypy to use routes
    conf = {
        '/':{
            'request.dispatch' : routes
        },
        '/admin':{
           'tools.auth_basic.on': True,
           'tools.auth_basic.realm': 'localhost',
           'tools.auth_basic.checkpassword': validate_password
        }
    }

    # starting the server with the configuration
    cherrypy.quickstart(controller, '', config = conf)

