import pygame


# Color Declaration
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class Window:
	def __init__(self, WIN_W, WIN_H):
		
		self.WIN_H = WIN_H
		self.WIN_W = WIN_W
		
		self.display = pygame.display.set_mode((self.WIN_W, self.WIN_H))
		
		pygame.display.set_caption('A neural net')
		
		pygame.display.update()
