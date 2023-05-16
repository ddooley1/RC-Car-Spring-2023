import time
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)
loopflag = True

for i in range(4):
	lcd.write_string('Hello, world!')
	time.sleep(4)
	lcd.clear()
	lcd.write_string('Test msg!')
	time.sleep(4)
	lcd.clear()

lcd.clear()
