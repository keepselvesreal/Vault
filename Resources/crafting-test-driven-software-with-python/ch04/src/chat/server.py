from multiprocessing.managers import SyncManager, ListProxy


class FakeServer:
    def __init__(self):
        self.last_command = None
        self.messages = []

    def __call__(self, *args, **kwargs):
        return self

    def send(self, data):
        callid, command, args, kwargs = data
        self.last_command = command
        self.last_args = args

    def recv(self, *args, **kwargs):
        if self.last_command == "dummy":
            return "#RETURN", None
        elif self.last_command == "create":
            return "#RETURN", ("fakeid", tuple())
        elif self.last_command == "append":
            self.messages.append(self.last_args[0])
            return "#RETURN", None
        elif self.last_command == "__getitem__":
            return "#RETURN", self.messages[self.last_args[0]]
        elif self.last_command in ("incref", "decref", "accept_connection"):
            return "#RETURN", None
        else:
            return "#ERROR", ValueError("%s - %r" % (self.last_command, self.last_args))

    def close(self):
        pass


_messages = []
def _srv_get_messages():
    return _messages
class _ChatServerManager(SyncManager):
    pass
_ChatServerManager.register("get_messages",
                            callable=_srv_get_messages,
                            proxytype=ListProxy)

def new_chat_server():
    return _ChatServerManager(("", 9090), authkey=b"mychatsecret")