import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
from time import sleep

#define pulse output function

def pulseOutput(pulseNumber):
    
    """ This is a for-loop that creates pulses at the output

        Preconditions: pulseNumber is a type int that tells us how many pulses
        we need, or how many times we need to repeat the for-loop
        
    """
    for i in range(0, pulseNumber):
        GPIO.output(26,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(26,GPIO.LOW)
        sleep(0.5)
        return
        
# setup port
GPIO.setup(26,GPIO.OUT)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

# create an analog input channel on pin 4
chan4 = AnalogIn(mcp, MCP.P4)

#number of pulses
pulseNum = int(float(chan0.voltage)*10)

print('ADC Voltage: ' + str(chan0.voltage) + 'V')

pulseOutput(pulseNum)
    
#number of additional pulses 
desV = 3
currV = chan4.voltage
print('Current Voltage (laser): ' + str(chan4.voltage) + 'V')
diffV = desV - currV
pulseV = 0.1
pulseNum2 = diffV/pulseV

pulseOutput(pluseNum2)