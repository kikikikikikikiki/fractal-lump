import pygame
import math as m
pygame.init()

main_surface = pygame.display.set_mode((1200, 800))
my_clock = pygame.time.Clock()

def draw_ball(itertat, color, vx, vy, gx, gy, veloy, velox, veloy2, velox2, siz):
    pygame.draw.circle(main_surface, color, [int(velox), int(veloy)], siz, 0)
    if itertat > 0:
        vy += gy*1j.real
        vx += gx*1j.imag
        
        veloy -= vy.imag**3
        velox -= vx.real**3
        velox2 = velox
        veloy2 = veloy
        
        color[0] +=1
        draw_ball(itertat-1, color, vx*1j, vy*1j, gx, gy, veloy2, velox2, veloy2, velox2, siz-1)
    else:
        color[0] = 0        

def gameloop():
    test = 0
    vely = 160
    velx = 160
    vely2 = vely
    velx2 = velx
    vy = 0
    vx = 0
    gy = 0.05 
    gx = 0.05
    itertat = 128
    siz = 128
    coloor = [0,0,0]
    while True:
        vy += gy
        vx += gx
        
        vely += vy
        velx += vx
        
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        main_surface.fill((100,100,100))
        if vely > 640:
            vely = 640
            vy = -(vy)
        if velx > 1040:
            velx = 1040
            vx = -(vx)
        draw_ball(itertat, coloor, vx, vy, gx, gy, vely, velx, vely2, velx2, siz)
        pygame.display.flip()
        my_clock.tick(60)

gameloop()
pygame.quit()
