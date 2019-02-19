from video import make_video
import pygame
import  math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size = 1000
main_surface = pygame.display.set_mode((800,800),pygame.HWSURFACE)
my_clock = pygame.time.Clock()

#@lru_cache(maxsize = None)
def draw_tree(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.016180327868852*8      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * (math.sin(((heading*1j)).real*(math.pi))+math.sin(((heading*1j)).real*(math.pi)))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol, clol2, clol2, 127)
      color2 = (clol2, clol2, clol, 127)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color1, depth+1)
      draw_tree(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+theta2), color2, depth+1)
def draw_treez(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.016180327868852*8      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * (math.sin(((heading*1j)).real))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      draw_treez(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color1, depth+1)
      draw_treez(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+theta2), color2, depth+1)

def draw_tree2(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.016180327868852*8        # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      draw_tree5(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+theta2), color1, depth+1)
      draw_tree5(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+thetaj), color2, depth+1)

def draw_tree6(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi)
   delta_y = trunk * math.sin((heading*(math.pi)).real)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      draw_tree6(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading+theta2), color1, depth+1)
      draw_tree6(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color2, depth+1)
def draw_tree7(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi/2)
   delta_y = trunk * math.sin((heading).real)*(math.pi/2)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
      pygame.draw.line(main_surface, color, posn, newpos, order)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (clol, clol, clol2)
      color2 = (clol2, clol, clol)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree9(rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color1, depth+1)
      draw_tree9(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+theta2), color2, depth+1)

