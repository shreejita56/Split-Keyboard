# Hardware mapping for the Rocket split keyboard.
#
# From the schematic:
#   U1 = PCA9555, A0/A1/A2 -> GND -> 0x20, bus SCL1/SDA1
#   U2 = PCA9555, A0/A1/A2 -> GND -> 0x20, bus SCL/SDA
#
# The two 0x20 devices MUST be on different I2C buses.
#
# Change ONLY the GPIO numbers below if your RP2040 routes the
# SCL/SDA nets to different GPIOs.

# Bus for the PCA9555 connected to SCL/SDA
I2C0_SDA_GPIO = 6
I2C0_SCL_GPIO = 7

# Bus for the PCA9555 connected to SCL1/SDA1
# Common RP2040 I2C1 routing used by many boards:
I2C1_SDA_GPIO = 20
I2C1_SCL_GPIO = 21

PCA9555_U2_ADDRESS = 0x20   # SCL/SDA
PCA9555_U1_ADDRESS = 0x20   # SCL1/SDA1

# Matrix connections visible in the schematic are exposed as
# PCA9555 port pins here. Adjust only if your net labels differ.
# U2 (SCL/SDA expander)
U2_ROWS = [0, 1, 2, 3, 4]
U2_COLS = [8, 9, 10, 11, 12, 13, 14, 15]

# U1 (SCL1/SDA1 expander)
U1_ROWS = [0, 1, 2, 3, 4]
U1_COLS = [8, 9, 10, 11, 12, 13, 14, 15]

DIODE_DIRECTION = "COL2ROW"

# Your direct LED data line.
# NOTE: if this means RP2040 GPIO7, it conflicts with I2C0_SCL_GPIO=7.
# In that case move I2C0_SCL_GPIO to the GPIO actually labelled SCL in
# your PCB/schematic. Do NOT run LED data and I2C SCL on the same GPIO.
LED_DATA_GPIO = 7

ENCODER_A_GPIO = 4
ENCODER_B_GPIO = 5
ENCODER_BUTTON_GPIO = 3
