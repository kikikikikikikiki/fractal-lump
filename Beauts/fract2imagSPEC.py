from video import make_video
from functools import lru_cache
import pygame
import math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 1600
main_surface = pygame.display.set_mode((1600,900),pygame.HWSURFACE+pygame.DOUBLEBUF+pygame.FULLSCREEN)
my_clock = pygame.time.Clock()

#@lru_cache(maxsize = None)
def draw_tree(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol, clol2, clol2)
      color2 = (clol2, clol2, clol)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color1, depth+1)
      draw_tree(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+theta2), color2, depth+1)

def draw_tree2(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 2, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (clol2, clol2, clol)
      color2 = (clol, clol2, clol2)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree2(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading+thetaj), color1, depth+1)
      draw_tree2(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading+theta2), color2, depth+1)
def draw_tree3(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi)
   delta_y = trunk * math.sin((heading).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol/2, clol2/2, 0)
      color2 = (clol2/2, clol2/2, 0)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree3(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+theta2), color1, depth+1)
      draw_tree3(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+thetaj), color2, depth+1)

def draw_tree4(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi)
   delta_y = trunk * math.sin((heading*(math.pi)).real)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (0, clol2/2, clol2)
      color2 = (0, clol2/2, clol)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree4(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading+theta2), color1, depth+1)
      draw_tree4(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color2, depth+1)
def draw_tree5(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi)
   delta_y = trunk * math.sin((heading*(math.pi)).real)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol/2, clol2/2, 0)
      color2 = (clol2/2, clol2/2, 0)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree5(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color1, depth+1)
      draw_tree5(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+theta2), color2, depth+1)

def draw_tree6(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi)
   delta_y = trunk * math.sin((heading*(math.pi)).real)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (0, clol2/2, clol2)
      color2 = (0, clol2/2, clol)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree6(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading+thetaj), color1, depth+1)
      draw_tree6(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading+theta2), color2, depth+1)
def draw_tree7(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi/2)
   delta_y = trunk * math.sin((heading).real)*(math.pi/2)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol, clol2, 0)
      color2 = (clol2, clol2, 0)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree7(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+theta2), color1, depth+1)
      draw_tree7(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+thetaj), color2, depth+1)

def draw_tree8(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi/2)
   delta_y = trunk * math.sin((heading).real)*(math.pi/2)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (0, clol2, clol2/2)
      color2 = (0, clol2, clol/2)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree8(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading+theta2), color1, depth+1)
      draw_tree8(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color2, depth+1)
def draw_tree9(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi/2)
   delta_y = trunk * math.sin((heading).real)*(math.pi/2)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol, clol2, 0)
      color2 = (clol2, clol2, 0)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree9(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+theta2), color1, depth+1)
      draw_tree9(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+thetaj), color2, depth+1)

def draw_tree10(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi/2)
   delta_y = trunk * math.sin((heading).real)*(math.pi/2)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (0, clol2, clol2/2)
      color2 = (0, clol2, clol/2)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree10(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading+theta2), color1, depth+1)
      draw_tree10(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color2, depth+1)
def draw_tree11(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol, clol2, clol2)
      color2 = (clol2, clol2, clol)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree11(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading-thetaj), color1, depth+1)
      draw_tree11(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading-theta2), color2, depth+1)

def draw_tree12(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 1, 1)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (clol2, clol2, clol)
      color2 = (clol, clol2, clol2)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree12(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree12(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading-theta2), color2, depth+1)
#@lru_cache(maxsize = None)
def gameloop():
    rendord = 2
    theta1 = 9.87
    theta2 = 6.10
    theta12 = -9.87
    theta22 = -6.10
    clol = 0
    clol2 = 0
    ft = 0
    inord = 12
    screen_size = (800, 450)
    save_screen = make_video(main_surface)
    video = False
    while True:

        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        #theta1 += 0.015
        #theta2 += 0.02
        theta1 +=  0.00987
        theta2 +=  0.00610
        theta12 -= 0.00987
        theta22 -= 0.00610
        # Draw everything
        main_surface.fill((0, 0, 0))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        #draw_tree(13, theta1, theta2, surface_size*0.9, clol, clol2, pygame.mouse.get_pos(), -math.pi/2)

        draw_tree5(rendord, inord, inord, theta1, theta2, surface_size*0.25, clol, clol2,screen_size , math.pi/2)
        draw_tree6(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_tree7(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_tree8(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_tree9(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree10(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree3(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree4(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree2(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree11(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_tree12(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        
        if video:
           if ft<600:
              ft+=1
              pygame.display.flip()
              next(save_screen)
           else:
              video = not video        
        my_clock.tick(60)
        pygame.display.flip()
        


gameloop()
pygame.quit()
