from video import make_video
import pygame
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 1600
main_surface = pygame.display.set_mode((1600,900))
my_clock = pygame.time.Clock()



def draw_tree(col,order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.071       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.sin((heading*1j).real/5)
   delta_y = trunk * math.sin((heading*1j).imag/5)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, order)
   pygame.draw.line(main_surface, color, newpos, posn, order)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [400, 400]], 0)
   thetaj = theta + 1j
   theta2 = theta + 1j
   gradd = ((128+(128*math.sin((heading*1j).real/5)))/(order+1))*2
   gradd2 = ((128+(128*math.sin((heading*1j).imag/5)))/(order+1))*2
   
   if order > 0 :   # Draw another layer of subtrees
         color1 = (0, gradd, gradd2)
         color2 = (0, gradd, gradd2)
      
      # make the recursive calls to draw the two subtrees
            
         newsz = sz*(1 - trunk_ratio)
         draw_tree(col, order-1, theta, thetab, newsz, clol, clol2, newpos, (heading-theta2), color1, depth+1)
         draw_tree(col, order-1, theta, thetab, newsz, clol, clol2, newpos, (heading+thetaj), color2, depth+1)


def gameloop():

    theta1 = 0
    theta2 = 0
    clol = 0
    clol2 = 0
    ft = 0
    col = 0
    save_screen = make_video(main_surface)
    video = True
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += math.pi/10
        theta2 += math.pi/10

        # Draw everything
        main_surface.fill((0, 0, 0))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        #draw_tree(12, theta1, theta2, surface_size*0.9, clol, clol2, pygame.mouse.get_pos(), -math.pi/2)
        
        draw_tree(col, 15, theta1, theta2, surface_size*0.9, clol, clol2, (800, 450), 0)
        my_clock.tick(20)
        
        if video:
           if ft<30:
              ft+=1
              next(save_screen)
           else:
              video = not video
        pygame.display.flip()

gameloop()
pygame.quit()
