import pygame
import  math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 800
main_surface = pygame.display.set_mode((800,800),pygame.HWSURFACE+pygame.DOUBLEBUF)
my_clock = pygame.time.Clock()

def drawline():
    pygame.draw.line(main_surface, (20,20,20), [0,0],[400,400],5)

drawline()
