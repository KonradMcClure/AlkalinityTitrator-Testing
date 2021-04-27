import time
from gpiozero import LED
import board
import busio
import digitalio
import pandas as pd
import adafruit_max31865
from array import*
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D7)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=1000, ref_resistor=4300, wires=3)
relay = LED(12)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
#sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=2)
# Main loop to print the temperature every second.

#Set initial values for errors for PID
error_prior=0
integral_prior=0
#Set PID Gains

k=0
temp = sensor.temperature
timelog = []
df = pd.DataFrame([[temp, k]], columns = ['temp','gain'])
timestep=1 #Set time for each temp control loop
setpoint=30 #Target temp

for i in range(0,1000): #Run for 1000 seconds
    #Get data values
    value=sensor.temperature
    timeAll = time.localtime(time.time())
    timelog.append(timeAll.tm_sec)
    #anti-windup, change PID parameters after 250s
    if i < 250:
        kp=.09
        Ti=0.000001
        Td =9
        integral=0
    elif i>250:
        kp=.04
        Ti=0.004
        Td =9
    #Update PID Gain
    error= setpoint-value
    integral=integral_prior+error*timestep
    derivative=(error-error_prior)/timestep
    k=kp*(error+Ti*integral+Td*derivative)

    if value < setpoint: #If temp is below setpoint
         if k<0: #If gain is less than zero, do nothing
             k=0
             time.sleep(timestep)
         elif k<1:
             #if gain is less than one turn relay on for an amount of time
             relay.on() 
             time.sleep(timestep*k)
             #then off for an amount of time
             relay.off()
             time.sleep(timestep*(1-k))
             #Update PID values
             error_prior=error
             integral_prior=integral
         elif k>1:
             #if K>1, set equal to 1, essentially turning on relay for full timestep
             k=1
             relay.on()
             time.sleep(timestep*k)
             relay.off()
             time.sleep(timestep*(1-k))
              #Update PID values
             error_prior=error
             integral_prior=integral
         
    elif value>=setpoint:
        #if temp is over setpoint, turn off relay
        k=0
        relay.off()
        time.sleep(timestep)
        error_prior=error
        integral_prior=integral
#output data to file
    df2 = pd.DataFrame([[value, k]], columns = ['temp','gain'])
    df = df.append(df2)
   
    print(df)
export_csv = df.to_csv ('PID9.txt', index = None, header=True) #Don't forget to add '.csv' at the end of the 
