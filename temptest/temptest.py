# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
 
# Simple demo of the MAX31865 thermocouple amplifier.
# Will print the temperature every second.
import time
 
import board
import busio
import digitalio
 
import adafruit_max31865
 
 
# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs0 = digitalio.DigitalInOut(board.D4)  # Chip select of the MAX31865 board.
cs1 = digitalio.DigitalInOut(board.CE1)  # Chip select of the MAX31865 board.

#sensor = adafruit_max31865.MAX31865(spi, cs)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
sensor0 = adafruit_max31865.MAX31865(spi, cs0, rtd_nominal=1000, ref_resistor=4300.0, wires=3)
sensor1 = adafruit_max31865.MAX31865(spi, cs1, rtd_nominal=1000, ref_resistor=4300.0, wires=3)
 
# Main loop to print the temperature every second.
while True:
    # Read temperature.
    temp0 = sensor0.temperature
    res0 = sensor0.resistance
    # Print the value.
    print("Temperature 0: {0:0.3f}C".format(temp0))
    print("Resistance 0: {0:0.3f}".format(res0))
    
    # Read temperature.
    temp1 = sensor1.temperature
    res1 = sensor1.resistance
    # Print the value.
    print("Temperature 1: {0:0.3f}C".format(temp1))
    print("Resistance 1: {0:0.3f}".format(res1))
    # Delay for a second.
    time.sleep(1.0)
