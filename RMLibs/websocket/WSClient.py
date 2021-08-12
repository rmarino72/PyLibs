# install package websocket-client
import websocket
from websocket import create_connection
from RMLibs.basic.BasicObject import BasicObject


class WSClient(BasicObject):

    NO_TIMEOUT: int = 0

    __url: str or None = None
    __connected: bool = False
    __timeout: int = NO_TIMEOUT
    __ws: websocket.WebSocket = None

    @property
    def url(self) -> str:
        """
        :return: the url to connect
        """
        return self.__url

    @url.setter
    def url(self, url: str):
        """
        :parameter url: the url to connect
        """
        self.__url = url

    @property
    def connected(self) -> bool:
        """
        :return: True if the client is connected
        """
        return self.__connected

    @property
    def timeout(self) -> int:
        """
        :return: the web socket timeout in seconds
        """
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: int):
        """
        :param timeout: the timeout in seconds to set (0 = no timeout)
        """
        if timeout < self.NO_TIMEOUT:
            self.error(".timeout - Invalid timeout value")
            raise Exception("Invalid timeout value")
        self.__timeout = timeout

    def __del__(self):
        """
        destructor
        """
        if self.connected:
            self.close_connection()

    def connect(self):
        """
        opens the connection
        """
        try:
            if self.__url is None:
                raise Exception("No url is set")
            if self.connected:
                raise Exception("The web socket is connected yet")
            if self.timeout == 0:
                self.__ws = create_connection(self.url)
            else:
                self.__ws = create_connection(self.url, self.timeout)
            self.__connected = True
        except Exception as ex:
            self.error(".connect(self) - " + str(ex))
            raise ex

    def close_connection(self):
        """
        closes the web socket connection
        """
        try:
            if not self.connected:
                raise Exception("The web socket is not connected")
            self.__ws.close()
        except Exception as ex:
            self.error(".close_connection(self) - " + str(ex))
            raise ex

    def send(self, content: str, receive: bool = True):
        """
        sends the content to the server
        :param content: the content to send (string)
        :param receive: True if a response is expected by the server (default: True)
        """
        try:
            if not self.connected:
                raise Exception("The web socket is not connected")
            self.debug_verbose(".send(self, content: str, receive: bool = True) - Sending: " + content)
            self.__ws.send(content)
            if receive:
                self.received(self.__ws.recv())
        except Exception as ex:
            self.error("send(self, content: str, receive: bool = True) - " + str(ex))
            raise ex

    def received(self, content: str):
        """
        This function is invoked when a response is received by the server after a send.
        OVERRIDE it to manage the response
        :param content: the received content
        """
        self.debug_verbose(".received(self, content: str) - RECEIVED: " + content)
