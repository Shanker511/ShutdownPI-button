# playSounds.py

import pygame.mixer
from time import sleep
from sys import exit

pygame.mixer.init(22050, -16, 1, 1024) 

soundA = pygame.mixer.Sound("shutdown.wav") 

soundChannelA = pygame.mixer.Channel(1) 



import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
 
prev_input = 0
while True:
  input = GPIO.input(4)
  if ((not prev_input) and input):
    print "System Shutdown"
    soundChannelA.play(soundA) 
    os.system("sudo shutdown -h now")
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)