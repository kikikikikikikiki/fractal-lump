from video import make_video
from functools import lru_cache
import pygame
import math
pygame.init()# prepare the pygame module for use

# Create a new surface and window.#
surface_size = 800
surface_x = 800
surface_y = 800
main_surface = pygame.display.set_mode((900,800),pygame.FULLSCREEN+pygame.HWSURFACE)
my_clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


#@lru_cache(maxsize=10000)
def draw_tree(maxord,order, depthprint, theta, thetab, sz, posn, heading, color=(125,100,150), depth=0):
   
   trunk_ratio = 0.1     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.sin(math.exp(math.sin(math.log10(math.exp(math.sin(heading)*math.pi)))))
   delta_y = trunk * math.cos(math.exp(math.cos(math.log10(math.exp(math.cos(heading)*math.pi)))))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y )
   color1 = color
   color2 = color
   if order <10:
      coljuin = (order-maxord)**2
   else:
      coljuin = (order-maxord)**2
   colju = (coljuin, 0, coljuin)
   colju2 = (0, coljuin, 0)
   #if order<11:
   pygame.draw.line(main_surface, color, posn, newpos, order)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      depth = math.ceil(depth)
      if depth == 0:
          color1 = colju
          color2 = colju2
      elif depth%2 == 0:
          color1 = colju
          color2 = colju2
      elif depth%3 == 0:
          color1 = colju
          color2 = colju2
      elif depth%4 == 0:
          color1 = colju
          color2 = colju2
      elif depth%5 == 0:
          color1 = colju
          color2 = colju2
      elif depth%6 == 0:
          color1 = colju
          color2 = colju2
      elif depth%7 == 0:
          color1 = colju
          color2 = colju2
      elif depth%8 == 0:
          color1 = colju
          color2 = colju2
      elif depth%9 == 0:
          color1 = colju
          color2 = colju2
      
      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(maxord, order-1, depthprint, theta*math.sin(heading), thetab*math.sin(heading), newsz, newpos, heading+theta, color1, order+math.sin(heading+theta))
      draw_tree(maxord, order-1, depthprint, theta*math.cos(heading), thetab*math.cos(heading), newsz, newpos, heading+theta+12, color2, order+math.sin(heading+theta))
#@lru_cache(maxsize=10000)
def gameloop():
    depthincr = 20
    theta1 = 1
    theta2 = 0
    save_screen = make_video(main_surface)
    ft = 0
    orrder = 13
    
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
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_d:
            theta1 += 0.1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_f:
            theta1 -= 0.1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_b:
            theta2 += 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_n:
            theta2 -= 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_j:
            depthincr += 1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_k:
            depthincr -= 1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_y:
            orrder -= 1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_u:
            orrder += 1
        # Updates - change the angle
        #theta1 += 0.002
        #theta2 += 0.002
        #depthincr += 1

            # Draw everything
        main_surface.fill((100, 100, 100))
        
        text = font.render("theta1 " + str(theta1), 100, (250, 100, 100))
        textpos = text.get_rect(centerx=200)
        main_surface.blit(text, textpos)
        text = font.render("theta2 " + str(theta2), 100, (250, 100, 100))
        textpos = text.get_rect(centerx=400)
        main_surface.blit(text, textpos)
        text = font.render("depincr " + str(depthincr), 100, (250, 100, 100))
        textpos = text.get_rect(centerx=600)
        main_surface.blit(text, textpos)
        draw_tree(orrder, orrder, int(depthprint), theta1, theta2, surface_size*0.5, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 0,color=(0,0,0), depth=depthincr)
        #draw_tree(12, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, , -math.pi/2, color=(0,0,0), depth=round(pygame.mouse.get_pos()[1]/10))(surface_size//2, surface_size-50)
        #draw_tree(10, (surface_x+pygame.mouse.get_pos()[0])/200, surface_y+pygame.mouse.get_pos()[1]/200, surface_y*0.8, (surface_x/2, surface_y), -math.pi/2)
            
        pygame.display.update()
        pygame.display.flip()
        
        my_clock.tick(60)
        pygame.display.update()    
        if video:
           if ft<1000:
              ft+=1
              next(save_screen)
           else:
              video = not video

gameloop()
pygame.quit()
