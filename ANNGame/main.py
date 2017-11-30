
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


rects = []
score = 0

running = True
fps = 30

window = Window(800,600)
base = Base(window)
player1 = Player(window)

font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()

for count in range(10):
	color = (randint(0,255), randint(0,255), randint(0,255))    
	random_size = (randint(25, 100), 25)
	enemy = Enemy(window, color, random_size)
	rects.append(enemy)


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player1.yc != 10 and enemy.x != player1.x+player1.width:
				player1.move()

	# Determines if Player has collided with the base, if true, then the player stays on it
	if player1.y == player1.jump_threshold:		
		player1.yc = 10
	elif player1.yc == 10 and player1.y+player1.height == base.y:
		player1.yc = 0

	player1.y += player1.yc


# Enemy spawn logic
	for r in rects:
		sx = randint(25, 200)
		size = (sx, 25)
		enemy.x -= enemy.speed
	if enemy.x == 0:
		enemy.generate_new(window, size)
		print(sx)
		score += 1
	
	elif enemy.x == player1.x+player1.width and enemy.y == player1.y:
		enemy.speed = 0
		window.game_over()

	score_txt = font.render('Score: ' + str(score), False, (0,0,0))

	window.display.blit(score_txt, [10, 10])

	pygame.display.update()

	window.display.fill(WHITE)

	player1.update(window)
	base.update(window)
	enemy.update(window)

	clock.tick(fps)	



