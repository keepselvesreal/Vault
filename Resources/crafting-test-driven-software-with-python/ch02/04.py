# 04_chat_spies.py

import unittest
import unittest.mock


# chat_acceptance.py

import unittest


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        user1 = ChatClient("John Doe")
        user2 = ChatClient("Harry Porter")
        user1.send_message("Hello World")
        messages = user2.fetch_messages()
        assert messages == ["John Doe: Hello World"]


class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")

        assert client.nickname == "User 1"
    
    def test_send_message(self):
        client = ChatClient("User 1")
        # client.connection = _DummyConnection()
        client.connection = unittest.mock.Mock()
        sent_message = client.send_message("Hello World")
        assert sent_message == "User 1: Hello World"

    def test_client_connectino(self):
        client = ChatClient('User 1')

        connection_spy = unittest.mock.MagicMock()
        with unittest.mock.patch.object(client, "_get_connection",
                                        return_value=connection_spy):
            client.send_message("Hello World")
        
        connection_spy.broadcast.assert_called_with("User 1: Hello World")


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        # c = Connection(("localhost", 9090))
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))
        
        # c.broadcast("some message")

        # assert c.get_messages()[-1] == "some message"

        with unittest.mock.patch.object(c, "get_messages",
                                        return_value=[]):
            c.broadcast("some message")

            assert c.get_messages()[-1] == "some message"


class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname
        self._connection = None

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        # self.connection.broadcast(message)
        self.connection.broadcast(sent_message)
        return sent_message
    
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._get_connection()
        return self._connection

    @connection.setter
    def connection(self, value):
        if self._connection is not None:
            self._connection.close()
        self._connection = value
    
    def _get_connection(self):
        return Connection(("localhost", 9090))

class _DummyConnection:
    def broadcast(*args, **kwargs):
        pass


from multiprocessing.managers import SyncManager

class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages")
        super().__init__(address=address, authkey=b"mychatsecret")
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)


if __name__ == "__main__":
    unittest.main()