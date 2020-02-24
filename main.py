import socket
from enum import Enum  # I think we'll find enums useful for enumerating the raw IRC
import configparser as cp
import io


class Connector(io.RawIOBase):  # placeholder, we wont end up extending this, possibly extend an asyncio class?
    def __init__(self):
        super().__init__()
        # fetch all the network parameters
        self.config = cp.RawConfigParser().read('config/config.properties')
        self.server = self.config.get('network', 'server')
        self.port = self.config.get('network', 'port')
        if self.config.get('network', 'tls'):
            with open(self.config.get('network', 'cert'), 'rb') as r:
                self.cert = r.read()
        # fetch all the IRC parameters
        self.nick = self.config.get('irc', 'nick')
        self.user = self.config.get('irc', 'user')
        self.real = self.config.get('irc', 'real')
        self.auth = self.config.get('irc', 'auth')