def draw_tree10(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos((heading*1j).imag)*(math.pi/2)
   delta_y = trunk * math.sin((heading).real)*(math.pi/2)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = 0,0,0,#
      color2 = (clol2, clol2, clol)#(0, clol2, clol/2)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree10(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2, newpos, (heading+thetaj), color1, depth+1)
      draw_tree10(rendord,inord, order-1, thetab, theta, newsz, clol, clol2+gradd, newpos, (heading+theta2), color2, depth+1)
def draw_tree11(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.016180327868852*8        # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
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
   trunk_ratio = 0.016180327868852*8        # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   if order<rendord:
      pygame.draw.line(main_surface, color, posn, newpos, order)
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

def draw_treex(ratio, rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_treex(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_treex(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)

def draw_tree2x(ratio, rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 2, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree2x(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_tree2x(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)
def draw_tree11x(ratio, rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j
   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree11x(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree11x(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)

def draw_tree12x(ratio,rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree12x(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree12x(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)
def draw_treexx(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_treexx(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_treexx(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)

def draw_tree2xx(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 2, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree2xx(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_tree2xx(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)
def draw_tree11xx(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree11xx(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree11xx(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)

def draw_tree12xx(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree12xx(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree12xx(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)
def draw_treey(ratio, rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * -math.cos(((heading*1j)).imag)
   delta_y = trunk * -math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_treey(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_treey(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)

def draw_tree2y(ratio, rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * -math.cos(((heading*1j)).imag)
   delta_y = trunk * -math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 2, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree2y(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_tree2y(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)
def draw_tree11y(ratio, rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * -math.cos(((heading*1j)).imag)
   delta_y = trunk * -math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j
   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree11y(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree11y(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)

def draw_tree12y(ratio,rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = ratio     # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * -math.cos(((heading*1j)).imag)
   delta_y = trunk * -math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree12y(ratio, rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree12y(ratio, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)
def draw_treexy(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(((heading*1j)).imag)
   delta_y = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_treexy(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_treexy(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)

def draw_tree2xy(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(((heading*1j)).imag)
   delta_y = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), 2, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree2xy(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading+thetaj), color1, depth+1)
      draw_tree2xy(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading+theta2), color2, depth+1)
def draw_tree11xy(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(((heading*1j)).imag)
   delta_y = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree11xy(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree11xy(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)

def draw_tree12xy(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(((heading*1j)).imag)
   delta_y = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = ((127+(127*math.sin(((heading*1j)).real*(math.pi)))))
   gradd2 = ((127+(127*math.cos(((heading*1j)).real))))
   gradd3 = ((127+(127*math.cos(((heading*1j)).imag))))
   if order<rendord:
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*10), int((1+((-math.sin(((heading*1j)).imag*(math.pi)))))*2))
   #pygame.draw.line(main_surface, color, [640,360], newpos, 1)
   #pygame.draw.polygon(main_surface, color, [[int(posn[0]),int(posn[1])],[int(newpos[0]),int(newpos[1])], [pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]]], 0)
   thetaj = theta + 9.87j
   theta2 = theta + 6.1j

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors  # at other depths, or when depth is even, or odd, etc.
   
      color1 = (gradd, gradd2, gradd3)
      color2 = (gradd, gradd2, gradd3)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree12xy(rendord,inord, order-1, theta, thetab, newsz, clol+gradd, clol2+gradd2, newpos, (heading-thetaj), color1, depth+1)
      draw_tree12xy(rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2+gradd2, newpos, (heading-theta2), color2, depth+1)
#@lru_cache(maxsize = None)
def gameloop():
    rendord = 1
    theta1 =  (9.87+9.87j)*234
    theta2 =  (6.10-6.10j)*234
    theta12 = -(9.87-9.87j)*234
    theta22 = -(6.10+6.10j)*234
    theta1ad  =  (0.00987+0.00987j)*234
    theta2ad  =  (0.00610-0.00610j)*234
    theta12ad =  (0.00987-0.00987j)*234
    theta22ad =  (0.00610+0.00610j)*234    
    clol = 0
    clol2 = 0
    ft = 0
    inord = 16
    ratio = 1.6180327868852
    screen_size = (500,500)
    save_screen = make_video(main_surface)
    video = True
    while True:

        #theta1 += 0.015
        #theta2 += 0.02
        theta1 -=  (0.000987+0.000987j)*5
        theta2 +=  (0.000610-0.000610j)*5
        theta12 += (0.000987-0.000987j)*5
        theta22 -= (0.000610+0.000610j)*5
        
        #theta1 -=  (0.00987+0.00987j)
        #theta12 += (0.00987-0.00987j)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_f:
               theta1 +=  (0.00987+0.00987j)
               theta2 +=  (0.00610-0.00610j)
               theta12 -= (0.00987-0.00987j)
               theta22 -= (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_g:
               theta1 -=  (0.00987+0.00987j)
               theta2 -=  (0.00610-0.00610j)
               theta12 += (0.00987-0.00987j)
               theta22 += (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_b:
            if rendord<15:
               rendord+=1 
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_v:
            if rendord>1:
               rendord-=1 
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_n:
            if inord<20:
               inord+=1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_m:
            if inord>1:
               inord-=1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_PERIOD:
               theta1 =  0
               theta2 =  0
               theta12 = 0
               theta22 = 0
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F1:
            theta1 -=  (0.00987+0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F2:
            theta2 -=  (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F3:
            theta12 += (0.00987-0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F4:
            theta22 += (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F5:
            theta1 -=  (0.00987+0.00987j)
            theta2 -=  (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F6:
            theta12 += (0.00987-0.00987j)
            theta22 += (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F7:
            theta1 -=  (0.00987+0.00987j)
            theta12 += (0.00987-0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F8:
            theta2 -=  (0.00610-0.00610j)
            theta22 += (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F9:
            theta1 -=  (0.00987+0.00987j)
            theta22 += (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F10:
            theta2 -=  (0.00610-0.00610j)
            theta12 += (0.00987-0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F11:
            theta22 += (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_F12:
            theta1 -=  (0.00987+0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_1:
            theta1 +=  (0.00987+0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_2:
            theta2 +=  (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_3:
            theta12 -= (0.00987-0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_4:
            theta22 -= (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_5:
            theta1 +=  (0.00987+0.00987j)
            theta2 +=  (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_6:
            theta12 -= (0.00987-0.00987j)
            theta22 -= (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_7:
            theta1 +=  (0.00987+0.00987j)
            theta12 -= (0.00987-0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_8:
            theta2 +=  (0.00610-0.00610j)
            theta22 -= (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_9:
            theta1 +=  (0.00987+0.00987j)
            theta22 -= (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_KP_MINUS:
            theta2 +=  (0.00610-0.00610j)
            theta12 -= (0.00987-0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_KP_EQUALS:
            theta22 -= (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_BACKSPACE:
            theta1 +=  (0.00987+0.00987j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_RIGHTBRACKET:
            theta1 += (1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_LEFTBRACKET:
            theta1 -= (1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_p:
            theta1 += (0.1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_o:
            theta1 -= (0.1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_i:
            theta2 += (1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_u:
            theta2 -= (1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_y:
            theta2 += (0.1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_t:
            theta2 -= (0.1*(0.00987+0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_x:
            pygame.key.set_repeat(1,10)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_l:
            theta12 += (1*(0.00987-0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_k:
            theta12 -= (1*(0.00987-0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_j:
            theta12 += (0.1*(0.00987-0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_h:
            theta12 -= (0.1*(0.00987-0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_g:
            theta22 += (1*(0.00987-0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_f:
            theta22 -= (1*(0.00987-0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_d:
            theta22 += (0.1*(0.00987-0.00987j))
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_s:
            theta22 -= (0.1*(0.00987-0.00987j))
        main_surface.fill((0, 0, 0))
        #draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
        #draw_tree(13, theta1, theta2, surface_size*0.9, clol, clol2, pygame.mouse.get_pos(), -math.pi/2)

        #draw_tree5(rendord, inord, inord, theta1, theta2, surface_size*0.25, clol, clol2,screen_size , math.pi/2)
        #draw_tree6(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        #draw_tree7(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        #draw_tree8(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        #draw_tree9(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        #draw_tree10(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        #draw_tree3(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        #draw_tree4(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        #draw_tree(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        #draw_treez(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        #draw_tree11(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        #draw_tree12(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_treex(ratio,rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, +math.pi/2)
        draw_tree2x(ratio,rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size,+math.pi/2)
        draw_tree11x(ratio,rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree12x(ratio, rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_treexx(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree2xx(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree11xx(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_tree12xx(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_treey(ratio,rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, +math.pi/2)
        draw_tree2y(ratio,rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size,+math.pi/2)
        draw_tree11y(ratio,rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree12y(ratio, rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_treexy(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree2xy(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree11xy(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        draw_tree12xy(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        
        if video:
           if ft<1:
              ft+=1
              pygame.display.flip()
              next(save_screen)
           else:
              video = not video
              break
        else:
              pygame.display.update()
              #break
        my_clock.tick(60)


gameloop()
pygame.quit()
