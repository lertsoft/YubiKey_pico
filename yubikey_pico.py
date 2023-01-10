import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

time.sleep(1)
keyboard_layout.write("STRANGE")
keyboard.press(Keycode.ENTER)
time.sleep(.09)
keyboard.release(Keycode.ENTER)

