from xmlrpc.server import SimpleXMLRPCServer
from DriverMotor import stop, move_motors, disable_motors


def hello(name: str = "World") -> str:
    return f"Hello {name}!"


def add(x, y):
    return x + y


# set up the server
server = SimpleXMLRPCServer(("192.168.0.10", 8000), allow_none=True, logRequests=False)
# register our functions
server.register_function(hello)
server.register_function(add)

server.register_function(stop)
server.register_function(disable_motors)
server.register_function(move_motors)
# Run the server's main loop
server.serve_forever()
