from xmlrpc.server import SimpleXMLRPCServer
from Motors import Motors


def hello(name: str = "World") -> str:
    return f"Hello {name}!"


def add(x, y):
    return x + y


# set up the server
server = SimpleXMLRPCServer(("192.168.0.10", 8000), allow_none=True)
# register our functions
server.register_function(hello)
server.register_function(add)
server.register_instance(Motors())
# Run the server's main loop
server.serve_forever()
