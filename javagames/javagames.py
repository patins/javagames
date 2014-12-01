from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from autobahn.twisted.resource import WSGIRootResource
from twisted.internet import reactor

import compilation_site
import game_connector

import config

if __name__ == '__main__':
    compilation_site.app.debug = True
    wsgi_app = WSGIResource(reactor, reactor.getThreadPool(), compilation_site.app)

    root = WSGIRootResource(wsgi_app, {'game_': game_connector.game_resource})

    reactor.listenTCP(config.PORT, Site(root))

    reactor.run()
