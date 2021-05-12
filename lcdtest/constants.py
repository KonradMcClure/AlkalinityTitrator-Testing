

# user choice options
ROUTINE_OPTIONS = {
    1: 'Run titration',
    2: 'Calibrate sensors',
    3: 'Prime Pump',
    4: 'Update settings',
    5: 'Test Mode',
    6: 'Exit'
}

# Define GPIO to LCD mapping
LCD_RS = 27
LCD_E  = 22
LCD_D4 = 18
LCD_D5 = 23
LCD_D6 = 24
LCD_D7 = 25
LCD_ON = 15

# Keypad values
KEY_0 = 10
KEY_1 = 11
KEY_2 = 12
KEY_3 = 13
KEY_4 = 14
KEY_5 = 15
KEY_6 = 16
KEY_7 = 17
KEY_8 = 18
KEY_9 = 19
KEY_A = 20
KEY_B = 21
KEY_C = 22
KEY_D = 23
KEY_STAR = 24
KEY_HASH = 25

# Keypad Pins
# KEY_ROW_0 = 1
# KEY_ROW_1 = 6
# KEY_ROW_2 = 5
# KEY_ROW_3 = 19

# KEY_COL_0 = 16
# KEY_COL_1 = 26
# KEY_COL_2 = 20
# KEY_COL_3 = 21

# Key Indexes
# KEY_ROW_0 = 0
# KEY_ROW_1 = 1
# KEY_ROW_2 = 2
# KEY_ROW_3 = 3

# KEY_COL_0 = 0
# KEY_COL_1 = 1
# KEY_COL_2 = 2
# KEY_COL_3 = 3

KEY_VALUES = {
  0: {
    0: KEY_1,
    1: KEY_2,
    2: KEY_3,
    3: KEY_A,
  },

  1: {
    0: KEY_4,
    1: KEY_5,
    2: KEY_6,
    3: KEY_B,
  },

  2: {
    0: KEY_7,
    1: KEY_8,
    2: KEY_9,
    3: KEY_C,
  },

  3: {
    0: KEY_STAR,
    1: KEY_0,
    2: KEY_HASH,
    3: KEY_D,
  }
}

KEY_LABELS = {
  0: {
    0: '1',
    1: '2',
    2: '3',
    3: 'A',
  },

  1: {
    0: '4',
    1: '5',
    2: '6',
    3: 'B',
  },

  2: {
    0: '7',
    1: '8',
    2: '9',
    3: 'C',
  },

  3: {
    0: '*',
    1: '0',
    2: '#',
    3: 'D',
  }
}

# KEY_ROWS = [KEY_ROW_0, KEY_ROW_1, KEY_ROW_2, KEY_ROW_3]
# KEY_COLS = [KEY_COL_0, KEY_COL_1, KEY_COL_2, KEY_COL_3]
 
# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LEFT_JUST = 1
LCD_CENT_JUST = 2
LCD_RIGHT_JUST = 3
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
 
