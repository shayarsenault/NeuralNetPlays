import pygame
from window import Window

# Color Declaration
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Player(Window):
	def update(self, win, x, y, color):
		pygame.draw.rect(win.display, color, (x, y, 25, 25))

class Base(Window):
	def update(self, win, x, y, color):
		pygame.draw.rect(win.display, color, (x, y, win.WIN_W, 10))


		