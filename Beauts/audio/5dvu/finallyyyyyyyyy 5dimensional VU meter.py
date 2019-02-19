import pygame
import math
import pyaudio
import numpy
import time
import wave
import scipy.fftpack
#from functools import lru_cache

from video import make_video
pygame.init()   

surface_size = 1000
main_surface = pygame.display.set_mode((1600,900),pygame.DOUBLEBUF+pygame.FULLSCREEN)
my_clock = pygame.time.Clock()

#lru_cache(maxsize=None)
def draw_tree(inord, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = (1 + 5 ** 0.5) / 2       
   trunk = sz * trunk_ratio
   delta_y = trunk * math.sin((heading*400/400).real)
   delta_x = trunk * math.cos((heading*400/400).real)

   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   #if order<2:
   if order==1:
   #if True:
      #pygame.draw.line(main_surface, color, posn, newpos, order)
      #pygame.draw.line(main_surface, color, newpos, posn, order)
      pygame.draw.circle(main_surface, color, (int(posn[0]),int(posn[1])),1,1)#int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),1,1)#int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(newpos[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(posn[1])),1,1)
   
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*(math.cos((heading*1j).imag)))
   gradd2 = 128+(127*(math.sin((heading).real)))
   gradd3 = 128+(128*math.sin((heading*1j).imag))
   gradd4 = 128+(128*math.cos((heading).real))
   gradd5 = 128+(128*math.sin((heading).real))
   gradd6 = 128+(128*math.sin((heading).real))
   

   if order > 0:
      if depth == 0:
          color1 = (gradd,0,gradd3)
          color2 = (gradd,0,gradd3)
      if depth == 0:
          color1 = (gradd,0,gradd3)
          color2 = (gradd,0,gradd3)
      else:
          color1 = (gradd,gradd2,gradd3)
          color2 = (gradd,gradd2,gradd3)

      #pygame.display.flip()
      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      #pygame.display.flip()
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading+theta+12j), color1, depth)
      draw_tree(inord, order-1, theta, thetab, newsz, newpos, (heading+thetab+12j), color2, depth)
      
