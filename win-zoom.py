# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Zoom', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0000FF, 'Mute', [Keycode.ALT, Keycode.A]),
        (0x0000FF, '', [Keycode.I]),
        (0x0000FF, '', [Keycode.ALT,]),
        # 2nd row ----------
        (0x0000FF, 'Video', [Keycode.CONTROL, Keycode.ALT, Keycode.V]),
        (0x0000FF, '', [Keycode.K]),
        (0x0000FF, 'Camera', [Keycode.ALT, Keycode.N]),
        # 3rd row ----------
        (0x0000FF, '', [Keycode.ONE]),
        (0x0000FF, '', [Keycode.TWO]),
        (0x0000FF, 'End', [Keycode.ALT, Keycode.Q]),
        # 4th row ----------
        (0x101010, '', [Keycode.CONTROL, Keycode.SHIFT, Keycode.A]),
        (0x800000, '', [Keycode.ZERO]),
        (0x101010, '', [Keycode.POUND]),
        # Encoder button ---
        (0x000000, '', [Keycode.ALT, Keycode.Q])
    ]
}
# Write your code here :-)
# Write your code here :-)
