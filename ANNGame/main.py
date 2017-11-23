from window import Window
from entities import Player, Base
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
player1 = Player()
base = Base(800,600)
player_x = 50
player_y = window.WIN_H/2
base_x = 0
base_y = window.WIN_H/2+25
yc = 0 

clock = pygame.time.Clock()

while running:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player_y+25 == base_y:
				yc = -10
	if player_y == 100:
		yc = 10
	elif player_y+25 == base_y and event.type == pygame.KEYUP:
		yc = 0
	
	
	player_y += yc
	window.display.fill(WHITE)
	player1.update(window, player_x, player_y, BLACK)
	base.update(window, base_x, base_y, BLUE)
	print(player_y)
	
	pygame.display.update()
	clock.tick(fps)
				

