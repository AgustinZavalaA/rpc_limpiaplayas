from typing import List, Tuple
from xmlrpc.server import SimpleXMLRPCServer
from Motors import Motors
from ArduinoSerialComm import ArduinoComm
import time
from multiprocessing import Process, Pipe
from CameraProcessing import (
    process_video_detect_mp_function,
    process_video_detect_mp_handler_function,
)
from DatasetCreator import DatasetCreator


class ServerObjects:
    motors = Motors()
    arduino = ArduinoComm()
    camera = DatasetCreator(0)
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

    def close_camera(self) -> None:
        self.camera.release()

    def update_camera(self) -> None:
        self.camera.update()

    def save_frame(self) -> None:
        self.camera.save_frame()


def server_function():
    server = SimpleXMLRPCServer(
        ("192.168.0.10", 8000), allow_none=True, logRequests=False
    )
    server.register_instance(ServerObjects())
    server.serve_forever()


def main():
    # NORMAL WAY
    # set up the server
    server = SimpleXMLRPCServer(
        ("192.168.0.11", 8000), allow_none=True, logRequests=False
    )

    # register our functions
    server.register_instance(ServerObjects())
    # Run the server's main loop
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")

    # Multiprocessing
    # parent_conn, child_conn = Pipe()

    # video_stream = Process(target=process_video_detect_mp_function, args=(child_conn,))
    # video_handler = Process(target=process_video_detect_mp_handler_function, args=(parent_conn,))
    # rpc_server = Process(target=server_function)

    # video_stream.start()
    # video_handler.start()
    # rpc_server.start()
    # try:
    #     video_stream.join()
    #     video_handler.join()
    #     rpc_server.join()
    # except KeyboardInterrupt:
    #     print("bye bye")
    #     rpc_server.terminate()
    #     video_stream.terminate()
    #     video_handler.terminate()


if __name__ == "__main__":
    main()
