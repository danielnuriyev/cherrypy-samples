__author__ = 'daniel.nuriyev'

import cherrypy

# this is an http server that maps urls to methods that handle them

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
    routes.connect('test','/test', controller=controller, action='test')

    # telling cherrypy to use routes
    conf = {
        '/' :
        {
            'request.dispatch' : routes,
        },
    }

    # setting the port
    cherrypy.config.update({'server.socket_port': port})

    # starting the server with the configuration
    cherrypy.quickstart(controller,'',config=conf)

