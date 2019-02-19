import pygame
import math
import pyaudio
import numpy
import time
pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((800,800))
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.1618       
   trunk = sz * trunk_ratio
   delta_x = trunk * math.cos((heading).imag)
   delta_y = trunk * math.sin((heading*1j).real)

   thetaj = theta+1j
   thetai = theta+1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, order)
   gradd  = 128+(127*math.cos((heading).imag))
   gradd2 = 128+(128*math.sin((heading*1j).real))
   

   if order > 0:
      if depth == 0:
          color1 = (gradd,gradd2,255)
          color2 = (gradd,gradd2,255)
      else:
          color1 = (gradd,gradd2,255)
          color2 = (gradd,gradd2,255)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading+theta, color1, depth+1)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading-thetab, color2, depth+1)

    
def gameloop():
    theta1 = 0
    theta2 = 0
    frame = 0

    WIDTH = 4
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()
    
    def callback(in_data, frame_count, time_info, status):
       decoded = numpy.fromstring(in_data, dtype=numpy.float32)
       theta1 = 5+(math.fabs(decoded[0])*1j)
       theta2 = 5+(math.fabs(decoded[1])*1j)
       main_surface.fill((0, 0, 0))
       draw_tree(12, theta1, theta2, surface_size*0.5, (400,400), math.pi)
       
       pygame.display.flip()
       my_clock.tick(60)
       #print(decoded)
       return (in_data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
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
