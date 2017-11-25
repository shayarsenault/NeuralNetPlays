
from window import Window
from entities import Player, Base, Enemy
import pygame
import time
from random import *

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

for count in range(10):
	color = (randint(0,255), randint(0,255), randint(0,255))
	    
	random_size = (51, 25)

	enemy = Enemy(window, color, random_size)
	rects.append(enemy)

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player1.y+player1.height == base.y:
				player1.move()
	if player1.y == 100:
		player1.yc = 10

	elif player1.y+25 == base.y and event.type == pygame.KEYUP:
		player1.yc = 0

	player1.y += player1.yc
	
	for r in rects:
		enemy.x -= enemy.speed
		if enemy.x == 0:
			enemy.speed = 0
			r.update(window)
		elif enemy.x == player1.y and player1.x+25:
			enemy.speed = 0 
			window.game_over()

	pygame.display.update()

	window.display.fill(WHITE)

	player1.update(window)
	base.update(window)
	enemy.update(window)

	clock.tick(fps)	



