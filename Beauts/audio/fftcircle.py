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
main_surface = pygame.display.set_mode((600,600),pygame.FULLSCREEN+pygame.DOUBLEBUF)
my_clock = pygame.time.Clock()


def draw_tree(inord, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.01618       
   trunk = sz * trunk_ratio
   delta_x = trunk * math.cos((heading*400/400).imag)
   delta_y = trunk * math.sin((heading*1j*400/400).real)

   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   if order==1:
   #if True:
      #pygame.draw.line(main_surface, color, posn, newpos, order)
      #pygame.draw.line(main_surface, color, newpos, posn, order)
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(posn[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),1,1)
      pygame.draw.polygon(main_surface, color,((posn[0],posn[1]),(newpos[0],newpos[1]),(posn[1],posn[0]),(newpos[1],newpos[0])),1)
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(newpos[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(posn[1])),1,1)
      
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*math.cos((heading*1).imag))
   gradd2 = 128+(127*math.sin((heading*1j*1).real))
   gradd3 = 128+(128*math.sin((heading).real))
   

   if order > 0:
      if depth == 0:
          color1 = (gradd,0,gradd2)
          color2 = (gradd,0,gradd2)
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
    headingin = 0
   
    WIDTH = 4
    CHANNELS = 1
    RATE = 22050

    save_screen = make_video(main_surface)
    
    wf = wave.open('sim.wav', 'rb')
    p = pyaudio.PyAudio()
    
    
   
    def callback(in_data, frame_count, time_info, status):
       pygame.display.flip()
       #my_clock.tick(20)
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
       decoded_oh = decoded[::2]
       yf_oh = yf[::2]       
       
       
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

                  #theta1 = ((math.exp(((i)/6000)*1 )))*1j
                  #theta2 = ((math.exp(((i)/6000)*1)))*1j

                  #theta1 = math.cos((math.exp((math.fabs(i)/6000)*1 )))*1j
                  #theta2 = math.cos((math.exp((math.fabs(i)/6000)*1)))*1j
                  #pygame.display.flip()
                  draw_tree(inord, 8, theta1, theta2, surface_size*3, (300,300), j*math.pi)
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
