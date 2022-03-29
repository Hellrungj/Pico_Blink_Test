from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    print("Hello, from Rasberry Pi Pico")
    time.sleep(0.5)