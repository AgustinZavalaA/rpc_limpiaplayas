from typing import List, Tuple
import serial
import time


class ArduinoComm:
    def __init__(self, port: str = "/dev/ttyACM0", baudrate: int = 115200, timeout: float = 0.5) -> None:
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.ser.flush()

    def communicate(self, data: str = "1") -> Tuple[int, int, List[str]]:
        self.ser.write(data.encode("ascii"))
        if data != "1":
            return 0, 0, []

        line = self.ser.readline().decode("ascii").rstrip()
        line_list = line.split(",")
        return int(line_list[0]), int(line_list[1]), line_list[2:]

    def close(self) -> None:
        self.ser.close()


def main():
    arduino = ArduinoComm()
    time.sleep(0.5)

    # print(arduino.communicate())
    # print(arduino.communicate("2"))
    # time.sleep(3)
    try:
        while True:
            print(arduino.communicate())
            time.sleep(0.1)
    except KeyboardInterrupt:
        arduino.close()


if __name__ == "__main__":
    # ser = serial.Serial("/dev/ttyACM0", 115200, timeout=0.1)
    # ser.flush()
    # time.sleep(3)
    # try:
    #     while True:
    #         ser.write(b"1")
    #         time.sleep(0.1)
    #         # works with sleep 1
    #         line = ser.readline().decode("ascii").rstrip()

    #         print(line.split(","))
    # except KeyboardInterrupt:
    #     ser.close()
    main()
