#import
import RPi.GPIO as GPIO
import time

from constants import *

def main():
  # Main program block
  
  GPIO.setwarnings(False)
 
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  GPIO.setup(LCD_ON, GPIO.OUT) # Backlight enable

  GPIO.setup(KEY_ROW_0, GPIO.OUT) # Top Row
  GPIO.setup(KEY_ROW_1, GPIO.OUT)
  GPIO.setup(KEY_ROW_2, GPIO.OUT)
  GPIO.setup(KEY_ROW_3, GPIO.OUT) # Bottom Row
  GPIO.setup(KEY_COL_0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Leftmost Column
  GPIO.setup(KEY_COL_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(KEY_COL_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(KEY_COL_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Rightmost Column

 
  # Initialise display
  lcd_init()
 
  # Toggle backlight on-off-on
  lcd_backlight(True)
  time.sleep(0.5)
  lcd_backlight(False)
  time.sleep(0.5)
  lcd_backlight(True)
  time.sleep(0.5)

  test_lcd()
  #test_keypad()


# def display_list(list_to_display):
#     """
#     Display a list of options
#     :param list_to_display: list to be displayed on LCD screen
#     """
#     for key, value in list_to_display.items():
#         lcd_out(str(key) + '. ' + value)

def test_lcd():
  # Splash Screen
  lcd_out("Open", LCD_LINE_1,LCD_CENT_JUST)
  lcd_out("Acidification",LCD_LINE_2,LCD_CENT_JUST)
  lcd_out("Project", LCD_LINE_3,LCD_CENT_JUST)
  lcd_out("Alkaninity Titrator", LCD_LINE_4,LCD_CENT_JUST)

  time.sleep(3) # Second delay

  while True:
    lcd_out("1: Run titration", LCD_LINE_1, LCD_LEFT_JUST)
    lcd_out("2: Calibrate sensors", LCD_LINE_2, LCD_LEFT_JUST)
    lcd_out("3: Prime Pump", LCD_LINE_3, LCD_LEFT_JUST)
    lcd_out("*: Page 2", LCD_LINE_4, LCD_LEFT_JUST)

    user_input = None
    while(user_input != '*'):
      user_input = keypad_poll()

    lcd_out("4: Update settings", LCD_LINE_1, LCD_LEFT_JUST)
    lcd_out("5: Test Mode", LCD_LINE_2, LCD_LEFT_JUST)
    lcd_out("6: Exit", LCD_LINE_3, LCD_LEFT_JUST)
    lcd_out("*: Page 1", LCD_LINE_4, LCD_LEFT_JUST)

    user_input = None
    while(user_input != '*'):
      user_input = keypad_poll()

def test_keypad():
  while(True):
    keys = keypad_poll_all()
    line_1 = "1:" + keys[0] +" 2:" + keys[1] +" 3:" + keys[2] +" A:" + keys[3]
    line_2 = "4:" + keys[4] +" 5:" + keys[5] +" 6:" + keys[6] +" B:" + keys[7]
    line_3 = "7:" + keys[8] +" 8:" + keys[9] +" 9:" + keys[10] +" C:" + keys[11]
    line_4 = "*:" + keys[12] +" 0:" + keys[13] +" #:" + keys[14] +" D:" + keys[15]
    
    lcd_out(line_1, LCD_LINE_1, LCD_LEFT_JUST)
    lcd_out(line_2, LCD_LINE_2, LCD_LEFT_JUST)
    lcd_out(line_3, LCD_LINE_3, LCD_LEFT_JUST)
    lcd_out(line_4, LCD_LINE_4, LCD_LEFT_JUST)

    # try:
    #   while True:
    #     readRow(KEY_ROW_0, ['1','2','3','A'])
    #     readRow(KEY_ROW_1, ['4','5','6','B'])
    #     readRow(KEY_ROW_2, ['7','8','9','C'])
    #     readRow(KEY_ROW_3, ['*','0','#','D'])
    #     time.sleep(0.1)
    # except KeyboardInterrupt:
    #   print("\nApplication Stopped")

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_out(message,line,style):
  """
   Send string to display. 
   Lines: LCD_LINE_X (1,2,3,4) 
   styles (justification): X (1=left, 2=center, 3=right) 
  """
 
  if style==1:
    message = message.ljust(LCD_WIDTH," ")
  elif style==2:
    message = message.center(LCD_WIDTH," ")
  elif style==3:
    message = message.rjust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
def lcd_backlight(flag):
  # Toggle backlight on-off-on
  GPIO.output(LCD_ON, flag)
 
def keypad_poll():
  """
  polls the keypad and returns the button label (1,2,A,B,*,#, etc) 
  of the button pressed.
  """
  # Set each row high and check if a column went high as well
  for row in KEY_ROWS:
    GPIO.output(row,1)
    for col in KEY_COLS:
      if GPIO.input(col):
        GPIO.output(row,0)
        print("Button: ", row, " ", col)
        return KEY_LABELS[row][col]
    GPIO.output(row,0)

  # No buttons were pressed
  return None

def keypad_poll_all():
  """
  polls the keypad and returns the button label (1,2,A,B,*,#, etc) 
  of the button pressed.
  """
  results = []
  # Set each row high and check if a column went high as well
  for row in KEY_ROWS:
    GPIO.output(row,1)
    for col in KEY_COLS:
      if GPIO.input(col):
        results.append('1')
      else:
        results.append('0')
    GPIO.output(row,0)

  # No buttons were pressed
  return results

def readRow(line, characters):
  """
  Reads a row and prints any pressed characters to the screen
  """
  GPIO.output(line, GPIO.HIGH)

  if (GPIO.input(KEY_COL_0)==1):
    lcd_out(str(characters[0]),LCD_LINE_1,1)
    print(characters[0])
  if (GPIO.input(KEY_COL_1)==1):
    lcd_out(str(characters[1]),LCD_LINE_1,1)
    print(characters[0])
  if (GPIO.input(KEY_COL_2)==1):
    lcd_out(str(characters[2]),LCD_LINE_1,1)
    print(characters[0])
  if (GPIO.input(KEY_COL_3)==1):
    lcd_out(str(characters[3]),LCD_LINE_1,1)
    print(characters[0])
    
  GPIO.output(line,GPIO.LOW)


if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass

# WAIT STOP DON'T PUT A FUNCTION DOWN HERE
