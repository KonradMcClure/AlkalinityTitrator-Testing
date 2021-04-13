

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
LED_ON = 15

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

KEY_ROW_0 = 6
KEY_ROW_1 = 13
KEY_ROW_2 = 19
KEY_ROW_3 = 26

KEY_COL_0 = 12
KEY_COL_1 = 16
KEY_COL_2 = 20
KEY_COL_3 = 21

KEY_LABELS = {
  KEY_ROW_0: {
    KEY_COL_0: '1',
    KEY_COL_1: '2',
    KEY_COL_2: '3',
    KEY_COL_3: 'A',
  },

  KEY_ROW_1: {
    KEY_COL_0: '4',
    KEY_COL_1: '5',
    KEY_COL_2: '6',
    KEY_COL_3: 'B',
  },

  KEY_ROW_2: {
    KEY_COL_0: '7',
    KEY_COL_1: '8',
    KEY_COL_2: '9',
    KEY_COL_3: 'C',
  },

  KEY_ROW_3: {
    KEY_COL_0: '*',
    KEY_COL_1: '0',
    KEY_COL_2: '#',
    KEY_COL_3: 'D',
  }
}



KEY_ROWS = [KEY_ROW_0, KEY_ROW_1, KEY_ROW_2, KEY_ROW_3]
KEY_COLS = [KEY_COL_0, KEY_COL_1, KEY_COL_2, KEY_COL_3]
 
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
 
