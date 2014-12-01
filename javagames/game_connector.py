from twisted.internet import protocol
from twisted.internet import reactor

from txsockjs.factory import SockJSResource

import game_manager

class GameProcessProtocol(protocol.ProcessProtocol):
    def __init__(self, socket):
        self.socket = socket
        self.active = True
    def outReceived(self, data):
        self.socket.transport.write(data)
    def errReceived(self, data):
        self.socket.transport.write(data)
    def processExited(self, reason):
        self.active = False
        if self.socket.transport:
            self.socket.transport.loseConnection()
    def processEnded(self, reason):
        self.active = False
        if self.socket.transport:
            self.socket.transport.loseConnection()

class GameProtocol(protocol.Protocol):
    def connectionMade(self):
        self.is_initialized = False
    def dataReceived(self, message):
        if self.is_initialized:
            self.process.transport.write(message.encode('ascii') + '\n')
        else:
            game_id = message
            if int(game_id) not in game_manager.get_valid_game_ids():
                self.close()
                return
            self.process = GameProcessProtocol(self)
            reactor.spawnProcess(self.process, 'java', ['java', '-cp', game_manager.get_class_path(game_id), game_manager.get_class_name(game_id)])
            self.is_initialized = True
    def connectionLost(self, reason):
        if self.process.active:
            self.process.transport.signalProcess('KILL')

game_resource = SockJSResource(protocol.Factory.forProtocol(GameProtocol))
