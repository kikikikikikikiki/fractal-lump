import pygame
import math

from video import make_video
pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((1600,900),pygame.FULLSCREEN+pygame.DOUBLEBUF)
my_clock = pygame.time.Clock()

def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   
   trunk_ratio = 0.1618       
   trunk = sz * trunk_ratio
   delta_x = trunk * calc_fourier_seriesx(heading)
   delta_y = trunk * math.cos(heading)
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, order)
   pygame.draw.line(main_surface, color, newpos, posn, order)

   gradient = 256-(order**2)
   gradient2 = order**2
   

   if order > 0:
      if depth == 0:
          color1 = (gradient,gradient,gradient)
          color2 = (0,gradient,gradient)
      else:
          color1 = (255,gradient,gradient)
          color2 = (0,gradient,gradient)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, (heading+theta), color1, depth+1)
      draw_tree(order-1, theta, thetab, newsz, newpos, (heading-theta), color2, depth)

def calc_fourier_seriesx(heading):
    inc = 1
    something = 0
    for x in range(1):
        something += ((math.sin(inc*heading))/inc) 
        inc +=2
    return something
    
def gameloop():
    theta1 = 0
    theta2 = 0
    ft = 0
    save_screen = make_video(main_surface)
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 = 0.20
        theta2 = 0.20

        # Draw everything
        main_surface.fill((0, 0, 0))
        draw_tree(10, theta1, theta2, surface_size*1.2, (800,1000), math.pi)

        pygame.display.flip()
        if False:
           if ft<14:
              ft+=1
              pygame.display.flip()
              next(save_screen)
           else:
              video = not video
              break
        else:
              pygame.display.flip()
              #break
        my_clock.tick(120)



gameloop()
pygame.quit()
