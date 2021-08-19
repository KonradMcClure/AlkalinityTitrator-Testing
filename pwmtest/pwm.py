import board
import time
import pwmio
import math

stirrer = pwmio.PWMOut(board.D13, duty_cycle=0,frequency=100)

while True:
	input("Press enter to start up")
	print("Starting Up Slow Mode")
	stirrer.duty_cycle = 7500
	print("Stirrer set to ", stirrer.duty_cycle)
	time.sleep(0.5)
	stirrer.duty_cycle = 9000
	print("Stirrer set to ", stirrer.duty_cycle)
	
	selection = -1
	while (selection != 3):
		selection = int(input("Select mode:\n\tSlow: 1\n\tFast: 2\n\tStop: 3\n\tCustom: 4\n>"))
		if (selection == 1):
			stirrer.duty_cycle = 9000
		elif selection == 2:
			stirrer.duty_cycle = 12000
		elif selection == 3:
			stirrer.duty_cycle = 0
		elif selection == 4:
			stirrer.duty_cycle = int(input("\tEnter duty cycle: "))
		else:
			print("Invalid input")
		
		print("Stirrer set to ", stirrer.duty_cycle)
		time.sleep(1.0)
		
	time.sleep(1.0)


