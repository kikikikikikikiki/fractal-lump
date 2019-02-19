import pygame
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, incr, line, color=(0,0,0), depth=0):
 
   trunk_ratio = 0.29       # How big is the trunk relative to whole tree?
   newpos = 0
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   colju = (16-order)*15
   if incr == 0:
      newpos = (u + delta_x*math.cos(heading), v + delta_y*math.sin(heading))
      incr = 1
   elif incr == 1:
      newpos = (u + delta_x*math.sin(heading), v + delta_y*math.cos(heading))
      incr = 0
   elif incr == 2:
      newpos = (u + delta_x*math.sin(heading), v + delta_y*math.cos(heading))
      incr = 0
   elif incr == 3:
      newpos = (u + delta_x*math.sin(heading), v + delta_y*math.cos(heading))
      incr = 0
   pygame.draw.line(main_surface, color, posn, newpos)
   #pygame.draw.circle(main_surface, color, [int(posn[0]),int(posn[1])], order*2, order)
  
   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      depth = math.ceil(depth)
      if depth == 0:
          color1 = color
          color2 = color
      elif depth%2 == 0:
          color1 = color
          color2 = color
      elif depth%3 == 0 & depth%9 != 0:
          color1 = (colju, 0, 0)
          color2 = (0, colju, colju)
      elif depth%4 == 0:
          color1 = (0, colju, 0)
          color2 = (colju, 0, colju)
      elif depth%5 == 0:
          color1 = (0, 0, colju)
          color2 = (colju, colju, 0)
      elif depth%6 == 0:
          color1 = (0, colju, colju)
          color2 = (colju, 0, 0)
      elif depth%7 == 0:
          color1 = (colju, 0, colju)
          color2 = (0, colju, 0)
      elif depth%8 == 0:
          color1 = (colju, colju,0)
          color2 = (0, 0, colju)
      elif depth%9 == 0:
          color1 = (colju, colju, colju)
          color2 = (0, 0, 0)
      else:
          color1 = color
          color2 = color

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading+theta, incr, order, color1, ((depth+12)/15)*10)
      draw_tree(order-1, thetab, theta, newsz, newpos, heading-theta, incr, order, color2, ((depth+9)/15)*10)
      


def gameloop():
    depthincr = 0
    theta1 = 0
    theta2 = 0
    line = 10
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        
        if ev.type == pygame.QUIT:
            break;
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_ESCAPE:
            break;
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_v:
            video = not video
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_x:
            pygame.key.set_repeat(1,10)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_RIGHTBRACKET:
            theta1 += 0.01
            theta2 += 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_LEFTBRACKET:
            theta1 -= 0.01
            theta2 -= 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_g:
            theta1 += 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_h:
            theta1 -= 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_b:
            theta2 += 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_n:
            theta2 -= 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_j:
            depthincr += 1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_k:
            depthincr -= 1
        # Updates - change the angle
        #theta1 += 0.002
        #theta2 += 0.002
        #depthincr += 1
        if line == 1:
           line = 10


        # Draw everything
        main_surface.fill((100, 100, 100))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        #draw_tree(8, theta1, theta2, surface_size*0.9, pygame.mouse.get_pos(), -math.pi/2)

        draw_tree(12, theta1, theta2, surface_size*0.9, pygame.mouse.get_pos(), -math.pi/2, 0, line, color=(0,0,0),depth=depthincr )

        pygame.display.flip()
        my_clock.tick(60)


gameloop()
pygame.quit()
