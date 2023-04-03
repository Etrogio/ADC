import RPi.GPIO as GPIO
import time

def decimal2binary(value):
	return [int(element) for element in bin(value)[2:].zfill(8)]
	
def adc():
	for value in range(256):
		GPIO.output(dac, decimal2binary(value))
		c = GPIO.input(comp)
		time.sleep(0.05)
		if c == 0:
			return value

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
	while True:
		i = adc()
		if i != 0:
			print(i, '{:.2f}v'.format{3.3*i/256})
finally:
	GPIO.output(dac, 0)
	GPIO.cleanup()