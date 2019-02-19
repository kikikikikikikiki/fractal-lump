from video import make_video
from functools import lru_cache
import pygame
import math
pygame.init()# prepare the pygame module for use

# Create a new surface and window.#
surface_size = 800
surface_x = 800
surface_y = 800
main_surface = pygame.display.set_mode((900,800))#pygame.HWSURFACE+pygame.DOUBLEBUF+pygame.FULLSCREEN)
my_clock = pygame.time.Clock()



def draw_tree(order, depthprint, theta, thetab, sz, posn, heading, color=(125,100,150), depth=0):

   trunk_ratio = 0.09     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y )
   colju = (order)**2
   pygame.draw.line(main_surface, color, posn, newpos, order)

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
         if depthprint == 1:
            #print(depth)
            color1 = (0, 0, 0)
            color2  = (0, 0, 0)
            depthprint = 0
         else:
            color1 = (0, 0,0)
            color2 = (0,0, 0)

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, newpos, heading+theta, color1, (((depth+math.pi)/15)*10))
      draw_tree(order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, newpos, heading+theta+math.exp(1), color2, (((depth+math.pi)/15)*10))

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
        
        event = pygame.event.poll()
            

        if event.type == pygame.QUIT:
            break;
        elif event.type == pygame.KEYDOWN  and event.key == pygame.K_ESCAPE:
            break;
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            video = not video
            # Updates - change the angle
        theta1 += surface_x+pygame.mouse.get_pos()[0]/400
        theta2 += surface_y+pygame.mouse.get_pos()[1]/200
        depthincr +=1

            # Draw everything
        main_surface.fill((0, 0, 0))
        draw_tree(10, depthprint, theta1, theta2, surface_size*0.8, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 0)
        #draw_tree(12, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, , -math.pi/2, color=(0,0,0), depth=round(pygame.mouse.get_pos()[1]/10))(surface_size//2, surface_size-50)
        #draw_tree(10, depthprint,(surface_x+pygame.mouse.get_pos()[0])/200, surface_y+pygame.mouse.get_pos()[1]/200, surface_y*0.8, (surface_x/2, surface_y), -math.pi/2)
            
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
