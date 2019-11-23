import time


# from pynput.keyboard import Key, Controller
# keyboard = Controller()

from pynput.mouse import Button, Controller
mouse = Controller()



time.sleep(2)

count = 0
while True:
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)
    count += 1
    print("press mouse " + str(count))

