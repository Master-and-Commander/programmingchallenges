import RPi.GPIO as GPIO
import time


# to control raspberry pi tank movements
# link https://opensourceforu.com/2017/07/introduction-raspberry-pi-gpio-programming-using-python/

def main():
    GPIO.setmode(GPIO.BOARD)
    mypin = 8
    GPIO.setup(mypin, GPIO.OUT, initial = 0)
    movementAi()

def movementController(direction, duration):
    #move the correct pin


def movementAi():
    try:
        while 1:
            movementController(up, 5):
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()




main()
