import pygame
import math
import math 
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 800
surface_sizeX = 1600
surface_sizeY= 900
main_surface = pygame.display.set_mode((surface_sizeX,surface_sizeY),pygame.HWSURFACE+pygame.FULLSCREEN+pygame.DOUBLEBUF)
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):
   delta_x = 0
   delta_y = 0
   trunk_ratio = 0.2       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.exp(math.sin((heading*1j).real))*math.exp(3)
   delta_y = trunk * math.exp(math.cos((heading*1j).real))*math.exp(3)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   color=(0,0,0)
   pygame.draw.line(main_surface, color, posn, newpos)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (255, 0, 0)
          color2 = (0, 0, 255)
      else:
          color1 = order*10
          color2 = order*10

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading-theta+math.sin(theta+1), color1, depth+1)
      draw_tree(order-1, thetab, theta, newsz, newpos, heading+theta+math.cos(theta+1)+12, color2, depth+1)


def gameloop():

    theta1 = 0
    theta2 = 0
    inc = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += 0.2
        theta2 += 0.2
        #inc +=0.0001

        # Draw everything
        main_surface.fill((255, 255, 0))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)
        draw_tree(14,
                  theta1,
                  theta2,
                  surface_size*0.015,
                  pygame.mouse.get_pos(),
                  -math.pi/2,
                  (pygame.mouse.get_pos()[0]/80,pygame.mouse.get_pos()[0]/80)
                  )

        pygame.display.flip()
        my_clock.tick(60)


gameloop()
pygame.quit()
