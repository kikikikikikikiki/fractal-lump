import pygame
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.15       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.sin((heading*1j).real)
   delta_y = trunk * math.cos((heading*1j).imag)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, order)
   #pygame.draw.line(main_surface, color, newpos, posn, order)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [400, 400]], 0)
   thetaj = theta + 2j
   theta2 = theta + 0j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
         if order == 20:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 19:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 18:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 17:
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)
         elif order == 16:
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
         draw_tree(order-1, theta, thetab, newsz, clol+12, clol2+12, newpos, (heading+theta2)+12, color1, depth+1)
         draw_tree(order-1, thetab, theta, newsz, clol, clol2, newpos, (heading+thetaj), color2, depth+1)


def gameloop():

    theta1 = 0
    theta2 = 0
    clol = 0
    clol2 = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_RIGHTBRACKET:
            theta1 -= 0.01j
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_LEFTBRACKET:
            theta1 += 0.01j
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_v:
            theta1 -= 0.02
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_c:
            theta1 += 0.02
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_p:
            theta2 -= 0.01j
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_o:
            theta2 += 0.01j
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_d:
            theta2 -= 0.02
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_f:
            theta2 += 0.02
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_x:
            pygame.key.set_repeat(1,10)

        # Updates - change the angle
        #theta1 += 0.02
        #theta2 += 0.02

        # Draw everything
        main_surface.fill((100, 0, 0))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        draw_tree(12, theta1, theta2, surface_size*0.9, clol, clol2, pygame.mouse.get_pos(), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(60)


gameloop()
pygame.quit()
