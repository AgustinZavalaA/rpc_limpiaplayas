import xmlrpc.client
import pygame


def print_info(joystick) -> None:
    """Print the current information gathered from the Xbox controller input

    Args:
        joystick ([pygame joystick]): Current joystick instance
    """
    print(f"dir = {joystick.get_axis(0):.2f}")
    print(f"ret = {joystick.get_axis(2):.2f}")
    print(f"ava = {joystick.get_axis(5):.2f}")

    print(f"freno = {joystick.get_button(0):.2f}")
    print(f"garra = {joystick.get_button(1):.2f}")
    print(f"pinza = {joystick.get_button(2):.2f}")
    print(f"Horn  = {joystick.get_button(3):.2f}")
    print(f"giroI = {joystick.get_button(4):.2f}")
    print(f"giroD = {joystick.get_button(5):.2f}")
    print(f"exit  = {joystick.get_button(8):.2f}")


def main() -> None:
    pygame.init()

    # Init the server with the raspberry, also it checks the connection with a hello world
    s = xmlrpc.client.ServerProxy("http://192.168.0.10:8000")
    print(s.hello())

    # Loop until the user clicks the xbox button
    done = False

    # Initialize the joysticks
    pygame.joystick.init()
    speed = 0

    while not done:
        # Probably unnecessary evenet to get the state of the buttons
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

        # Pause the program until there is a valid controller
        if pygame.joystick.get_count() < 1:
            print("no hay control")
            while pygame.joystick.get_count() < 1:
                pass

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        print_info(joystick)

        f = lambda x: 35 * x + 35
        speed = f(joystick.get_axis(5)) - f(joystick.get_axis(2))
        # print(speed)

        y = lambda x: 30 * x
        mod = y(joystick.get_axis(0))
        # print(mod)
        print(f"i:{speed-mod:2f} d:{speed+mod:2f}")
        speed_left, speed_right = speed - mod, speed + mod

        if joystick.get_button(0):
            s.stop()
        elif joystick.get_button(4):
            s.move_motors(True, 90, True)
            s.move_motors(False, 90, False)
        elif joystick.get_button(5):
            s.move_motors(True, 90, False)
            s.move_motors(False, 90, True)
        elif speed > 0:
            speed_left, speed_right = speed_left if speed_left > 0 else 0, speed_right if speed_right > 0 else 0
            print(f"i:{speed_left:2f} d:{speed_right:2f}")

            s.move_motors(True, speed_left, True)
            s.move_motors(False, speed_right, True)
        else:
            speed_left, speed_right = speed_left if speed_left < 0 else 0, speed_right if speed_right < 0 else 0
            print(f"i:{speed_left:2f} d:{speed_right:2f}")

            s.move_motors(True, -speed_left, False)
            s.move_motors(False, -speed_right, False)

        if joystick.get_button(8):
            s.stop()
            done = True
            joystick.quit()


if __name__ == "__main__":
    main()
