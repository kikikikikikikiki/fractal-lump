import pygame
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.15       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)
   delta_y = trunk * math.sin((heading*1j).real)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos,2)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [400, 400]], 0)
   thetaj = theta + 6j
   theta2 = theta + 3j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if True:
          color1 = (order*10, 0, 0)
          color2 = (0, 0, order*10)
      else:
          color1 = color
          color2 = color
      
      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, (heading+theta2), color1, depth+1)
      draw_tree(order-1, thetab, theta, newsz, newpos, (heading+thetaj), color2, depth+1)


def gameloop():

    theta1 = 0
    theta2 = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += 0.015
        theta2 += 0.02

        # Draw everything
        main_surface.fill((0, 0, 0))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        draw_tree(16, theta1, theta2, surface_size*0.9, pygame.mouse.get_pos(), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(60)


gameloop()
pygame.quit()
