#import
import digitalio
import time
from board import *
from constants import *

class LCD():
  """Sunfire LCD 2x16 Char Display Module"""
  def __init__(self):
    # Set up pins
    self.pin_RS  = digitalio.DigitalInOut(D27) # RS
    self.pin_E   = digitalio.DigitalInOut(D22) # E
    self.pin_D4  = digitalio.DigitalInOut(D18) # DB4
    self.pin_D5  = digitalio.DigitalInOut(D23) # DB5
    self.pin_D6  = digitalio.DigitalInOut(D24) # DB6
    self.pin_D7  = digitalio.DigitalInOut(D25) # DB7
    self.pin_ON = digitalio.DigitalInOut(D15) # Backlight enable

    self.pin_E.direction = digitalio.Direction.OUTPUT
    self.pin_RS.direction = digitalio.Direction.OUTPUT
    self.pin_D4.direction = digitalio.Direction.OUTPUT
    self.pin_D5.direction = digitalio.Direction.OUTPUT
    self.pin_D6.direction = digitalio.Direction.OUTPUT
    self.pin_D7.direction = digitalio.Direction.OUTPUT
    self.pin_ON.direction = digitalio.Direction.OUTPUT
    
     # Initialise display
    self.lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    self.lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    self.lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
    self.lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
    self.lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    self.lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)
    
    # Toggle backlight on-off-on
    self.lcd_backlight(True)
    time.sleep(0.5)
    self.lcd_backlight(False)
    time.sleep(0.5)
    self.lcd_backlight(True)
    time.sleep(0.5)


  def lcd_byte(self,bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command
   
    self.pin_RS.value = mode # RS
   
    # High bits
    self.pin_D4.value = False
    self.pin_D5.value = False
    self.pin_D6.value = False
    self.pin_D7.value = False
    if bits&0x10==0x10:
      self.pin_D4.value = True
    if bits&0x20==0x20:
      self.pin_D5.value = True
    if bits&0x40==0x40:
      self.pin_D6.value = True
    if bits&0x80==0x80:
      self.pin_D7.value = True
   
    # Toggle 'Enable' pin
    self.lcd_toggle_enable()
   
    # Low bits
    self.pin_D4.value = False
    self.pin_D5.value = False
    self.pin_D6.value = False
    self.pin_D7.value = False
    if bits&0x01==0x01:
      self.pin_D4.value = True
    if bits&0x02==0x02:
      self.pin_D5.value = True
    if bits&0x04==0x04:
      self.pin_D6.value = True
    if bits&0x08==0x08:
      self.pin_D7.value = True
   
    # Toggle 'Enable' pin
    self.lcd_toggle_enable()
 
  def lcd_toggle_enable(self):
    # Toggle enable
    time.sleep(E_DELAY)
    self.pin_E.value = True
    time.sleep(E_PULSE)
    self.pin_E.value = False
    time.sleep(E_DELAY)
 
  def out(self,message,line,style):
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
   
    self.lcd_byte(line, LCD_CMD)
   
    for i in range(LCD_WIDTH):
      self.lcd_byte(ord(message[i]),LCD_CHR)
 
  def lcd_backlight(self,flag):
    # Toggle backlight on-off-on
    self.pin_ON.value = flag

class Keypad():
  def __init__(self):
    
    self.pin_R0 = digitalio.DigitalInOut(D1) # Top Row
    self.pin_R1 = digitalio.DigitalInOut(D6)
    self.pin_R2 = digitalio.DigitalInOut(D5)
    self.pin_R3 = digitalio.DigitalInOut(D19) # Bottom Row
    self.pin_C0 = digitalio.DigitalInOut(D16) # Leftmost Column
    self.pin_C1 = digitalio.DigitalInOut(D26)
    self.pin_C2 = digitalio.DigitalInOut(D20)
    self.pin_C3 = digitalio.DigitalInOut(D21) # Rightmost Column
    
    self.rows = [
      self.pin_R0,
      self.pin_R1,
      self.pin_R2,
      self.pin_R3]
    self.cols = [
      self.pin_C0,
      self.pin_C1,
      self.pin_C2,
      self.pin_C3]    
    
    self.rows[0].direction = digitalio.Direction.OUTPUT
    self.rows[1].direction = digitalio.Direction.OUTPUT
    self.rows[2].direction = digitalio.Direction.OUTPUT
    self.rows[3].direction = digitalio.Direction.OUTPUT
    self.cols[0].direction = digitalio.Direction.INPUT
    self.cols[1].direction = digitalio.Direction.INPUT
    self.cols[2].direction = digitalio.Direction.INPUT
    self.cols[3].direction = digitalio.Direction.INPUT
    
    self.cols[0].pull = digitalio.Pull.DOWN
    self.cols[1].pull = digitalio.Pull.DOWN
    self.cols[2].pull = digitalio.Pull.DOWN
    self.cols[3].pull = digitalio.Pull.DOWN
    
  def keypad_poll(self):
    """
    polls the keypad and returns the button label (1,2,A,B,*,#, etc) 
    of the button pressed.
    """
    # Set each row high and check if a column went high as well
    for row in range(len(self.rows)):
      self.rows[row].value = True
      for col in range(len(self.cols)):
        if self.cols[col].value:
          self.rows[row].value = False
          print("Button: ", row, " ", col)
          return KEY_LABELS[row][col]
      self.rows[row].value = False

    # No buttons were pressed
    return None

  def keypad_poll_all(self):
    """
    polls the keypad and returns the button label (1,2,A,B,*,#, etc) 
    of the button pressed.
    """
    results = []
    # Set each row high and check if a column went high as well
    for row in range(len(self.rows)):
      self.rows[row].value = True
      for col in range(len(self.cols)):
        if self.cols[col].value:
          results.append('1')
        else:
          results.append('0')
      self.rows[row].value = False

    # No buttons were pressed
    return results

  def readRow(self,lcd, line, characters):
    """
    Reads a row and prints any pressed characters to the screen
    """
    self.rows[line].value = True

    if (KEY_COL_0.value==1):
      lcd.out(str(characters[0]),LCD_LINE_1,1)
      print(characters[0])
    if (KEY_COL_1.value==1):
      lcd.out(str(characters[1]),LCD_LINE_1,1)
      print(characters[0])
    if (KEY_COL_2.value==1):
      lcd.out(str(characters[2]),LCD_LINE_1,1)
      print(characters[0])
    if (KEY_COL_3.value==1):
      lcd.out(str(characters[3]),LCD_LINE_1,1)
      print(characters[0])
      
    self.rows[line].value = False
    
      
def main():
  # Main program block
  lcd = LCD()
  key = Keypad()

  # test_lcd(lcd, key)
  test_keypad(lcd, key)


# def display_list(list_to_display):
#     """
#     Display a list of options
#     :param list_to_display: list to be displayed on LCD screen
#     """
#     for key, value in list_to_display.items():
#         lcd_out(str(key) + '. ' + value)

def test_lcd(lcd, key):
  # Splash Screen
  lcd.out("Open", LCD_LINE_1,LCD_CENT_JUST)
  lcd.out("Acidification",LCD_LINE_2,LCD_CENT_JUST)
  lcd.out("Project", LCD_LINE_3,LCD_CENT_JUST)
  lcd.out("Alkaninity Titrator", LCD_LINE_4,LCD_CENT_JUST)

  time.sleep(3) # Second delay

  while True:
    lcd.out("1: Run titration", LCD_LINE_1, LCD_LEFT_JUST)
    lcd.out("2: Calibrate sensors", LCD_LINE_2, LCD_LEFT_JUST)
    lcd.out("3: Prime Pump", LCD_LINE_3, LCD_LEFT_JUST)
    lcd.out("*: Page 2", LCD_LINE_4, LCD_LEFT_JUST)

    user_input = None
    while(user_input != '*'):
      user_input = key.keypad_poll()

    lcd.out("4: Update settings", LCD_LINE_1, LCD_LEFT_JUST)
    lcd.out("5: Test Mode", LCD_LINE_2, LCD_LEFT_JUST)
    lcd.out("6: Exit", LCD_LINE_3, LCD_LEFT_JUST)
    lcd.out("*: Page 1", LCD_LINE_4, LCD_LEFT_JUST)

    user_input = None
    while(user_input != '*'):
      user_input = key.keypad_poll()

def test_keypad(lcd, key):
  while(True):
    keys = key.keypad_poll_all()
    line_1 = "1:" + keys[0] +" 2:" + keys[1] +" 3:" + keys[2] +" A:" + keys[3]
    line_2 = "4:" + keys[4] +" 5:" + keys[5] +" 6:" + keys[6] +" B:" + keys[7]
    line_3 = "7:" + keys[8] +" 8:" + keys[9] +" 9:" + keys[10] +" C:" + keys[11]
    line_4 = "*:" + keys[12] +" 0:" + keys[13] +" #:" + keys[14] +" D:" + keys[15]
    
    lcd.out(line_1, LCD_LINE_1, LCD_LEFT_JUST)
    lcd.out(line_2, LCD_LINE_2, LCD_LEFT_JUST)
    lcd.out(line_3, LCD_LINE_3, LCD_LEFT_JUST)
    lcd.out(line_4, LCD_LINE_4, LCD_LEFT_JUST)

    # try:
    #   while True:
    #     readRow(KEY_ROW_0, ['1','2','3','A'])
    #     readRow(KEY_ROW_1, ['4','5','6','B'])
    #     readRow(KEY_ROW_2, ['7','8','9','C'])
    #     readRow(KEY_ROW_3, ['*','0','#','D'])
    #     time.sleep(0.1)
    # except KeyboardInterrupt:
    #   print("\nApplication Stopped")


if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass

# WAIT STOP DON'T PUT A FUNCTION DOWN HERE
