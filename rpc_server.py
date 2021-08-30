from xmlrpc.server import SimpleXMLRPCServer
from Motors import Motors

# from DriverMotor import stop, move_motors, disable_motors


def hello(name: str = "World") -> str:
    return f"Hello {name}!"


def add(x, y):
    return x + y


class DriverMotors:
    motors = Motors()

    def move(self, motor: bool, speed: int, direction: bool) -> None:
        self.motors.move(motor, speed, direction)

    def disable_motors(self) -> None:
        self.motors.disable()

    def stop_motors(self) -> None:
        self.motors.stop()


# set up the server
server = SimpleXMLRPCServer(("192.168.0.10", 8000), allow_none=True, logRequests=False)
# register our functions
server.register_function(hello)
server.register_function(add)

# server.register_function(stop)
# server.register_function(disable_motors)
# server.register_function(move_motors)
server.register_instance(DriverMotors())
# Run the server's main loop
server.serve_forever()
