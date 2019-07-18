import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
RED = (255,0,0)

class Pendulum:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.dx = 0
		self.dy = 0
		self.ddx = 0
		self.ddy = 0
		
		self.L = 1



pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pendulum")

done = False

clock = pygame.time.Clock()

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# game logic
	
	screen.fill(WHITE)
	
	# drawing here
	
	
	pygame.display.flip()
	
	clock.tick(60)
pygame.quit()