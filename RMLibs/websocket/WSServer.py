# install package websocket
# install package websocket-client


import websocket
import websockets
import asyncio
from RMLibs.basic.BasicObject import BasicObject


class WSServer(BasicObject):
    NO_TIMEOUT: int = 0

    __url: str = "localhost"
    __port: int = 80
    __connected: bool = False
    __timeout: int = NO_TIMEOUT

    @property
    def url(self) -> str:
        """
        :return: the server url
        """
        return self.__url

    @url.setter
    def url(self, url: str):
        """
        :parameter url: the server url (default: "localhost")
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

    @property
    def port(self) -> int:
        """
        :return: the server port number
        """
        return self.__port

    @port.setter
    def port(self, port: int):
        """
        :param port:
        """
        if port <= 0:
            self.error(".port - Invalid port number")
            raise Exception("Invalid port number")
        self.__port = port

    def run(self):
        """
        Starts the WS Server
        """
        try:
            start_server = websockets.serve(self.__handle_content, self.url, self.port)
            asyncio.get_event_loop().run_until_complete(start_server)
            asyncio.get_event_loop().run_forever()
        except Exception as ex:
            self.error("run(self) - " + str(ex))
            raise ex

    async def __handle_content(self, web_socket: websocket.WebSocket, path: str):
        """
        Private method invoked when a message is received
        :param web_socket: the web socket
        :param path: the path
        :return:
        """
        self.debug_verbose(".__handle_content(self, web_socket: websocket.WebSocket, path: str) - Got something from "
                           + path)
        message = await web_socket.recv()
        await self.received_message(web_socket, message)

    async def received_message(self, web_socket: websocket.WebSocket, content: str):
        """
        Received message handles: OVERRIDE this method to customize the response
        :param web_socket: the web socket from which the message is received
        :param content: the content of the message
        :return:
        """
        self.debug_verbose(".received_message(self, web_socket: websocket.WebSocket, content:str) - got: " + content)
        await web_socket.send(content)
