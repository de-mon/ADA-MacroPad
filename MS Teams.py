# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Teams', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x800080, 'Mute', [Keycode.CONTROL, Keycode.SHIFT, Keycode.M]),
        (0x800080, '', [Keycode.I]),
        (0x800080, '', [Keycode.T]),
        # 2nd row ----------
        (0x800080, 'Video', [Keycode.CONTROL, Keycode.SHIFT, Keycode.O]),
        (0x800080, '', [Keycode.K]),
        (0x800080, '', [Keycode.L]),
        # 3rd row ----------
        (0x800080, '', [Keycode.ONE]),
        (0x800080, '', [Keycode.TWO]),
        (0x800080, 'End', [Keycode.CONTROL, Keycode.SHIFT, Keycode.B]),
        # 4th row ----------
        (0x101010, 'Answer', [Keycode.CONTROL, Keycode.SHIFT, Keycode.A]),
        (0x800000, '0', [Keycode.ZERO]),
        (0x101010, '#', [Keycode.POUND]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
# Write your code here :-)
# Write your code here :-)
