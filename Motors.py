import RPi.GPIO as GPIO
import time


class Motors:
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BOARD)

        # Motor A
        self.PWMA = 12
        self.AIN1 = 13
        self.AIN2 = 15
        # Motor B
        self.PWMB = 35
        self.BIN1 = 16
        self.BIN2 = 18

        GPIO.setup(self.AIN1, GPIO.OUT)
        GPIO.setup(self.AIN2, GPIO.OUT)
        GPIO.setup(self.BIN1, GPIO.OUT)
        GPIO.setup(self.BIN2, GPIO.OUT)

        GPIO.setup(self.PWMA, GPIO.OUT)  # Set GPIO pin 12 to output mode.
        self.pwmA = GPIO.PWM(self.PWMA, 100)  # Initialize PWM on pwmPin 100Hz frequency

        GPIO.setup(self.PWMB, GPIO.OUT)
        self.pwmB = GPIO.PWM(self.PWMB, 100)  # Initialize PWM on pwmPin 100Hz frequency

        dc = 0  # set dc variable to 0 for 0%
        self.pwmA.start(dc)  # Start PWM with 0% duty cycle
        self.pwmB.start(dc)

    def stop(self) -> None:
        # GPIO.output(STBY, False)
        dc = 0
        self.pwmA.ChangeDutyCycle(dc)
        self.pwmB.ChangeDutyCycle(dc)

        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.LOW)

    def move(self, motor: bool, speed: int, direction: bool) -> None:
        in_pin1 = GPIO.LOW
        in_pin2 = GPIO.HIGH

        if direction:
            in_pin1 = GPIO.HIGH
            in_pin2 = GPIO.LOW

        if motor:
            GPIO.output(self.AIN1, in_pin1)
            GPIO.output(self.AIN2, in_pin2)
            self.pwmA.ChangeDutyCycle(speed)
        else:
            GPIO.output(self.BIN1, in_pin1)
            GPIO.output(self.BIN2, in_pin2)
            self.pwmB.ChangeDutyCycle(speed)

    def disable(self) -> None:
        self.stop()
        self.pwmA.stop()  # stop PWM
        self.pwmB.stop()  # stop PWM
        GPIO.cleanup()  # resets GPIO ports used back to input mode


def main() -> None:
    motors = Motors()
    try:
        while True:
            motors.move(True, 100, True)
            motors.move(False, 100, True)
            time.sleep(1.2)

            motors.stop()
            time.sleep(1)

            motors.move(True, 100, False)
            motors.move(False, 100, False)
            time.sleep(1.2)

            motors.stop()
            time.sleep(1)
    except KeyboardInterrupt:
        motors.disable()


if __name__ == "__main__":
    main()
