import pygame
import math
import numpy as np
from functools import lru_cache
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((1600,900),pygame.HWSURFACE+pygame.DOUBLEBUF+pygame.FULLSCREEN)
my_clock = pygame.time.Clock()

def steping(steep):
   steep += 1
   return steep
@lru_cache(maxsize=10000)
def draw_tree(order, theta, thetab, sz, step, clol, clol2, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = math.e/10      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   a = heading+2j
   b = theta+2j
   delta_x = trunk * math.sin(math.log10(math.exp(((a.real)*b.imag)/2)))
   delta_y = trunk * math.cos(math.log10(math.exp(((a.imag)*b.real)/2)))
   #delta_y = trunk * math.cos(math.log10(math.exp((heading+(theta))/2)))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y )
   pygame.draw.line(main_surface, color, posn, newpos, order+1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [400, 400]], 0)
   

   if order > 0:   # Draw another layer of subtrees
      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
         if order == 16:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 15:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 14:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 13:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 12:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 11:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 10:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 9:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 8:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 7:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 6:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 5:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 4:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 3:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 2:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 1:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         else:
            color1 = (0, 0, 0)
            color2 = (0, 0, 0)

      # make the recursive calls to draw the two subtrees
         newsz = sz*(1 - trunk_ratio)
         draw_tree(order-1, theta, thetab, newsz, step, clol+order*2, clol2+order*2, newpos, heading-math.fabs(math.exp(math.sin(theta))), color1, depth)
         draw_tree(order-1, thetab, theta, newsz, step, clol, clol2, newpos, heading-math.fabs(math.exp(math.sin(theta))), color2, depth+1)

def gameloop():
    depthincr = 0
    theta1 = 0
    theta2 = 0
    colol = 0
    colol2 = 0
    step = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += 0.02
        theta2 += 0.009
        depthincr +=1
        #colol +=1
        if colol>100:
           colol = 0
        # Draw everything
        main_surface.fill((0, 0, 0))
        draw_tree(12, theta1, theta2, surface_size*1.1, step, colol, colol2, pygame.mouse.get_pos(), -math.pi/2, color=(0,0,0), depth=depthincr)
        #draw_tree(12, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, , -math.pi/2, color=(0,0,0), depth=round(pygame.mouse.get_pos()[1]/10))
        #(surface_size//2, surface_size-50)
        #draw_tree(13, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, (surface_size//2, surface_size-100), -math.pi/2)
        
        pygame.display.update()
        pygame.display.flip()
        my_clock.tick(60)


gameloop()
pygame.quit()
