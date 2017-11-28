
from window import Window
from entities import Player, Base, Enemy
import pygame
from pygame.locals import *
import time
from random import *
from threading import *

pygame.init()


# Color Declaration
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


running = True
fps = 30



window = Window(800,600)
base = Base(window)
player1 = Player(window)


clock = pygame.time.Clock()

rects = []
size = (randint(25, 200), 25)

for count in range(10):
	color = (randint(0,255), randint(0,255), randint(0,255))
	    
	random_size = (randint(25, 100), 25)

	enemy = Enemy(window, color, random_size)
	rects.append(enemy)

while running:
	# TODO: FIX PLAYER GLITCHING THROUGH BASE ***
	# TODO: FIX ENEMY SPAWN OBJECT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player1.y+player1.height == base.y:
				player1.move()

				if player1.y+25 != base.y:
					player1.y += player1.yc
				elif player1.y+25 == base.y:
					player1.yc = 0

	# Determines if Player has collided with the base, if true, then the player stays of then
	if player1.y == player1.jump_threshold:
		player1.yc = 10
	elif player1.y+25 == base.y:
		if event.type == pygame.KEYDOWN:
			player1.yc = 0
	
	

	for r in rects:
		enemy.x -= enemy.speed
		if enemy.x == 0:
			enemy.generate_new(window, size)
		elif enemy.x == player1.x+player1.width and enemy.y == player1.y:
			enemy.speed = 0 
			window.game_over()
			exit()

			
	pygame.display.update()

	window.display.fill(WHITE)

	player1.update(window)
	base.update(window)
	enemy.update(window)

	clock.tick(fps)	



