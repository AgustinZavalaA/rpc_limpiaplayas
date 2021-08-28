from xmlrpc.server import SimpleXMLRPCServer


def hello(name: str = "World") -> str:
    return f"Hello {name}!"


def add(x, y):
    return x + y


def stop_motors():
    return "DETENIENDO"


def move_motors():
    return "AVANZANDO"


def disable_motors():
    return "APAGAOO"


# set up the server
server = SimpleXMLRPCServer(("192.168.0.10", 8000))
# register our functions
server.register_function(hello)
server.register_function(add)
server.register_function(stop_motors)
server.register_function(move_motors)
server.register_function(disable_motors)
# Run the server's main loop
server.serve_forever()
