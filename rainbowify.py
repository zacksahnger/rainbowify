# sponsored by neither Alex Jones nor frogs
# it's so broken dear lord
# to use it, run the script, type something in the IRC chat box, and press "Escape". it will rainbowify your message and wait for you to send it.


import threading
from time import sleep
from pynput.keyboard import Key, Controller
from pynput import keyboard


class dataStore():
    key_store = []

    def store_key(self, key):
        self.key_store.append(key)


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))

    kb.store_key(key)  # right now it stores the key press once you release it. weird i know. There's a better way to do this.

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def do_stuff(kb):
    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


kb = dataStore()
keyboard_controller = Controller()


def new_thing(key_controller, txt):
    for i in range(len(kb.key_store)):
        key_controller.press(Key.backspace)
        key_controller.release(Key.backspace)
    sleep(0.4)
    color_list = ["04", "07", "08", "03", "10", "06", "13"]  # roy g biv
    crappy_alphabet = "abcdefghijklmnopqrstuvwxyz,./'\""  # not used yet but will improve input validation
    i = 0

    for item in txt:
        if str(item).count("Key.space") > 0:
            key_controller.type(" ")
        elif str(item).count("Key.esc") > 0 or str(item).count("Key.backspace") > 0 or str(item).count("Key.shift_r") > 0 or str(item).count("Key.shift_l") > 0 or str(item).count("Key.enter") > 0:
            key_controller.type("")
        elif str(item).count("'") > 2:  # this doesn't work yet
            key_controller.type("'")
        else:
            key_controller.press(Key.ctrl)
            key_controller.press('k')
            key_controller.release(Key.ctrl)
            key_controller.release('k')
            key_controller.type(color_list[i % len(color_list)] + str(item).replace("'", ""))
            print(" color " + color_list[i % len(color_list)] + " " + str(item))
            i = i + 1


while True:
    kb.key_store.clear()
    t1 = threading.Thread(do_stuff(kb))
    t2 = threading.Thread(new_thing(keyboard_controller, kb.key_store))

    t1.start()
    t2.start()

    t1.join()  # no idea what is necessary here.
    t2.join()
