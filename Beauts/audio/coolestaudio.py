import pygame
import math
import pyaudio
import numpy
import time
pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((200,200))
my_clock = pygame.time.Clock()


def draw_tree(inord, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.01618       
   trunk = sz * trunk_ratio
   delta_x = trunk * math.cos((heading*pygame.mouse.get_pos()[0]/400).imag)
   delta_y = trunk * math.sin((heading*1j*pygame.mouse.get_pos()[1]/400).real)

   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   #if order<2:
   if True:
      #pygame.draw.line(main_surface, color, posn, newpos, order)
      #pygame.draw.line(main_surface, color, newpos, posn, order)
      pygame.draw.circle(main_surface, color, (int(posn[0]),int(posn[1])),1,1)
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),1,1)
      pygame.draw.circle(main_surface, color, (int(posn[0]),int(newpos[1])),1,1)
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(posn[1])),1,1)
      
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*math.cos((heading).imag))
   gradd2 = 128+(128*math.sin((heading*1j).real))
   gradd3 = 128+(128*math.sin((heading).real))
   

   if order > 0:
      if depth == 0:
          color1 = (0,gradd,gradd2)
          color2 = (255,gradd,gradd2)
      else:
          color1 = (0,gradd,gradd2)
          color2 = (0,gradd,gradd2)#(gradd,gradd2,0)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading+theta+12j), color1, depth)
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading+thetab-12j), color2, depth)
    
def gameloop():
    theta1 = 0
    theta2 = 0
    frame = 0
    inord = 0
   
    WIDTH = 4
    CHANNELS = 1
    RATE = 22050
    p = pyaudio.PyAudio()
    
    
    def callback(in_data, frame_count, time_info, status):
       pygame.display.flip()
       my_clock.tick(60)
       decoded = numpy.fromstring(in_data, dtype=numpy.float32)
       #here = numpy.fft(
       #theta1 = 5+(math.log10((1/math.fabs(0.00001+decoded[0])))*1j)
       #theta2 = 5+(math.log10((1/math.fabs(0.00001+decoded[1])))*1j)

       #theta1 = (math.exp(math.sin(decoded[0])))*1j
       #theta2 = (math.exp(math.sin(decoded[1])))*1j

       theta1 = math.sin((math.exp(decoded[0])))*1j
       theta2 = math.sin((math.exp(decoded[1])))*1j
       
       #theta1 = (math.exp(decoded[0]))*1j
       #theta2 = (math.exp(decoded[1]))*1j
       
       main_surface.fill((0, 0, 0))
       draw_tree(inord, 12, theta1, theta2, surface_size*0.4, (100,100), math.pi)
       #pygame.display.flip()
       if math.fabs(decoded[0])>4e-05:
          if math.fabs(decoded[1])>4e-05:
             #draw_tree(inord, 8, theta1, theta2, surface_size*0.8, (400,400), math.pi)
             pass
       
       
       #print(decoded)
       return (in_data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)
    while True:
        
        
        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        #theta1 += 0.002
        #theta2 -= 0.002
        
            
        # Draw everything
        #main_surface.fill((0, 0, 0))
        #draw_tree(8, theta1, theta2, surface_size, (45

gameloop()
pygame.quit()
