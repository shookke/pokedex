import pygame
import os
from time import sleep
import RPi.GPIO as GPIO


screen_width = 320
screen_height = 240
center = (160,120)

pygame.init()

screen = pygame.display.set_mode([screen_width,screen_height])


screen.fill((255,255,255))
pygame.display.update()

logo = pygame.image.load('resources/pokemon_logo.png')
rect = logo.get_rect(center=center)
screen.blit(logo,rect)

	

while True:
	pygame.display.update()
	sleep(0.1)
