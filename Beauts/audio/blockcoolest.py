import pygame
import math
import pyaudio
import numpy
import time
import wave
import scipy.fftpack

from video import make_video

pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((600,600))
my_clock = pygame.time.Clock()


def draw_tree(inord, order, theta, thetab, size, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.0001618 
      # A trunk ratio above ~0.1618 inverts the tree
   
   trunk = size * trunk_ratio
   
   delta_y = trunk * math.cos((heading*1j*400/400).imag)
   delta_x = trunk * math.sin((heading*1j*400/400).real)
   #Calculates the x and y coordinates
   
   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   if order == 1:
   #if order < 4:
   #if True:
      #pygame.draw.line(main_surface, color, posn, newpos, 1)
      pygame.draw.line(main_surface, color, newpos, posn, 1)
      #pygame.draw.polygon(main_surface, color,((posn[0],newpos[0]),(posn[0],newpos[1]),(posn[1],newpos[1]),(posn[1],newpos[0])),0)
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(posn[1])),4*int(math.exp(math.cos((heading*400/400).imag))),4*int(math.exp(math.cos((heading*400/400).imag))))
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),int(math.cos((heading*400/400).imag)),int(math.cos((heading*400/400).imag)))
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(newpos[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(posn[1])),1,1)
      
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*math.cos((heading*1j).imag))
   gradd2 = 128+(127*math.cos((heading*1j).real))
   gradd3 = 128+(128*math.sin((heading).real))

   graddgrade = ((16**((gradd/255)+1))-1)

   if order > 0:
      if depth == 0:
          #color1 = (0,graddgrade,0)
          #color2 = (graddgrade,0,graddgrade)

          color1 = (0,graddgrade,0)
          color2 = (0,0,0)
      #if heading > 1j: or something find slices of values in j
      else:
          color1 = (0,gradd,gradd2)
          color2 = (0,gradd,gradd2)#(gradd,gradd2,0)


      # make the recursive calls to draw the two subtrees
      newsz = size*(1 - trunk_ratio)
      #pygame.display.flip()
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading+theta+12j), color1, depth)
      #pygame.display.flip()
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading+thetab-12j), color2, depth)
    
def gameloop():
    theta1 = 0
    theta2 = 0
    frame = 0
    inord = 0
    headingin = 0
   
    WIDTH = 4
    CHANNELS = 1
    RATE = 22050

    save_screen = make_video(main_surface)
    
    wf = wave.open('vio.wav', 'rb')
    p = pyaudio.PyAudio()
    
    
   
    def callback(in_data, frame_count, time_info, status):
       pygame.display.flip()
       my_clock.tick(120)
       #next(save_screen)
       data = wf.readframes(frame_count)
       decoded = numpy.fromstring(data, dtype=numpy.int16)
       yf = scipy.fftpack.fft(decoded)
       #print(yf)
       #here = numpy.fft(
       #theta1 = 5+(math.log10((1/math.fabs(0.00001+decoded[0])))*1j)
       #theta2 = 5+(math.log10((1/math.fabs(0.00001+decoded[1])))*1j)

       #theta1 = (math.exp(math.sin(decoded[0])))*1j
       #theta2 = (math.exp(math.sin(decoded[1])))*1j
       decoded_oh = decoded[::]
       yf_oh = yf[::]       
       #print(len(decoded))
       
       #theta1 = decoded[0]
       #theta2 = decoded[1]
       #print(decoded[0])
       main_surface.fill((0, 0, 0))
       if math.fabs(decoded[0]) > 0:
           if math.fabs(decoded[1]) > 0:
               #print(decoded[0])
               for i, j in zip(decoded_oh, yf_oh): # Change to every other value for left/right side [0] = left [1] = right
                  theta1 = math.cos((math.exp(((i)/6000)*1 )))*1j
                  theta2 = math.cos((math.exp(((i)/6000)*1)))*1j

                  theta11 = math.sin((math.exp(((i)/6000)*1 )))*1j
                  theta22 = math.sin((math.exp(((i)/6000)*1)))*1j

                  #theta1 = ((math.exp(((i)/6000)*1 )))*1j
                  #theta2 = ((math.exp(((i)/6000)*1)))*1j

                  #theta1 = math.cos((math.exp((math.fabs(i)/6000)*1 )))*1j
                  #theta2 = math.cos((math.exp((math.fabs(i)/6000)*1)))*1j
                  #pygame.display.flip()
                  #draw_tree(inord, 2, theta1, theta2, surface_size*1500, (300,300), math.pi*j)
                  draw_tree(inord, 2, theta11, theta22, surface_size*800, (300,300), math.pi*j)
       #pygame.display.flip()
             #draw_tree(inord, 8, theta1, theta2, surface_size*0.8, (400,400), math.pi)
             #pass
       
       
       #print(decoded)
       return (data, pyaudio.paContinue)
    print(wf.getsampwidth())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
    stream.start_stream()
    #does the stream need to wait??
    #Is the callback loop time accurate?
    
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
