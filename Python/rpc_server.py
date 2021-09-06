from typing import List, Tuple
from xmlrpc.server import SimpleXMLRPCServer
from Motors import Motors
from ArduinoSerialComm import ArduinoComm
import time


class ServerObjects:
    motors = Motors()
    arduino = ArduinoComm()
    time.sleep(2)
    print("Arduino y motores listos")

    def move_motors(self, motor: bool, speed: int, direction: bool) -> None:
        self.motors.move(motor, speed, direction)

    def disable_motors(self) -> None:
        self.motors.disable()

    def stop_motors(self) -> None:
        self.motors.stop()

    def communicate_arduino(self, data: str = "1") -> Tuple[int, int, List[str]]:
        return self.arduino.communicate(data)

    def close_arduino(self) -> None:
        self.arduino.close()


# set up the server
server = SimpleXMLRPCServer(("192.168.0.10", 8000), allow_none=True, logRequests=False)

# register our functions
server.register_instance(ServerObjects())
# Run the server's main loop
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Exiting")
