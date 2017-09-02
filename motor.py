# GumballMachine
# import necessary libraries
import RPi.GPIO as GPIO, time
from time import sleep

# set the pin numbering mode
GPIO.setmode(GPIO.BOARD)
# set variables for easy reference
Motor1A = 16
Motor1B = 18
Motor1E = 22
Button = 37
IRDetector = 31

# initialize GPIO pins
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IRDetector, GPIO.IN)

# define a function for running the motor
def runMotor(seconds):
    #print("Turning motor on")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    sleep(seconds)

    #print("Stopping motor")
    GPIO.output(Motor1E, GPIO.LOW)

coin_dropped = GPIO.input(IRDetector)
number_coins = 0
while True:
    signal_received = GPIO.input(IRDetector)
    if signal_received != coin_dropped:
        if signal_received == True:
            number_coins = number_coins + 1
            print("{} coin(s) dropped! Redeemable for {} gumball(s)!".format(number_coins, number_coins))
        coin_dropped = signal_received
        time.sleep(0.1)

    button_pressed = not GPIO.input(Button)
    if button_pressed == True:
        print("Button Pressed.")
        print("DISPENSING {} GUMBALL(S)!".format(number_coins))
        print("")
        motorTime = number_coins * 3.5
        runMotor(motorTime)
        number_coins = 0
    

GPIO.cleanup()
