
# Importing the python libraries 
import pygame, math 
  
# Initialize all imported pygame modules 
pygame.init() 
  
# Create a new surface and window. 
surface_height, surface_width = 800, 600        #Surface variables 
main_surface = pygame.display.set_mode((surface_height,surface_width)) 
  
# Captioning the window 
pygame.display.set_caption("Fractal_Tree_geeksforgeeks") 
  
def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0): 
  
   # The relative ratio of the trunk to the whole tree   
   trunk_ratio = 0.29     
  
   # Length of the trunk   
   trunk = sz * trunk_ratio 
   delta_x = trunk * math.cos(heading) 
   delta_y = trunk * math.sin(heading) 
   (u, v) = posn 
   newpos = (u + delta_x, v + delta_y) 
   pygame.draw.line(main_surface, color, posn, newpos) 
  
   if order > 0:   # Draw another layer of subtrees 
  
      # These next six lines are a simple hack to make  
      # the two major halves of the recursion different  
      # colors. Fiddle here to change colors at other  
      # depths, or when depth is even, or odd, etc. 
      if depth == 0: 
          color1 = (255, 0, 0) 
          color2 = (0, 0, 255) 
      else: 
          color1 = color 
          color2 = color 
  
      # make the recursive calls to draw the two subtrees 
      newsz = sz*(1 - trunk_ratio) 
      draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1) 
      draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1) 
  
  
def main(): 
    theta = 0
  
    while True: 
  
        # Update the angle 
        theta += 0.01
  
        # This little part lets us draw the stuffs  
        # in the screen everything 
        main_surface.fill((255, 255, 0)) 
        draw_tree(9, theta, surface_height*0.9, (surface_width//2, surface_width-50), -math.pi/2) 
        pygame.display.flip() 
  
# Calling the main function 
main() 
pygame.quit() 
