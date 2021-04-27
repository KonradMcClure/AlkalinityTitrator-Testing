# All Sensor Test
import time
from gpiozero import LED
import board
import busio
import pulseio
import digitalio
import serial
import pandas as pd
import adafruit_max31865
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from array import*
#---------------------------------------------------------------#
# GPIO Pin Wiring
# Stepper-3.3V:
#    GND-39, DIR-GPIO 26,-STEP: GPIO 13(PWM1)
# SssssssCR:
#    Pin3- GPIO12 (PWM0), Pin 4 - GND
# Temp Probe-(Normally 3 (trying 5)):
#    GPIO 10 (MOSI), GPIO 9 (MISO), GPIO 11(SCLK), GPIO 5
# Ph Probe-3.3V:
#    GPIO 2 (SDA), GPIO 3 (SCL), VCC (3.3V), GND -> GND, ALRT, ADDR 
#---------------------------------------------------------------#
# Temp Probe and SSR
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=1000, ref_resistor=4300, wires=3)
relay = LED(12)

# Ph Probe
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0, ADS.P1)
ads.gain = 2

# Step Stick and Arduino 
port="/dev/ttyUSB0"
baud=9600
TO=5
arduino = serial.Serial(port=port,baudrate=baud,timeout=TO)
arduino.reset_output_buffer()
arduino.reset_input_buffer()
time.sleep(2)

#---------------------------------------------------------------#
# dir values: 1 to pump, 0 to 'extract'
def driveStepStick(cycles, dir):
    time.sleep(.01)
    if(arduino.writable()):
        arduino.write(cycles.to_bytes(4, 'little'))
        arduino.write(dir.to_bytes(1, 'little'))
        arduino.flush()
        wait_time = cycles/1000 + .5
        time.sleep(wait_time)
        temp = arduino.readline()
        if(temp != b'DONE\r\n'):
            print("Error")
            print(temp)
    else:
        print("Arduino Not Available")
#---------------------------------------------------------------#

# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
#sensor = adafruit_max31865.MAX31865(spi, cs, rtd_nominal=100, ref_resistor=430.0, wires=2)

# Main loop to print the temperature every second.
error_prior=0
integral_prior=0
kp=.05
ki=0.00001
kd = 0.00001
temp = sensor.temperature
timelog = []
df = pd.DataFrame([[0]], columns = ['temp'])
timestep=1
setpoint=30
# turn relay on here
for i in range(0,1000):
    start = time.time()
    value=sensor.temperature
    timeAll = time.localtime(time.time())
    timelog.append(timeAll.tm_sec)      
    error= setpoint-value
    integral=integral_prior+error*timestep
    derivative=error-error_prior/timestep
    k=kp*error+ki*integral+kd*derivative

    if value < 30:
         if k<1:
             relay.on()
             time.sleep(timestep*k)
             relay.off()
             time.sleep(timestep*(1-k))
             error_prior=error
             integral_prior=integral
         elif k>1:
             k=1
             relay.on()
             time.sleep(timestep*k)
             relay.off()
             time.sleep(timestep*(1-k))
             error_prior=error
             integral_prior=integral
    elif value>=30:
        k=0
        relay.off()
        time.sleep(timestep)
        error_prior=error
        integral_prior=integral
       #relay.on()
       #time.sleep(timestep)
    #elif temp[i] > 30:
     #  relay.off()
      # time.sleep(timestep)
    df2 = pd.DataFrame([value], columns = ['temp'])
    df = df.append(df2)
    print("\nTemp:\t", value, "degC")
    print("Time:\t", timeAll.tm_sec, " s")
    print("K:\t", k)
    print("The Juice is going")
    mid = time.time()
    temp_time = (mid - start)
    print("Time Elapsed for Temp: ", temp_time)
    probe = chan.voltage/10
    print("Probe Voltage: ", probe)

    #time.sleep(.1)
    print("Stepping")
    driveStepStick(500,1)
    step_time = (time.time()-mid)
    print("Steps Done, Time elapsed: ", step_time)
    