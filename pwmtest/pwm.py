import board
import time
import pwmio
import math

stirrer = pwmio.PWMOut(board.D13, duty_cycle=0,frequency=50)

while True:
	input("Press enter to start up")
	print("Starting Up Slow Mode")
	stirrer.duty_cycle = 30000
	print("Stirrer set to ", stirrer.duty_cycle)
	time.sleep(2.0)
	stirrer.duty_cycle = 10000
	print("Stirrer set to ", stirrer.duty_cycle)
	
	selection = -1
	while (selection != 3):
		selection = int(input("Select mode:\n\tSlow: 1\n\tFast: 2\n\tStop: 3\n>"))
		if (selection == 1):
			stirrer.duty_cycle = 10000
		elif selection == 2:
			stirrer.duty_cycle = 15000
		elif selection == 3:
			stirrer.duty_cycle = 0
		else:
			print("Invalid input")
		
		print("Stirrer set to ", stirrer.duty_cycle)
		time.sleep(1.0)
		
	time.sleep(1.0)


