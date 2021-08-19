import board
import time
import pwmio
import math

def change_pwm(stirrer, target):
	direction = math.copysign(1, target - stirrer.duty_cycle)
	next_step = min(abs(target - stirrer.duty_cycle), 1000)
	while stirrer.duty_cycle != target:
		stirrer.duty_cycle = stirrer.duty_cycle + (next_step * direction)
		print("Stirrer set to ", stirrer.duty_cycle)
		time.sleep(0.2)

stirrer = pwmio.PWMOut(board.D13, duty_cycle=0,frequency=100)

while True:
	input("Press enter to start up")
	print("Starting Up Slow Mode")
	stirrer.duty_cycle = 9000
	print("Stirrer set to ", stirrer.duty_cycle)
	
	selection = -1
	while (selection != 3):
		selection = int(input("Select mode:\n\tSlow: 1\n\tFast: 2\n\tStop: 3\n\tCustom: 4\n>"))
		if (selection == 1):
			change_pwm(stirrer, 9000)
		elif selection == 2:
			change_pwm(stirrer, 12000)
		elif selection == 3:
			stirrer.duty_cycle = 0
		elif selection == 4:
			target = int(input("\tEnter duty cycle: "))
			change_pwm(stirrer, target)
		else:
			print("Invalid input")
		
		print("Stirrer set to ", stirrer.duty_cycle)
		time.sleep(1.0)
		
	time.sleep(1.0)


