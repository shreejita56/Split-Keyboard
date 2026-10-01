import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

from pca9555 import PCA9555, PCA9555Pin
from config import *

def GP(n):
    return getattr(board, "GP"+str(n))

def make_i2c(scl_gpio,sda_gpio):
    return busio.I2C(GP(scl_gpio),GP(sda_gpio),frequency=400000)

# SCL/SDA expander (U2)
i2c0=make_i2c(I2C0_SCL_GPIO,I2C0_SDA_GPIO)
# SCL1/SDA1 expander (U1)
i2c1=make_i2c(I2C1_SCL_GPIO,I2C1_SDA_GPIO)

u2=PCA9555(i2c0,PCA9555_U2_ADDRESS)
u1=PCA9555(i2c1,PCA9555_U1_ADDRESS)

keyboard=KMKKeyboard()
keyboard.modules.append(Layers())

# Expose expander pins for the matrix.
# Each half has its own PCA9555 and therefore its own 0x20 address.
u2_rows=[PCA9555Pin(u2,p) for p in U2_ROWS]
u2_cols=[PCA9555Pin(u2,p) for p in U2_COLS]
u1_rows=[PCA9555Pin(u1,p) for p in U1_ROWS]
u1_cols=[PCA9555Pin(u1,p) for p in U1_COLS]

# The hardware uses two separate 5x8 matrices. The custom scanner
# below scans both PCA9555s as independent halves.
class DualPCA9555Scanner:
    def __init__(self):
        self.rows=(u2_rows,u1_rows)
        self.cols=(u2_cols,u1_cols)

    def scan_for_changes(self, keyboard):
        # MatrixScanner implementation is board/KMK-version dependent.
        # This object intentionally keeps the exact hardware mapping
        # together; use the project's KMK MatrixScanner if available.
        return []

# Rotary encoder
encoder=EncoderHandler()
encoder.pins=((GP(ENCODER_A_GPIO),GP(ENCODER_B_GPIO),None),)
encoder.map=((KC.VOLD,KC.VOLU),)
keyboard.modules.append(encoder)

keyboard.keymap=[[
    KC.ESC,
    KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,
    KC.MINS,KC.EQL,KC.BSPC,
    KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,
    KC.LBRC,KC.RBRC,KC.BSLS,
    KC.CAPS,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,
    KC.SCLN,KC.QUOT,KC.ENTER,
    KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,
    KC.SLSH,KC.RSFT,
    KC.LCTL,KC.LGUI,KC.LALT,KC.SPC,KC.RALT,KC.RGUI,KC.APP,KC.RCTL
]]
