import serial
import time

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    ser.flush()
    time.sleep(3)
    try:
        while True:
            ser.write(b"1")
            time.sleep(0.25)
            # works with sleep 1
            line = ser.readline().decode("ascii").rstrip()

            print("u1 = " + line)
    except KeyboardInterrupt:
        ser.close()
