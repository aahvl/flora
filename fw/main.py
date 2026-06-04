import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()

keyboard.col_pins = (board.D1, board.D2, board.D5)
keyboard.row_pins = (board.D3, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X)],
    [KC.NO, KC.NO, KC.NO],
]

encoder_handler.pins = ((board.D3, board.D4, board.D5),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

if __name__ == "__main__":
    keyboard.go()