import pygame
from pygame.locals import *
from random import randrange
from window import Window

# Color Declaration
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class Base(Window):
	def __init__(self, win):
		self.x = 0
		self.y = win.height/2+25
	def update(self, win):
		pygame.draw.rect(win.display, BLUE, (self.x, self.y, win.width, 20))
		

class Player(Base):
	def __init__(self, win):
		self.x = 75
		self.y = win.height/2
		self.yc = 0 

		self.width = 25
		self.height = 25

		self.area = self.width * self.height

	def update(self, win):
		pygame.draw.rect(win.display, BLACK, (self.x, self.y, self.width, self.height))

	def move(self):
		self.yc = -10

class Enemy(Window):
	def __init__(self, win, color, size):
		
		self.color = color
		self.size = size
		self.x = win.width
		self.y = win.height/2
		self.speed = 5

		self.enemies = []

	def update(self, win):
		pygame.draw.rect(win.display, self.color, Rect((self.x, self.y), self.size))
		
	def move_and_gen(self):
		pass
		




