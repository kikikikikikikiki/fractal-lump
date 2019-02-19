from video import make_video
import pygame
import math
pygame.init()# prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((800,800))
my_clock = pygame.time.Clock()



def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.29       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y + 20)
   pygame.draw.line(main_surface, color, posn, newpos, order)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (255, 0, 0)
          color2 = (0, 0, 255)
      elif depth%2 == 0:
          color1 = (0, 255, 0)
          color2 = (0, 0, 255)
      elif depth%3 == 0:
          color1 = (0, 255, 0)
          color2 = (0, 255, 0)
      elif depth%4 == 0:
          color1 = (0, 0, 255)
          color2 = (0, 255, 0)
      elif depth%5 == 0:
          color1 = (0, 0, 255)
          color2 = (255, 0, 0)
      elif depth%6 == 0:
          color1 = (255, 0, 255)
          color2 = (255, 0, 0)
      elif depth%7 == 0:
          color1 = (255, 0, 255)
          color2 = (0, 255, 255)
      else:
          color1 = color
          color2 = color

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading+theta, color1, depth)
      draw_tree(order-1, thetab, theta, newsz, newpos, heading-theta, color2, depth+1)

def gameloop():
    depthincr = 0
    theta1 = 0
    theta2 = 0
    save_screen = make_video(main_surface)
    video = False
    while True:

        # Handle evente from keyboard, mouse, etc.
        
        event = pygame.event.poll()
            

        if event.type == pygame.QUIT:
            break;
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            video = not video
            # Updates - change the angle
        theta1 += 0.009
        theta2 += 0.009
        depthincr +=1

            # Draw everything
        main_surface.fill((0, 0, 0))
        draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-400), -math.pi/2, color=(0,0,0),)
            #draw_tree(12, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, , -math.pi/2, color=(0,0,0), depth=round(pygame.mouse.get_pos()[1]/10))
            #(surface_size//2, surface_size-50)
            #draw_tree(13, pygame.mouse.get_pos()[0]/100, pygame.mouse.get_pos()[1]/100, surface_size*0.9, (surface_size//2, surface_size-100), -math.pi/2)
            

        pygame.display.flip()
        my_clock.tick(250)
            
        if video:
            next(save_screen) 

gameloop()
pygame.quit()
