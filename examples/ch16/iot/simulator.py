# simulator.py
"""A connected thermostat simulator that publishes JSON
messages to dweet.io"""
import dweepy
import sys
import time
import random

MIN_CELSIUS_TEMP = -25  
MAX_CELSIUS_TEMP = 45 
MAX_TEMP_CHANGE = 2

# get the number of messages to simulate and delay between them
NUMBER_OF_MESSAGES = int(sys.argv[1]) 
MESSAGE_DELAY = int(sys.argv[2])

dweeter = 'temperature-simulator-deitel-python'  # provide a unique name
thermostat = {'Location': 'Boston, MA, USA',
              'Temperature': 20, 
              'LowTempWarning': False,
              'HighTempWarning': False}

print('Temperature simulator starting')

for message in range(NUMBER_OF_MESSAGES):
    # generate a random number in the range -MAX_TEMP_CHANGE 
    # through MAX_TEMP_CHANGE and add it to the current temperature
    thermostat['Temperature'] += random.randrange(
        -MAX_TEMP_CHANGE, MAX_TEMP_CHANGE + 1)
    
    # ensure that the temperature stays within range
    if thermostat['Temperature'] < MIN_CELSIUS_TEMP:
        thermostat['Temperature'] = MIN_CELSIUS_TEMP
    
    if thermostat['Temperature'] > MAX_CELSIUS_TEMP:
        thermostat['Temperature'] = MAX_CELSIUS_TEMP
    
    # check for low temperature warning
    if thermostat['Temperature'] < 3:
        thermostat['LowTempWarning'] = True
    else:
        thermostat['LowTempWarning'] = False

    # check for high temperature warning
    if thermostat['Temperature'] > 35:
        thermostat['HighTempWarning'] = True
    else:
        thermostat['HighTempWarning'] = False

    # send the dweet to dweet.io via dweepy
    print(f'Messages sent: {message + 1}\r', end='')
    dweepy.dweet_for(dweeter, thermostat)
    time.sleep(MESSAGE_DELAY)

print('Temperature simulator finished')
