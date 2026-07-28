import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

keyboard.row_pins = (
    # LEFT SIDE
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,

    # RIGHT SIDE
    board.GP28, board.GP27, board.GP26, board.GP22, board.GP21,
    # pin 1   # pin 2       # pin 3     # pin 4     # pin 5
)

keyboard.col_pins = (
    # LEFT SIDE
    board.GP11, board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5,

    # RIGHT SIDE
    board.GP20, board.GP19, board.GP18, board.GP17, board.GP16, board.GP15, board.GP14,
    # pin 6   # pin 7       # pin 8     # pin 9     # pin 10    # pin 11    # pin 12
)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.modules.append(Layers())

TRANS = KC.TRNS # Creates a transparent Key. Transparent Keys are pressed through the upper layer to the lower layer.
LAYER = KC.MO(1) # Momentarily activate LAYER 1 until released

keyboard.keymap = [
    [   # LAYER 0 - Base Layer
        # LEFT SIDE                                                                         # RIGHT SIDE (THIS TOP PART DOES NOTHING)
        KC.GRAVE,     KC.N1,     KC.N2,    KC.N3,      KC.N4,      KC.N5,      KC.NO,       KC.NO,       KC.NO,      KC.NO,      KC.NO,       KC.NO,     KC.NO,        KC.NO,
        KC.TAB,       KC.Q,      KC.W,     KC.E,       KC.R,       KC.T,       KC.NO,       KC.NO,       KC.NO,      KC.NO,      KC.NO,       KC.NO,     KC.NO,        KC.NO,
        KC.LSHIFT,    KC.A,      KC.S,     KC.D,       KC.F,       KC.G,       KC.NO,       KC.NO,       KC.NO,      KC.NO,      KC.NO,       KC.NO,     KC.NO,        KC.NO,
        KC.LCTRL,     KC.Z,      KC.X,     KC.C,       KC.V,       KC.B,       LAYER,       KC.NO,       KC.NO,      KC.NO,      KC.NO,       KC.NO,     KC.NO,        KC.NO,
        KC.NO,        KC.NO,     KC.NO,    KC.HOME,    KC.LGUI,    KC.LALT,    KC.SPACE,    KC.NO,       KC.NO,      KC.NO,      KC.NO,       KC.NO,     KC.NO,        KC.NO,
        # LEFT SIDE (THIS BOTTOM PART DOES NOTHING)                                         # RIGHT SIDE
        KC.NO,        KC.NO,     KC.NO,    KC.NO,      KC.NO,      KC.NO,      KC.NO,       KC.NO,       KC.N6,      KC.N7,      KC.N8,       KC.N9,     KC.N0,        KC.DEL,
        KC.NO,        KC.NO,     KC.NO,    KC.NO,      KC.NO,      KC.NO,      KC.NO,       KC.NO,       KC.Y,       KC.U,       KC.I,        KC.O,      KC.P,         KC.BSLASH,
        KC.NO,        KC.NO,     KC.NO,    KC.NO,      KC.NO,      KC.NO,      KC.NO,       KC.NO,       KC.H,       KC.J,       KC.K,        KC.L,      KC.SCOLON,    KC.QUOTE,
        KC.NO,        KC.NO,     KC.NO,    KC.NO,      KC.NO,      KC.NO,      KC.NO,       LAYER,       KC.N,       KC.M,       KC.COMMA,    KC.DOT,    KC.SLASH,     KC.PSCREEN,
        KC.NO,        KC.NO,     KC.NO,    KC.NO,      KC.NO,      KC.NO,      KC.NO,       KC.BSPACE,   KC.RALT,    KC.LGUI,    KC.END,      KC.NO,     KC.NO,        KC.NO,
    ],
    [   # LAYER 1 - Special Characters and secondary actions
        # LEFT SIDE BEGINS HERE                                                             # RIGHT SIDE (THIS TOP PART DOES NOTHING)
        KC.ESC,    KC.F1,      KC.F2,      KC.F3,       KC.F4,    KC.F5,          KC.NO,    KC.NO,       KC.NO,          KC.NO,    KC.NO,     KC.NO,       KC.NO,       KC.NO,
        TRANS,     KC.NO,      KC.UP,      KC.NO,       KC.NO,    KC.LBRACKET,    KC.NO,    KC.NO,       KC.NO,          KC.NO,    KC.NO,     KC.NO,       KC.NO,       KC.NO,
        TRANS,     KC.LEFT,    KC.DOWN,    KC.RIGHT,    KC.NO,    KC.NO,          KC.NO,    KC.NO,       KC.NO,          KC.NO,    KC.NO,     KC.NO,       KC.NO,       KC.NO,
        TRANS,     KC.NO,      KC.CAPS,    KC.NO,       KC.NO,    KC.NO,          KC.NO,    KC.NO,       KC.NO,          KC.NO,    KC.NO,     KC.NO,       KC.NO,       KC.NO,
        KC.NO,     KC.NO,      KC.NO,      TRANS,       TRANS,    TRANS,          TRANS,    KC.NO,       KC.NO,          KC.NO,    KC.NO,     KC.NO,       KC.NO,       KC.NO,
        # LEFT SIDE (THIS BOTTOM PART DOES NOTHING)                                         # RIGHT SIDE
        KC.NO,     KC.NO,      KC.NO,      KC.NO,       KC.NO,    KC.NO,          KC.NO,    KC.NO,       KC.F6,          KC.F7,    KC.F8,     KC.F9,       KC.F10,      KC.F11,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,       KC.NO,    KC.NO,          KC.NO,    KC.NO,       KC.RBRACKET,    KC.NO,    KC.NO,     KC.MINUS,    KC.EQUAL,    KC.F12,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,       KC.NO,    KC.NO,          KC.NO,    KC.NO,       KC.NO,          KC.NO,    KC.NO,     KC.NO,       KC.NO,       KC.NO,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,       KC.NO,    KC.NO,          KC.NO,    KC.NO,       KC.NO,          KC.NO,    KC.NO,     KC.NO,       KC.NO,       KC.NO,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,       KC.NO,    KC.NO,          KC.NO,    KC.ENTER,    TRANS,          TRANS,    TRANS,     KC.NO,       KC.NO,       KC.NO,
    ]
]

keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
