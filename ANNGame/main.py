from window import Window
from entities import Player, Base, Enemy
import pygame
import time


pygame.init()

# Color Declaration
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


running = True
fps = 60

window = Window(800,600)
base = Base(window)
player1 = Player(window)
enemy = Enemy(window)

clock = pygame.time.Clock()

while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player1.y+player1.height == base.y:
				player1.move()
	if player1.y == 100:
		player1.yc = 10

	elif player1.y+25 == base.y and event.type == pygame.KEYUP and event.type != pygame.KEYDOWN:
		player1.yc = 0
			
	player1.y += player1.yc



	window.display.fill(WHITE)
	player1.update(window)
	base.update(window)
	enemy.update(window)


	pygame.display.update()
	clock.tick(fps)
				

