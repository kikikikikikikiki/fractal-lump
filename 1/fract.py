import pygame 
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((900,800),pygame.HWSURFACE+pygame.DOUBLEBUF+pygame.FULLSCREEN)
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):
   delta_x = 0
   delta_y = 0
   trunk_ratio = 0.09       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.exp(math.sin(heading))
   delta_y = trunk * math.exp(math.cos(heading))

      
      
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos)

   if order > 0:   # Draw another layer of subtrees
      color1 = (order**2,0,0)
      color2 = (order**2,0,0)
      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (255, 0, 0)
          color2 = (0, 0, 255)
      else:
         color1 = (order**2,0,0)
         color2 = (order**2,0,0)

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading-theta+math.sin(theta), color1, depth+1)
      draw_tree(order-1, thetab, theta, newsz, newpos, heading+theta+math.cos(theta), color2, depth+1)


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
        theta1 += 0.02
        theta2 += 0.02
        #inc +=0.0001

        # Draw everything
        main_surface.fill((0, 0, 0))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)
        draw_tree(14, theta1, theta2, surface_size*0.9, pygame.mouse.get_pos(), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(60)


gameloop()
pygame.quit()
