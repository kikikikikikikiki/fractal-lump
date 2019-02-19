from video import make_video
from functools import lru_cache
import pygame
import math
pygame.init()# prepare the pygame module for use

# Create a new surface and window.#
surface_size = 800
surface_x = 800
surface_y = 800
main_surface = pygame.display.set_mode((1000,800))
my_clock = pygame.time.Clock()


#@lru_cache(maxsize=10000)
def draw_tree(order, depthprint, theta, thetab, sz, clol, clol2, posn, heading, color=(125,100,150), depth=0):

   trunk_ratio = 0.19     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.exp(math.cos(heading))
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y )
   colju = order*9
   pygame.draw.line(main_surface, color, posn, newpos, order)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
         if order == 16:
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
            color1 = (0, clol, 255)
            color2 = (0, clol2, 255)

      # make the recursive calls to draw the two subtrees
         newsz = sz*(1 - trunk_ratio)
         draw_tree(order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, clol+12, clol2+12, newpos, heading+theta*1j.imag, color1, depth+(theta*math.sin(heading)))
         draw_tree(order-1, depthprint, theta*math.cos(heading), thetab*math.sin(heading), newsz, clol+6, clol2+6, newpos, heading+theta*1j.real, color2, depth+(theta*math.sin(heading)))
#@lru_cache(maxsize=10000)
def gameloop():
    depthincr = 0
    theta1 = 0
    theta2 = 0
    save_screen = make_video(main_surface)
    ft = 0
    colol = 0
    colol2 = 0
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
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_r:
            theta1 *= 1j
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_t:
            theta1 *= 1j
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_n:
            theta2 -= 0.01
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_j:
            depthincr += 1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_k:
            depthincr -= 1
      
        # Updates - change the angle
        #theta1 += 0.004
        #theta2 += 0.004
        #depthincr += 1

            # Draw everything
        main_surface.fill((0, 0, 0))
        #draw_tree(12, depthprint, theta1, theta2, surface_size*0.9, colol, colol2, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 0,color=(0,0,0), depth=depthincr)
        draw_tree(12, depthprint, theta1, theta2, surface_size/2, colol, colol2, (0, 400), 0,color=(0,0,0), depth=depthincr)
            
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
