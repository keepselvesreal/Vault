import unittest
from unittest import mock

from chat.client import ChatClient

from .fakeserver import FakeServer

class TestChatMessageExchange(unittest.TestCase):
    def setUp(self):
        self.fakeserver = unittest.mock.patch("multiprocessing.managers.listener_client", new={
            "pickle": (None, FakeServer())
        })
        self.fakeserver.start()

    def tearDown(self):
        self.fakeserver.stop()
    
    def test_exchange_with_server(self):
        c1 = ChatClient("User1")
        c2 = ChatClient("User2")

        c1.send_message("connected message")
        
        assert c2.fetch_messages()[-1] == "User1: connected message"