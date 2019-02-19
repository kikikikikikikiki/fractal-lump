from video import make_video
from functools import lru_cache
import pygame
import math
pygame.init()# prepare the pygame module for use

# Create a new surface and window.#
surface_size = 900
surface_x = 1600
surface_y = 900
main_surface = pygame.display.set_mode((1600,900))
my_clock = pygame.time.Clock()


@lru_cache(maxsize=10000)
def draw_tree(order, flip, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.2     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   colju = order*14
   pygame.draw.line(main_surface, color, posn, newpos, order)
   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (200-colju, 0, 0)
          color2 = (0, 0, 200-colju)
      elif depth%2 == 0:
          color1 = (0, 200-colju, 0)
          color2 = (0, 0, 200-colju)
      elif depth%3 == 0:
          color1 = (0, 200-colju, 0)
          color2 = (0, 200-colju, 0)
      elif depth%4 == 0:
          color1 = (0, 0, 200-colju)
          color2 = (0, 200-colju, 0)
      elif depth%5 == 0:
          color1 = (0, 0, 200-colju)
          color2 = (200-colju, 0, 0)
      elif depth%6 == 0:
          color1 = (200-colju, 0, 200-colju)
          color2 = (200-colju, 0, 0)
      elif depth%7 == 0:
          color1 = (200-colju, 0, 200-colju)
          color2 = (0, 200-colju, 200-colju)
      elif depth%8 == 0:
          color1 = (100, 100, 100)
          color2 = (200, 200, 200)
      elif depth%9 == 0:
          color1 = (200, 100, 200)
          color2 = (100, 200, 100)
      elif depth%10 == 0:
          color1 = (255, 255, 255)
          color2 = (255, 255, 255)
      else:
          color1 = (100, 0, 100)
          color2 = (0, 100, 0)

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      if flip == 0:
         flip = 1
         draw_tree(order-1, flip, theta, thetab, newsz, newpos, heading+theta+math.sin(heading), color1, depth)
         draw_tree(order-1, flip, thetab, theta, newsz, newpos, heading+theta+math.cos(heading), color2, depth+1)
      elif flip == 1:
         flip = 0
         draw_tree(order-1, flip, theta, thetab, newsz, newpos, heading+theta+math.sin(heading), color1, depth)
         draw_tree(order-1, flip, thetab, theta, newsz, newpos, heading+theta+math.cos(heading), color2, depth+1)


@lru_cache(maxsize=10000)
def gameloop():
    depthincr = 0
    theta1 = 0
    theta2 = 0
    save_screen = make_video(main_surface)
    ft = 0
    flip = 0
    video = True
    while True:

        # Handle evente from keyboard, mouse, etc.
        
        event = pygame.event.poll()
            

        if event.type == pygame.QUIT:
            break;
        elif event.type == pygame.KEYDOWN  and event.key == pygame.K_ESCAPE:
            break;
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            video = not video
            # Updates - change the angle
        theta1 += 0.001
        theta2 += 0.001
        depthincr +=1

            # Draw everything
        main_surface.fill((100, 100, 100))
        draw_tree(14, flip, theta1, theta2, surface_size*0.8, (surface_x/2, surface_y/2+300), -math.pi/2, color=(0,0,0),depth=depthincr)
        #draw_tree(12,flip, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, , -math.pi/2, color=(0,0,0), depth=round(pygame.mouse.get_pos()[1]/10))(surface_size//2, surface_size-50)
        #draw_tree(10, flip,(surface_x+pygame.mouse.get_pos()[0])/200, surface_y+pygame.mouse.get_pos()[1]/200, surface_y*0.8, (surface_x/2, surface_y), -math.pi/2)
            

        pygame.display.flip()
        my_clock.tick(60)
            
        if video:
           if ft<500:
              ft+=1
              next(save_screen)
           else:
              video = not video

gameloop()
pygame.quit()
