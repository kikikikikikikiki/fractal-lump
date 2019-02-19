import pygame
import math
pygame.init()   


surface_size = 1000
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.1618       
   trunk = sz * trunk_ratio
   delta_x = trunk * ((math.cos((1j*heading).real)* (1*1j)+1  )).real
   delta_y = trunk * ((math.sin((1j*heading).imag)* (1*1j)+1  )).imag
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, order)
   

   if order > 0:
      if depth == 0:
          color1 = (0,255,255)
          color2 = (255,255,0)
      else:
          color1 = (0,255,255)
          color2 = (255,255,0)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, thetab, theta, newsz, newpos, (heading+thetab)*1j, color1, depth+1)
      draw_tree(order-1, theta, thetab, newsz, newpos, (heading-theta)*-1j, color2, depth+1)
      
def gameloop():

    theta1 = 0
    theta2 = 0
    imagine = 0
    imaginej = 0
    imagine2 = 0
    incr = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += 0.02
        theta2 -= 0.02
        imagine += 0.2
        imagine2 -= 0.2

        # Draw everything
        main_surface.fill((20, 20, 20))
        draw_tree(12, theta1, theta2, surface_size*0.3, pygame.mouse.get_pos(), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(120)


gameloop()
pygame.quit()
