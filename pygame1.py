#!/usr/bin/python

import pygame
from pygame.locals import *
import random
import time
import threading
import csv
import serial
import sys

displayed_numbers = []

locations = ["/dev/ttyACM0","/dev/ttyACM1","/dev/ttyACM2"]
pygame_flag = True

for port in locations:

    try:
        print "Trying port",port,"..."
        serial_port = serial.Serial(port,115200)

    except:
        print "Failed to connect to port",port
        
print "connected to port",port

def isint(string):
    try:
        int(string)
        return True
    except:
        return False

def eeg_data(serial_port):
    
    file_n = "data_visual_"+time.strftime("%Y_%m_%d_%H_%M")
    file_path = "/home/aswin/eeg_data/"+file_n
    file_name = open(file_path,"w")

    while(pygame_flag):
   
        eeg_string = serial_port.readline().strip("\0\n").split(",")
    
        if(isint(eeg_string[0]) and isint(eeg_string[1])):
            file_name.write(eeg_string[0]+"\n")
            
def print_numbers(disp_numbers):
        
        global pygame_flag

        rank = []

        print "Now your turn to enter the numbers"
        print "=================================="
        input_numbers = raw_input("Enter the numbers:")
        list_numbers = input_numbers.split(" ")
        while(len(list_numbers) < 10):
            list_numbers.append("N")
        print "Numbers displayed:",disp_numbers
        print "Numbers you typed:",list_numbers
        for i in range(0,len(disp_numbers)):
            if(disp_numbers[i] == list_numbers[i]):
                rank.append(1)
            else:
                rank.append(0)
        success = (float(sum(rank))/float(len(disp_numbers))*100)


        print rank
        print "Your percentage of success is = ",success,"%"
        pygame_flag = False

def random_numbers():

	numbers = ["1", "2", "3", "4", "5","6","7","8","9","0"]
        global displayed_numbers
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((600, 300))
	pygame.display.set_caption('memory game')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))
        
	# Display some text
	# Event loop
	for i in range(0,10):
		for event in pygame.event.get():
			if event.type == QUIT:
				return
	        font = pygame.font.Font(None, 150)
                random_number = random.choice(numbers)
                displayed_numbers.append(random_number)
	        text = font.render(random_number, 1, (10, 10, 10))
	        textpos = text.get_rect()
	        textpos.centerx = background.get_rect().centerx
	        background.blit(text, textpos)

	# Blit everything to the screen
	        screen.blit(background, (0, 0))
	        pygame.display.flip()
                
                time.sleep(1)
                background.fill((250,250,250))
                i+=1
        pygame.quit()
        print_numbers(displayed_numbers)

thread1 = threading.Thread(target=random_numbers,args=())
thread2 = threading.Thread(target=eeg_data,args=(serial_port,))

thread1.start()
thread2.start()

