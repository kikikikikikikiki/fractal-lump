import pygame
import math
import pyaudio
import numpy
import time
pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((900,900),pygame.FULLSCREEN)
my_clock = pygame.time.Clock()


def draw_tree(inord, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 1.618       
   trunk = sz * trunk_ratio
   delta_x = trunk * math.sin((heading).real)
   delta_y = trunk * math.cos((heading).real)

   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   #if order<2:
   if True:
      #pygame.draw.line(main_surface, color, posn, newpos, order)
      #pygame.draw.line(main_surface, color, newpos, posn, order)
      pygame.draw.polygon(main_surface, color,((posn[0],newpos[0]),(posn[0],newpos[1]),(posn[1],newpos[1]),(posn[1],newpos[0])),1)
      
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*math.sin((heading).imag))
   gradd2 = 128+(127*math.cos((heading).real))
   gradd3 = 128+(128*math.sin((heading).real))
   

   if order > 0:
      if depth == 0:
          color1 = (gradd,gradd2,0)
          color2 = (gradd,gradd2,255)
      else:
          color1 = (gradd,gradd2,0)
          color2 = (gradd,gradd2,255)#(gradd,gradd2,0)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading+theta), color1, depth)
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading-thetab), color2, depth)
    
def gameloop():
    theta1 = 0
    theta2 = 0
    frame = 0
    inord = 0
   
    WIDTH = 4
    CHANNELS = 2
    RATE = 22050
    p = pyaudio.PyAudio()
    print(p.get_default_output_device_info())
    
    def callback(in_data, frame_count, time_info, status):
       pygame.display.flip()
       #my_clock.tick(60)
       decoded = numpy.fromstring(in_data, dtype=numpy.float32)
       #theta1 = 5+(math.log10((1/math.fabs(0.00001+decoded[0])))*1j)
       #theta2 = 5+(math.log10((1/math.fabs(0.00001+decoded[1])))*1j)

       #theta1 = (math.exp(math.sin(decoded[0])))
       #theta2 = (math.exp(math.sin(decoded[1])))

       theta1 = math.cos((math.exp(decoded[0])))
       theta2 = math.cos((math.exp(decoded[1])))
       
       #theta1 = (math.exp(decoded[0]))
       #theta2 = (math.exp(decoded[1]))
       
       main_surface.fill((0, 0, 0))
       draw_tree(inord, 16, theta1, theta2, (pygame.mouse.get_pos()[0]/1)*(pygame.mouse.get_pos()[1]/1), (450,900), math.pi)
       #draw_tree(inord, 6, theta1, theta2, (50)*(100), (1000,2000), math.pi)
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
