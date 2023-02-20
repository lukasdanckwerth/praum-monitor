from time import sleep
from Controller import Controller
from Server import run_server

if __name__ == '__main__':
    print("\nPress CTRL+C to abort.\n")

    run_server()

    print("Initializing controller")
    controller = Controller()

    try:
        print("Controller will loop forever\n")
        while True:
            controller.loop()
            sleep(1)  # avoid overloading cpu
            print("loop_count: " + str(controller.loop_count), end="\r")

    except KeyboardInterrupt:
        print("User abort.")
        exit(0)

    except Exception as e:
        print("Error: " + str(e))
        exit(1)
