import pygame
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 900
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()


def draw_tree(imagine2, imaginej, imagine, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.1618       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * (math.sin(heading) + math.e**(1j*imagine)).imag
   delta_y = trunk * (calc_fourier_series(heading) + math.e**(1j*imagine)).real
   #delta_y = trunk * (math.cos(heading) + math.e**(1j*imagine)).real
   deepth = depth * 10
   delta_xc = 127+(deepth*(math.cos(heading)))
   delta_yc = 127+(deepth*(math.sin(heading)))
   delta_zc = 127+(deepth*((imaginej*math.sin(imagine)).imag)/7)
   delta_zc2 = 127+(deepth*((imaginej*math.cos(imagine)).imag)/7)
   #delta_xc = theta
   #delta_yc = thetab
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, order)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [400, 400]], 0)
   

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (delta_xc, delta_yc, delta_zc)
          color2 = (delta_xc, delta_yc, delta_zc2)
      else:
          color1 = (delta_xc, delta_yc, delta_zc)#deepth*2)
          color2 = (delta_xc, delta_yc, delta_zc)#deepth*2)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(imagine2, imaginej*imagine, imagine, order-1, thetab, theta, newsz, newpos, (heading+theta)+1, color1, depth+1)
      draw_tree(imagine2, imaginej*imagine2, imagine, order-1, theta, thetab, newsz, newpos, (heading-theta)-1, color2, depth+1)
      

def calc_fourier_series(heading):
    inc = 1
    something = 0
    for x in range(100):
        something += ((math.sin(inc*heading))/inc) 
        inc +=2
    return something

def gameloop():

    theta1 = 0
    theta2 = 0
    imagine = 0
    imaginej = 0
    imagine2 = 0
    incr = 0
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta1 += 0.002
        theta2 += 0.002
        imagine += 0.03
        imagine2 -= 0.09

        # Draw everything
        main_surface.fill((20, 20, 20))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        draw_tree(imagine2, +math.pi/2, imagine, 8, theta1, theta2, surface_size*0.3, pygame.mouse.get_pos(), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(60)


gameloop()
pygame.quit()
