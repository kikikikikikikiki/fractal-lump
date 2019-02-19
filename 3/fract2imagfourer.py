from video import make_video import pygame import  math pygame.init()  #
prepare the pygame module for use

# Create a new surface and window.
surface_size = 1920
main_surface = pygame.display.set_mode((1920,1080),pygame.HWSURFACE+pygame.DOUBLEBUF)
my_clock = pygame.time.Clock()

#@lru_cache(maxsize = None)
def draw_tree(deapth, rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.116180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
   delta_y2 = (math.cos(((newpos[1])).imag)+(math.cos(((newpos[1])).imag))/2)
   delta_x2 = (math.sin(((newpos[0])).real*(math.pi))+math.sin(((newpos[0])).real*(math.pi))/2)
   newpos2 = [u + delta_x2, v + delta_y2]
   diffpos_x2 = newpos2[0]-posn[0]
   diffpos_y2 = newpos2[1]-posn[1]
   length2   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre2 = (newpos[0]+diffpos_x2/2, newpos[1]+diffpos_y2/2)
   vortexnum = str(deapth)
   vortexlist = list(vortexnum)
   vortexlistlen = len(vortexlist)
   num0 = 0
   num1 = 0
   num2 = 0
   num3 = 0
   num4 = 0
   num5 = 0
   num6 = 0
   num7 = 0
   num01 = 0
   num12 = 0
   num23 = 0
   num34 = 0
   num45 = 0
   num56 = 0
   num67 = 0
   num78 = 0
   combination = 0
   combinationing = 0
   combination2 = 0
   for i in vortexlist:
      x = 0
      while x<vortexlistlen:
         if x ==0:
            num0 = int(i)
         if x ==1:
            num1 = int(i)
         if x ==2:
            num2 = int(i)
         if x ==3:
            num3 = int(i)
         if x ==4:
            num4 = int(i)
         if x ==5:
            num5 = int(i)
         if x ==6:
            num6 = int(i)
         if x ==7:
            num7 = int(i)
         x+=1
      combination = (num0+num1+num2+num3+num4+num5+num6+num7)
      combination = str(combination)
      combination2 = list(combination)
      combination2len = len(combination2)
      if len(list(combination))>1:
         for lll in list(combination):
               z = 0
               while x<combination2len:
                  if x ==0:
                     num01 = int(lll)
                  if x ==1:
                     num12 = int(lll)
                  if x ==2:
                     num23 = int(lll)
                  if x ==3:
                     num34 = int(lll)
                  if x ==4:
                     num45 = int(lll)
                  if x ==5:
                     num56 = int(lll)
                  if x ==6:
                     num67 = int(lll)
                  if x ==7:
                     num78 = int(lll)
                  z+=1
               combinationing = (num0+num1+num2+num3+num4+num5+num6+num7)
               #print(combinationing)

    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
      pygame.draw.line(main_surface, (255,0,0), posn, newpos, order)
   if order == 2:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
      pygame.draw.line(main_surface, (0,255,0), posn, newpos, order)

   
      
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
      color1 = (combinationing*5, clol2, clol2)
      color2 = (clol2, clol2, combinationing*5)
            # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(deapth, rendord,inord, order-1, theta, thetab, newsz, clol, clol2+gradd, newpos, (heading+thetaj), color1, depth+1)
      draw_tree(deapth, rendord,inord, order-1, thetab, theta, newsz, clol+gradd, clol2, newpos, (heading+theta2), color2, depth+1)

def draw_tree2(rendord,inord, order, theta, thetab, sz, clol, clol2, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
   trunk_ratio = 0.16180327868852      # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_y = trunk * math.cos(((heading*1j)).imag)
   delta_x = trunk * math.sin(((heading*1j)).real*(math.pi))
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   gradd = (256/inord)
   diffpos_x = newpos[0]-posn[0]
   diffpos_y = newpos[1]-posn[1]
   length   = math.sqrt(diffpos_x**2 + diffpos_y**2)/2
   circcentre = (posn[0]+diffpos_x/2, posn[1]+diffpos_y/2)
    
   if order == 1:
      pygame.draw.circle(main_surface, color, (int(circcentre[0]),int(circcentre[1])), int(length),int(length))
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
#@lru_cache(maxsize = None)
def gameloop():
    rendord = 2
    theta1 =  (0.00987+0.00987j)*1111
    theta2 =  (0.00610+0.00610j)*1111
    theta12 = (0.00987-0.00987j)*1111
    theta22 = (0.00610-0.00610j)*1111
    clol = 0
    clol2 = 0
    ft = 0
    inord = 3
    deapth = 0
    screen_size = (960, 540)
    save_screen = make_video(main_surface)
    video = False
    while True:

        #theta1 += 0.015
        #theta2 += 0.02
        theta1 +=  (0.00987+0.00987j)
        theta2 +=  (0.00610+0.00610j)
        theta12 -= (0.00987-0.00987j)
        theta22 -= (0.00610-0.00610j)
        deapth += 1
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_b:
            if rendord<15:
               rendord+=1 
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_v:
            if rendord>2:
               rendord-=1 
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_n:
            if inord<20:
               inord+=1
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_m:
            if inord>1:
               inord-=1 
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_1:
            theta1 +=  (0.00987+0.00987j)
            theta2 +=  (0.00610+0.00610j)
            theta12 -= (0.00987-0.00987j)
            theta22 -= (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_2:
            theta1 -=  (0.00987+0.00987j)
            theta2 -=  (0.00610+0.00610j)
            theta12 += (0.00987-0.00987j)
            theta22 += (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_3:
            theta1 -=  (0.00987+0.00987j)
            theta2 -=  (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_4:
            theta1 += (0.00987-0.00987j)
            theta2 += (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_5:
            theta12 -=  (0.00987+0.00987j)
            theta22 -=  (0.00610+0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_6:
            theta12 += (0.00987-0.00987j)
            theta22 += (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_6:
            theta12 += (0.00987-0.00987j)
            theta1 += (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_7:
            theta12 -= (0.00987-0.00987j)
            theta1 -= (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_8:
            theta12 += (0.00987-0.00987j)
            theta2 += (0.00610-0.00610j)
        elif ev.type == pygame.KEYDOWN  and ev.key == pygame.K_9:
            theta12 -= (0.00987-0.00987j)
            theta2 -= (0.00610-0.00610j)
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
        main_surface.fill((20, 20, 20))
##        draw_tree(14, theta1, theta2, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)pygame.mouse.get_pos()
##        draw_tree(13, theta1, theta2, surface_size*0.9, clol, clol2, pygame.mouse.get_pos(), -math.pi/2)
##
##        draw_tree5(rendord, inord, inord, theta1, theta2, surface_size*0.25, clol, clol2,screen_size , math.pi/2)
##        draw_tree6(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
##        draw_tree7(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
##        draw_tree8(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
##        draw_tree9(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
##        draw_tree10(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
##        draw_tree3(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
##        draw_tree4(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree(deapth, rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
        draw_tree2(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, -math.pi/2)
##        draw_tree11(rendord,inord, inord, theta1, theta2, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
##        draw_tree12(rendord,inord,inord, theta12, theta22, surface_size*0.25, clol, clol2, screen_size, math.pi/2)
        
        if video:
           if ft<1:
              ft+=1
              pygame.display.flip()
              next(save_screen)
           else:
              video = not video
              break
        else:
              pygame.display.flip()
              
        my_clock.tick(24)


gameloop()
pygame.quit()
