import objects
import pygame
import structures
import pymunk
import pymunk.pygame_util
import math

pygame.init()

WIDTH,HEIGHT=1024,720
fondo = pygame.image.load("fondo.png")
fondoEscalado=pygame.transform.scale(fondo,(WIDTH,HEIGHT))
window=pygame.display.set_mode((WIDTH,HEIGHT))


def calculate_distance(p1,p2):
    return math.sqrt((p2[1]-p1[1])**2+(p2[0]-p1[0])**2)

def calculate_angle(p1,p2):
    return math.atan2(p2[1]-p1[1],p2[0]-p1[0])

def draw(space,window,draw_options,line):
    window.blit(fondoEscalado, (0, 0))
    if line:
        pygame.draw.line(window,"black",line[0],line[1],3)
    space.debug_draw(draw_options)

    pygame.display.update()


def run(window,width,height):
    run=True
    clock=pygame.time.Clock()
    fps=60
    dt=1/fps

    space=pymunk.Space()
    space.gravity=(0,981)

    objects.create_boundaries(space,width,height)
    structures.house(space,(500,500))
    structures.house(space,(500,300))
    structures.house(space,(500,200))
    objects.create_ball(space,50,10,(80,90)).body.body_type=pymunk.Body.DYNAMIC
    objects.create_boundaries(space,width,height)
    objects.create_swinging_ball(space)
    draw_options=pymunk.pygame_util.DrawOptions(window)

    pressed_pos=None
    ball=None


    while run:
        line=None
        if ball and pressed_pos:
            line=[pressed_pos,pygame.mouse.get_pos()]
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            if event.type==pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos=pygame.mouse.get_pos()
                    ball=objects.create_ball(space,30,10,pressed_pos)
                elif pressed_pos:
                    ball.body.body_type=pymunk.Body.DYNAMIC
                    angle=calculate_angle(*line)
                    force=calculate_distance(*line)*40
                    fx=math.cos(angle)*force
                    fy=math.sin(angle)*force
                    ball.body.apply_impulse_at_local_point((fx,fy),(0,0))
                    pressed_pos=None
                else:
                    space.remove(ball,ball.body)
                    ball=None
                    
        draw(space,window,draw_options,line)
        space.step(dt)
        clock.tick(fps)
        
    pygame.quit()

if __name__=='__main__':
    run(window,WIDTH,HEIGHT)