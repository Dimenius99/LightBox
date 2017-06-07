import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 7
 
def move_90_degrees():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(7.5)
    p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    time.sleep(1) # sleep 1 second
    p.stop()
 
def rc_time (pin_to_circuit):
    count = 0
    
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    
    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
    
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    
    if count > 1000000:
        move_90_degrees()
return True
        
    else:
        return count
 
#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
