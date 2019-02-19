import pygame
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, incr, color=(0,0,0), depth=0):
 
   trunk_ratio = 0.29       # How big is the trunk relative to whole tree?
   newpos = 0
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   if incr == 0:
      newpos = (u + delta_x*math.cos(heading), v + delta_y*math.sin(heading))
      incr = 1
   elif incr == 1:
      newpos = (u + delta_x*math.sin(heading), v + delta_y*math.cos(heading))
      incr = 0
   pygame.draw.line(main_surface, color, posn, newpos)
   pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])], [(surface_size/2), (surface_size/2)], [(surface_size/2), (surface_size/2)]], 5)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (0, 0, 0)
          color2 = (255, 255, 255)
      elif depth%2 == 0:
          color1 = (255, 0, 0)
          color2 = (0, 255, 255)
      elif depth%3 == 0:
          color1 = (0, 255, 0)
          color2 = (255, 0, 255)
      elif depth%4 == 0:
          color1 = (0, 0, 255)
          color2 = (255, 255, 0)
      elif depth%5 == 0:
          color1 = (255, 0, 255)
          color2 = (0, 255, 0)
      elif depth%6 == 0:
          color1 = (0, 255, 255)
          color2 = (255, 0, 0)
      elif depth%7 == 0:
          color1 = (255, 255, 0)
          color2 = (0, 0, 255)
      elif depth%8 == 0:
          color1 = (255, 255, 255)
          color2 = (0, 0, 0)
      elif depth%9 == 0:
          color1 = (255, 255, 255)
          color2 = (255, 255, 255)
      else:
          color1 = color
          color2 = color

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading-theta, incr, color1, depth+1)
      draw_tree(order-1, thetab, theta, newsz, newpos, heading+theta, incr, color2, depth-1)
      


def gameloop():

    theta1 = 0
    theta2 = 0
    depthincr = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += 0.02
        theta2 += 0.02

        # Draw everything
        main_surface.fill((100, 100, 100))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        #draw_tree(8, theta1, theta2, surface_size*0.9, pygame.mouse.get_pos(), -math.pi/2)

        draw_tree(8, theta1, theta2, surface_size*0.9, pygame.mouse.get_pos(), -math.pi/2, depthincr, color=(0,0,0), depth=depthincr)

        pygame.display.flip()
        my_clock.tick(120)


gameloop()
pygame.quit()
