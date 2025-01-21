import unittest
import unittest.mock

from chat.client import Connection
from chat.server import FakeServer

class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")
            messages = c.get_messages()
        
        assert messages[-1] == "some message"

    def test_exchange_with_server(self):
        with unittest.mock.patch("multiprocessing.managers.listener_client", new={
            "pickle": (None, FakeServer())
        }):
            c1 = Connection(("localhost", 9090))
            c2 = Connection(("localhost", 9090))

            c1.broadcast("connected message")
            
            assert c2.get_messages()[-1] == "connected message"