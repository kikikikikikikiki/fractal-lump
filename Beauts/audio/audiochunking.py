import pygame
import math
pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((1600,900))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.1618       
   trunk = sz * trunk_ratio
   delta_x = trunk * math.sin((heading*1j).real)
   delta_y = trunk * math.sin((heading*1j).imag)

   thetaj = theta+1j
   thetai = theta+1j
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, 1)
   

   if order > 0:
      if depth == 0:
          color1 = (255,255,255)
          color2 = (255,255,255)
      else:
          color1 = (255,255,255)
          color2 = (255,255,255)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading+thetaj, color1, depth+1)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading-thetai, color2, depth+1)
      
def gameloop():
    theta1 = 0
    theta2 = 0
    
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += 0.002
        theta2 -= 0.002
        # Draw everything
        main_surface.fill((0, 0, 0))
        draw_tree(12, theta1, theta2, surface_size*1.2, (800,450), math.pi)

        pygame.display.flip()
        my_clock.tick(30)


gameloop()
pygame.quit()
