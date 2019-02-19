from video import make_video
from functools import lru_cache
import pygame
import math
pygame.init()# prepare the pygame module for use

# Create a new surface and window.#
surface_size = 800
surface_x = 800
surface_y = 800
main_surface = pygame.display.set_mode((900,600),pygame.HWSURFACE+pygame.DOUBLEBUF+pygame.FULLSCREEN)
my_clock = pygame.time.Clock()


#@lru_cache(maxsize=10000)
def draw_tree(order, depthprint, theta, thetab, sz, posn, heading, color=(125,100,150), depth=0):

   trunk_ratio = 0.03     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.exp(math.cos(heading))
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y )
   colju = order*11
   pygame.draw.line(main_surface, color, posn, newpos, order)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      depth = math.ceil(depth)
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
      draw_tree(order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, newpos, heading+theta, color1, depth+(theta*math.sin(heading)))
      draw_tree(order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, newpos, heading+theta+12, color2, depth+(theta*math.sin(heading)))
#@lru_cache(maxsize=10000)
def gameloop():
    depthincr = 0
    theta1 = 0
    theta2 = 0
    save_screen = make_video(main_surface)
    ft = 0
    depthprint = 1
    #video = True
    video = False
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
        theta1 += 0.002
        theta2 += 0.002
        #depthincr += 1

            # Draw everything
        main_surface.fill((0, 0, 0))
        draw_tree(12, depthprint, theta1, theta2, surface_size*0.9, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 0,color=(0,0,0), depth=depthincr)
        #draw_tree(12, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, , -math.pi/2, color=(0,0,0), depth=round(pygame.mouse.get_pos()[1]/10))(surface_size//2, surface_size-50)
        #draw_tree(10, (surface_x+pygame.mouse.get_pos()[0])/200, surface_y+pygame.mouse.get_pos()[1]/200, surface_y*0.8, (surface_x/2, surface_y), -math.pi/2)
            
        pygame.display.update()
        pygame.display.flip()
        
        my_clock.tick(60)
        #pygame.display.update()    
        if video:
           if ft<1000:
              ft+=1
              next(save_screen)
           else:
              video = not video

gameloop()
pygame.quit()
