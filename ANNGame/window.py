import pygame
from pygame.locals import *
import time

# Color Declaration
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class Window:
	def __init__(self, width, height):
		
		self.height = height
		self.width = width
		
		self.display = pygame.display.set_mode((self.width, self.height))
		
		self.font = pygame.font.SysFont(None, 30)	
		self.gameOverText = self.font.render('Game Over', False, (0,0,0))

		pygame.display.set_caption('A neural net')
		
		pygame.display.update()
		
	def game_over(self):
		self.display.blit(self.gameOverText, [self.width/2-25, self.height/2-100])
		

