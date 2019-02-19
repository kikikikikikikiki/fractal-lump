from video import make_video
from functools import lru_cache
import pygame
import math
pygame.init()# prepare the pygame module for use

# Create a new surface and window.#
surface_size = 800
surface_x = 800
surface_y = 800
main_surface = pygame.display.set_mode((1600,900),pygame.HWSURFACE+pygame.DOUBLEBUF+pygame.FULLSCREEN)
my_clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)



def draw_tree(gen, order, depthprint, theta, thetab, sz, posn, heading, color=(125,100,150), depth=0):

   trunk_ratio = 0.19     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading*1j.real)*math.sin(heading*1j.imag)
   delta_y = trunk * math.sin(heading*1j.imag)*math.cos(heading*1j.imag)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y )
   colju = (order-1)*16
   pygame.draw.line(main_surface, color, posn, newpos, order)

  # pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])], [(surface_size/2), (surface_size/2)], [(surface_size/2), (surface_size/2)]], 5)
   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      depth = math.floor(depth)
      if depth == 0:
          color1 = color
          color2 = color
      elif depth%2 :
          color1 = (colju, colju, colju)
          color2 = (colju, colju, colju)
      elif depth%3 == 0 :
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
          color2 = (0,0,0)
      elif depth%10 == 0:
          color1 = (255,255,255)
          color2 = (255,255,255)
      else:
          color1 = (colju, colju, colju)
          color2 = (colju, colju, colju)

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(gen, order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, newpos, heading+theta-5.3, color1, depth+math.sin(heading+math.pi))
      draw_tree(gen, order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, newpos, heading+theta+1, color2, depth+math.sin(heading+math.pi))

def gameloop():
    gen = 1
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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            gen+=0.1
            # Updates - change the angle
        theta1 += math.pi/500
        theta2 += math.pi/500
        #0.009
        depthincr =0

            # Draw everything
        main_surface.fill((0, 0, 0))
        text = font.render("theta1 " + str(gen), 100, (250, 100, 100))
        textpos = text.get_rect(centerx=200)
        main_surface.blit(text, textpos)
        draw_tree(gen, 12, depthprint, theta1, theta2, surface_size*2, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 0,color=(10,10,10), depth=depthincr)
        #draw_tree(12, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, , -math.pi/2, color=(0,0,0), depth=round(pygame.mouse.get_pos()[1]/10))(surface_size//2, surface_size-50)
        #draw_tree(10, (surface_x+pygame.mouse.get_pos()[0])/200, surface_y+pygame.mouse.get_pos()[1]/200, surface_y*0.8, (surface_x/2, surface_y), -math.pi/2)
            
        pygame.display.update()
        pygame.display.flip()
        
        my_clock.tick(60)
        #pygame.display.update()    
        if video:
           if ft<600:
              ft+=1
              next(save_screen)
           else:
              video = not video

gameloop()
pygame.quit()
