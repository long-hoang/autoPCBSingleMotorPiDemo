# Test v7 --> TESTED AND WORKS!
# Long Hoang, NeuroLeap Corp
#
# Developing code to run stepper driver + stepper motor system
from time import sleep # note: sleep input units = seconds
import RPi.GPIO as GPIO

# I/O Pin 
PUL = 17
DIR = 22
ENA = 23


pul_delay = 0.00005 # seconds/pulse, sets speed
 

def init():
    # Set GPIO mode
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PUL, GPIO.OUT)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    print('Initialization Completed')
    return

def go():

    
    GPIO.output(PUL,GPIO.HIGH)
    sleep(pul_delay)
    GPIO.output(PUL,GPIO.LOW)
    sleep(pul_delay)


    return





def main(): 

    while True:     # continuously asking for user input
        user_input = raw_input("Enter command:") # 0 or 1

        
        if user_input == 'dirlow':
            GPIO.output(DIR, GPIO.LOW)
            print("Direction set to LOW")
            
        elif user_input == 'dirhigh':
            GPIO.output(DIR, GPIO.HIGH)
            print("Direction set to HIGH")
            
        elif user_input == 'enable':
            GPIO.output(ENA, GPIO.HIGH)
            print("ENABLED Motor")
            
        elif user_input == 'disable':
            GPIO.output(ENA, GPIO.LOW)
            print("DISABLED Motor")
            
        elif user_input == 'run':
            
            step_cycle_input = input("Cycles?")
            print("Motor GO!") 
            for x in range(step_cycle_input):    
                
                go()
            print("Motor Stopped...")
            
        elif user_input == 'off':
            GPIO.cleanup()
            break


    return


init()
main()
print("DONE!")






