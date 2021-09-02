from xmlrpc.server import SimpleXMLRPCServer
from Motors import Motors


class DriverMotors:
    motors = Motors()

    def move_motors(self, motor: bool, speed: int, direction: bool) -> None:
        self.motors.move(motor, speed, direction)

    def disable_motors(self) -> None:
        self.motors.disable()

    def stop_motors(self) -> None:
        self.motors.stop()


# set up the server
server = SimpleXMLRPCServer(("192.168.0.10", 8000), allow_none=True, logRequests=False)

# register our functions
server.register_instance(DriverMotors())
# Run the server's main loop
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Exiting")
