# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', [Keycode.SEVEN]),
        (0x202000, '8', [Keycode.EIGHT]),
        (0x202000, '9', [Keycode.NINE]),
        # 2nd row ----------
        (0x202000, '4', [Keycode.FOUR]),
        (0x202000, '5', [Keycode.FIVE]),
        (0x202000, '6', [Keycode.SIX]),
        # 3rd row ----------
        (0x202000, '1', [Keycode.ONE]),
        (0x202000, '2', [Keycode.TWO]),
        (0x202000, '3', [Keycode.THREE]),
        # 4th row ----------
        (0x101010, '*', [Keycode.KEYPAD_ASTERISK]),
        (0x800000, '0', [Keycode.ZERO]),
        (0x101010, '#', [Keycode.POUND]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
