import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Motor A
PWMA = 12
AIN1 = 13
AIN2 = 15
# Motor B
PWMB = 35
BIN1 = 16
BIN2 = 18


GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

GPIO.setup(PWMA, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwmA = GPIO.PWM(PWMA, 100)  # Initialize PWM on pwmPin 100Hz frequency

GPIO.setup(PWMB, GPIO.OUT)
pwmB = GPIO.PWM(PWMB, 100)  # Initialize PWM on pwmPin 100Hz frequency

dc = 0  # set dc variable to 0 for 0%
pwmA.start(dc)  # Start PWM with 0% duty cycle
pwmB.start(dc)


def stop():
    # GPIO.output(STBY, False)
    dc = 0
    pwmA.ChangeDutyCycle(dc)
    pwmB.ChangeDutyCycle(dc)

    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)


def move_motors(motor, speed, direction):
    inPin1 = GPIO.LOW
    inPin2 = GPIO.HIGH

    if direction:
        inPin1 = GPIO.HIGH
        inPin2 = GPIO.LOW

    if motor:
        GPIO.output(AIN1, inPin1)
        GPIO.output(AIN2, inPin2)
        pwmA.ChangeDutyCycle(speed)
    else:
        GPIO.output(BIN1, inPin1)
        GPIO.output(BIN2, inPin2)
        pwmB.ChangeDutyCycle(speed)


def disable_motors():
    stop()
    pwmA.stop()  # stop PWM
    pwmB.stop()  # stop PWM
    GPIO.cleanup()  # resets GPIO ports used back to input mode
