import pygame
import math
import pyaudio
import numpy
import time
pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((1600,900),pygame.FULLSCREEN)
my_clock = pygame.time.Clock()


def draw_tree(order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.1618       
   trunk = sz * trunk_ratio
   delta_x = trunk * math.sin((heading*1j).real)
   delta_y = trunk * math.cos((heading*1j).real)

   thetaj = theta+1j
   thetaj += 10
   thetai = theta+1j
   thetai += 10
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos, order)
   gradd = 128+(128*math.sin((heading*1j).real))
   gradd2 = 128+(128*math.cos((heading*1j).imag))
   

   if order > 0:
      if depth == 0:
          color1 = (gradd,gradd2,255)
          color2 = (gradd,gradd2,255)
      else:
          color1 = (gradd,gradd2,255)
          color2 = (gradd,gradd2,255)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading+thetaj, color1, depth+1)
      draw_tree(order-1, theta, thetab, newsz, newpos, heading-thetai, color2, depth+1)

    
def gameloop():
    theta1 = 0
    theta2 = 0
    frame = 0

    WIDTH = 4
    CHANNELS = 2
    RATE = 44100
    p = pyaudio.PyAudio()
    
    def callback(in_data, frame_count, time_info, status):
       wf = open("wavtestfile.wav", 'rb')
       decoded = numpy.fromstring(in_data, dtype=numpy.float32)
       theta1 = math.sin(decoded[0])
       theta2 = math.sin(decoded[0])
       theta1 += 10+1j
       theta2 += 10+1j
       main_surface.fill((0, 0, 0))
       draw_tree(12, theta1, theta2, surface_size, (800,450), math.pi)
       pygame.display.flip()
       my_clock.tick(60)
       #print(decoded[1])
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
