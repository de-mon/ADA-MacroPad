# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'YouTube', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x800000, 'Full', [Keycode.F]),
        (0x101010, 'Mini', [Keycode.I]),
        (0x800000, 'Default', [Keycode.T]),
        # 2nd row ----------
        (0x101010, 'Back', [Keycode.J]),
        (0x800000, 'Play/Pse', [Keycode.K]),
        (0x101010, 'Fwrd', [Keycode.L]),
        # 3rd row ----------
        (0x101010, '', [Keycode.ONE]),
        (0x800000, 'Mute', [Keycode.M]),
        (0x101010, '', [Keycode.THREE]),
        # 4th row ----------
        (0x101010, '', [Keycode.KEYPAD_ASTERISK]),
        (0x800000, '', [Keycode.ZERO]),
        (0x101010, '', [Keycode.POUND]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
# Write your code here :-)
