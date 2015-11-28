#!/usr/bin/python

import pygame
from pygame.locals import *
import random
import time
import threading
import csv
import serial

displayed_numbers = []

def print_numbers(disp_numbers):
        
        rank = []

        print "Now your turn to enter the numbers"
        print "=================================="
        input_numbers = raw_input("Enter the numbers:")
        list_numbers = input_numbers.split(" ")
        while(len(list_numbers) < 10):
            list_numbers.append('11')
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
                
                time.sleep(2)
                background.fill((250,250,250))
                i+=1
        pygame.quit()

random_numbers()
print_numbers(displayed_numbers)


