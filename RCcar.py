#This is the main Python program used to run the RC car. Boots on startup

from Phidget22.Phidget import * 
from Phidget22.Devices.DCMotor import * #Libraries used to interact with the Phidget motor controller onboard
from RPLCD.i2c import CharLCD #Used for LCD functionality
from gpiozero import CPUTemperature #Reads CPU temp in celcius
import time #time based functions to use in code
import pygame #used to run code based on keyboard inputs while the pygame window is running

## Helper functions ##

# Initializes the LCD display for future use
def initializeLCD():
	lcd = CharLCD('PCF8574', 0x27)
	
	return lcd

# Reads CPU temp 
def getTemp():
	# Create a CPUTemperature object
	cpuTemp = CPUTemperature()

	# Get the temperature as a float
	tempFloat = float(cpuTemp.temperature)
	
	celciusTemp = (tempFloat-32) * (5/9)
	celciusTemp = round(celciusTemp, 2)
	
	#overheating handling, but this should literally never happen unless you run a million things on the Pi
	if celciusTemp > 60:
		lcd.clear()
		lcd_write("Overheated!")
		cursor_pos(1,0)
		lcd_write("Shutting down...")
		pygame.quit
	
	cpuTemp = celciusTemp
	return cpuTemp
	
# Displays a welcome message to the user on startup via the LCD display

def welcomemsg(lcd):
	
	lcd = initializeLCD()

	lcd.write_string("Please wait")
	for i in range (1):
		for j in range (3):
			lcd.write_string(".")
			time.sleep(0.5)
	time.sleep(3)
	lcd.clear()
	
	lcd.write_string("Connect your")
	lcd.cursor_pos = (1,0)
	lcd.write_string("controller now!")	
	time.sleep(3)
	
# Displays the current temprature of the raspberry pi
	
def displaytemp(lcd):
	
	cpuTemp = getTemp()

	cpuTempString = str(cpuTemp)
	
	lcd.cursor_pos = (1,0)
	lcd.write_string("CPU Temp:")
	
	lcd.cursor_pos = (1,10)
	lcd.write_string(cpuTempString)
	
	lcd.cursor_pos = (1,15)
	lcd.write_string("C")
	
## Main RC Car code ##

def main():
	
	pygame.init()
	screen = pygame.display.set_mode((250,250)) #screen used to take keyboard inputs
	pygame.display.set_caption("RC Car")
	
	# pygame.joystick.init()
	# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())
	
	#inializes the LCD
	lcd = initializeLCD()
	
	#Creates motor channels
	dcMotor0 = DCMotor()
	dcMotor1 = DCMotor()

	#Sets default value for velocity
	velocity = 1

	#Sets addressing parameters to specify which channel to open (if any)
	dcMotor0.setChannel(0)
	dcMotor1.setChannel(1)

	#Open your motors and wait for attachment
	dcMotor0.openWaitForAttachment(5000)
	dcMotor1.openWaitForAttachment(5000)

	# print(dcMotor0.getMinDataInterval())
	# print(dcMotor1.getMinDataInterval())
	
	#Other stuff

	# dcMotor0.setDataInterval(32)
	# dcMotor1.setDataInterval(32)
	# dcMotor0.setDataRate(31)
	# dcMotor1.setDataRate(31)
	dcMotor0.setAcceleration(10)
	dcMotor1.setAcceleration(10)
	
	# Starts welcome message to display before any user input
	welcomemsg(lcd)

	#Controls for the RC Car. Change depending on what key is detected on input
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:		
				#Forwards / Reverse
				if event.key == pygame.K_1: #Left trigger
					lcd.clear()
					lcd.cursor_pos = (0,0)					
					lcd.write_string("Accelerating!")				
					displaytemp(lcd)
					dcMotor0.setTargetVelocity(velocity)
					
				if event.key == pygame.K_2: #Right trigger
					lcd.clear()
					lcd.cursor_pos = (0,0)				
					lcd.write_string("Accelerating!")		
					displaytemp(lcd)
					dcMotor1.setTargetVelocity(velocity)
					
				if event.key == pygame.K_3: #Left bumper
					lcd.clear()
					lcd.cursor_pos = (0,0)				
					lcd.write_string("Reversing!")		
					displaytemp(lcd)
					dcMotor0.setTargetVelocity(-1*velocity)

				if event.key == pygame.K_4: #Right bumper
					lcd.clear()
					lcd.cursor_pos = (0,0)				
					lcd.write_string("Reversing!")	
					displaytemp(lcd)
					dcMotor1.setTargetVelocity(-1*velocity)
					
				#Left / Right
				if event.key == pygame.K_5: #Turn left
					lcd.clear()
					lcd.cursor_pos = (0,0)				
					lcd.write_string("Turning left!")
					displaytemp(lcd)											
					dcMotor1.setTargetVelocity(-1*velocity)
					dcMotor0.setTargetVelocity(velocity)

				if event.key == pygame.K_6: #Turn right
					lcd.clear()
					lcd.cursor_pos = (0,0)				
					lcd.write_string("Turning right!")
					displaytemp(lcd)
					dcMotor0.setTargetVelocity(-1*velocity)
					dcMotor1.setTargetVelocity(velocity)

				#Select Button (only use for debugging)
				if event.key == pygame.K_0: #Kills Program
					lcd.clear()
					lcd.cursor_pos = (0,0)				
					lcd.write_string("Shutting down...")
					time.sleep(1)
					lcd.clear()										
					pygame.quit()
					
			#Idle state (no keys are being inputed)
			if event.type == pygame.KEYUP:
				dcMotor0.setTargetVelocity(0)
				dcMotor1.setTargetVelocity(0)
				displaytemp(lcd)															
				
			if event.type == pygame.QUIT:
				#Close Motors
				lcd.clear()
				lcd.cursor_pos = (0,0)								
				lcd.write_string("Shutting down...")
				time.sleep				
				dcMotor0.close()
				dcMotor1.close()
				lcd.clear()
				quit()
main()
