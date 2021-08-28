import xmlrpc.client
import pygame


def print_info(joystick):
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


def main():
    pygame.init()

    s = xmlrpc.client.ServerProxy("http://192.168.0.10:8000")
    print(s.hello())

    # Loop until the user clicks the close button.
    done = False

    # Initialize the joysticks
    pygame.joystick.init()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

        if pygame.joystick.get_count() < 1:
            print("no hay control")
            while pygame.joystick.get_count() < 1:
                pass

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        print_info(joystick)

        s.move(True, 100, True)

        if joystick.get_button(8):
            done = True


if __name__ == "__main__":
    main()