#@lru_cache(maxsize=None)
def draw_tree2(inord, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = (1 + 5 ** 0.5) / 2       
   trunk = sz * trunk_ratio
   delta_y = trunk * -math.cos((heading*400/400).real)
   delta_x = trunk * -math.sin((heading*400/400).real)

   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   #if order<2:
   #if order==1:
   if True:
      #pygame.draw.line(main_surface, color, posn, newpos, order)
      #pygame.draw.line(main_surface, color, newpos, posn, order)
      pygame.draw.circle(main_surface, color, (int(posn[0]),int(posn[1])),int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(newpos[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(posn[1])),1,1)
      
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*math.cos((heading*1j).imag))
   gradd2 = 128+(127*math.sin((heading*1).imag))
   gradd3 = 128+(128*math.sin((heading).real))
   

   if order > 0:
      if depth == 0:
          color1 = (gradd,255,gradd2)
          color2 = (gradd,0,gradd2)
      else:
          color1 = (gradd,255,gradd2)
          color2 = (gradd,0,gradd2)#(gradd,gradd2,0)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      #pygame.display.flip()
      draw_tree2(inord, order-1, theta, thetab, newsz, newpos, (heading+theta+12j), color1, depth)
      draw_tree2(inord, order-1, theta, thetab, newsz, newpos, (heading+thetab+12j), color2, depth)

def draw_tree3(inord, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = (1 + 5 ** 0.5) / 2       
   trunk = sz * trunk_ratio
   delta_x = trunk * -math.cos((heading*400/400).real)
   delta_y = trunk * -math.sin((heading*400/400).real)

   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   #if order<2:
   #if order==1:
   if True:
      #pygame.draw.line(main_surface, color, posn, newpos, order)
      #pygame.draw.line(main_surface, color, newpos, posn, order)
      pygame.draw.circle(main_surface, color, (int(posn[0]),int(posn[1])),int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(newpos[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(posn[1])),1,1)
      
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*math.cos((heading*1).imag))
   gradd2 = 128+(127*math.sin((heading*1j*1).real))
   gradd3 = 128+(128*math.sin((heading).real))
   

   if order > 0:
      if depth == 0:
          color1 = (255,gradd2,gradd)
          color2 = (0,gradd2,gradd)
      else:
          color1 = (gradd2,255,gradd)
          color2 = (gradd2,0,gradd)#(gradd,gradd2,0)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      #pygame.display.flip()
      draw_tree3(inord, order-1, theta, thetab, newsz, newpos, (heading+theta+12j), color1, depth)
      draw_tree3(inord, order-1, theta, thetab, newsz, newpos, (heading+thetab+12j), color2, depth)

def draw_tree4(inord, order, theta, thetab, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = (1 + 5 ** 0.5) / 2       
   trunk = sz * trunk_ratio
   delta_x = trunk * math.cos((heading*400/400).real)
   delta_y = trunk * math.sin((heading*400/400).real)

   thetaj = theta*1j*1j
   thetai = thetab*1j*1j
   
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   #if order<2:
   #if order==1:
   if True:
      #pygame.draw.line(main_surface, color, posn, newpos, order)
      #pygame.draw.line(main_surface, color, newpos, posn, order)
      pygame.draw.circle(main_surface, color, (int(posn[0]),int(posn[1])),int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      pygame.draw.circle(main_surface, color, (int(newpos[0]),int(newpos[1])),int(1*math.fabs(math.sin((heading*400/400).real))),int(1*math.fabs(math.sin((heading*400/400).real))))
      #pygame.draw.circle(main_surface, color, (int(posn[0]),int(newpos[1])),1,1)
      #pygame.draw.circle(main_surface, color, (int(newpos[0]),int(posn[1])),1,1)
      
   #gradd  = 128+(127*math.cos((math.exp(heading.imag)).imag))
   gradd  = 128+(127*math.cos((heading*1).imag))
   gradd2 = 128+(127*math.sin((heading*1j*1).real))
   gradd3 = 128+(128*math.sin((heading).real))
   

   if order > 0:
      if depth == 0:
          color1 = (255,gradd,gradd2)
          color2 = (0,gradd2,gradd2)
      else:
          color1 = (gradd2,255,gradd)
          color2 = (gradd2,0,gradd)#(gradd,gradd2,0)


      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      #pygame.display.flip()
      draw_tree4(inord, order-1, theta, thetab, newsz, newpos, (heading+theta+12j), color1, depth)
      draw_tree4(inord, order-1, theta, thetab, newsz, newpos, (heading+thetab+12j), color2, depth)
#@lru_cache(maxsize=None)
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
    
    wf = wave.open('long.wav', 'rb')
    timer = wave.open('fishy.wav', 'rb')
    song = wave.open('fish.wav', 'rb')
    song2 = wave.open('sim.wav', 'rb')
    p = pyaudio.PyAudio()

    main_surface.fill((0, 0, 0))
    
   
    def callback(in_data, frame_count, time_info, status):
       pygame.display.flip()
       my_clock.tick(24)
       #next(save_screen)
       data = wf.readframes(frame_count)
       data2 = timer.readframes(frame_count)
       data3 = song.readframes(frame_count)
       data4 = song2.readframes(frame_count)
       
       decoded = numpy.fromstring(data, dtype=numpy.int32)
       decoded2 = numpy.fromstring(data2, dtype=numpy.int32)
       decoded3 = numpy.fromstring(data3, dtype=numpy.int32)
       decoded4 = numpy.fromstring(data4, dtype=numpy.int32)
       #yf = scipy.fftpack.fft(decoded)
       #print(yf)
       #here = numpy.fft(
       #theta1 = 5+(math.log10((1/math.fabs(0.00001+decoded[0])))*1j)
       #theta2 = 5+(math.log10((1/math.fabs(0.00001+decoded[1])))*1j)

       #theta1 = (math.exp(math.sin(decoded[0])))*1j
       #theta2 = (math.exp(math.sin(decoded[1])))*1j
       
       decoded_oh = decoded[::]
       #yf_oh = yf[::]

       #decoded_ohh = yf_oh*decoded_oh
       
       #theta1 = decoded[0]
       #theta2 = decoded[1]
       #print(decoded[0])
       if math.fabs(decoded[0]) > 0:
           if math.fabs(decoded[1]) > 0:
               #print(decoded[0])
               for i,x,j,l in zip(decoded_oh,decoded2,decoded3,decoded4):
                  #theta1 = math.cos((math.exp(((i)/32767)*1)))*1j
                  #theta2 = math.cos((math.exp(((i)/32767)*1)))*1j

                  #theta1 = math.cos((pygame.mouse.get_pos()[1]/225)*math.pi*(i/2147483647))*1j
                  #theta2 = math.sin((pygame.mouse.get_pos()[1]/225)*math.pi*(i/2147483647))*1
                  
                  theta1 = (2*math.pi*(i/2147483647))#**math.cos(math.pi*((i/2147483647)))#*((x/2147483647))#*(1*(pygame.mouse.get_pos()[0]/450))
                  theta2 = math.cos(2*math.pi*(math.exp((l/50)/2147483647)))+math.sin(-2*math.pi*(math.exp((l/50)/2147483647)))#**math.cos(2*math.pi*((j/2147483647)))#*(1*(pygame.mouse.get_pos()[1]/450))
                  #theta1 = ((math.exp(((i)/6000)*1 )))*1j
                  #theta2 = ((math.exp(((i)/6000)*1)))*1j
            
                  #theta1 = math.cos((math.exp((math.fabs(i)/6000)*1 )))*1j
                  #theta2 = math.cos((math.exp((math.fabs(i)/6000)*1)))*1j
                  draw_tree(inord,3, theta1, theta2, surface_size*0.3*(i/2147483647), (800,450), (i/2147483647)*math.pi*(math.exp((l/50)/2147483647)))
                  #draw_tree2(inord,8, theta1, theta2, surface_size*0.2, (450,450), (math.pi*(i/2147483647)))
                  #draw_tree3(inord,8, theta1, theta2, surface_size*0.2, (450,450), (math.pi*(i/2147483647)))
                  #draw_tree4(inord,8, theta1, theta2, surface_size*0.2, (450,450), (math.pi*(i/2147483647)))
                  
                  #draw_tree2(inord,8, theta1, theta2, surface_size*0.2, (450,450), (pygame.mouse.get_pos()[0]/225)*math.pi*(i/2147483647))
                  #draw_tree3(inord,8, theta1, theta2, surface_size*0.2, (450,450), (pygame.mouse.get_pos()[0]/225)*math.pi*(i/2147483647))
                  #draw_tree4(inord,8, theta1, theta2, surface_size*0.2, (450,450), (pygame.mouse.get_pos()[0]/225)*math.pi*(i/2147483647))
       #pygame.display.flip()
             #draw_tree(inord, 8, theta1, theta2, surface_size*0.8, (400,400), math.pi)
             #pass
       
       
       #print(decoded)
       return (data, pyaudio.paContinue)
    #print(wf.getsampwidth())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=96000,
                output=True,
                stream_callback=callback)
    stream.start_stream()
    while True:
        
        
        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_s:
           next(save_screen)

        # Updates - change the angle
        #theta1 += 0.002
        #theta2 -= 0.002
        
            
        # Draw everything
        #main_surface.fill((0, 0, 0))
        #draw_tree(8, theta1, theta2, surface_size, (45

gameloop()
pygame.quit()
