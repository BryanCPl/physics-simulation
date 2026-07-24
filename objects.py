import pygame
import pymunk


#walls
def create_boundaries(space,width,height):
    rect=[
        [(width/2,height+10),(width,20)],#floor
        [(width/2,-10),(width,20)],#ceiling
        [(-10,height/2),(20,height)],#right wall
        [(width+10,height/2),(20,height)]#left wall
    ]
    for pos,size in rect:
        body=pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position=pos
        shape=pymunk.Poly.create_box(body,size)
        shape.color=(0,0,0,50)
        shape.elasticity=0.4
        shape.friction=0.5
        space.add(body,shape)

def create_rect(space,x,y,width,height,color):
    rects=[
        [(x,y),(width,height),color,100],
    ]

    for pos,size,color,mass in rects:
        body=pymunk.Body()
        body.position=pos
        shape=pymunk.Poly.create_box(body,size)
        shape.color=color
        shape.mass=mass
        shape.elasticity=0.4
        shape.friction=0.4
        space.add(body,shape)

def create_ball(space,radius,mass,pos):
    body=pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position=(pos)
    shape=pymunk.Circle(body,radius)
    shape.mass=mass
    shape.color=(100,100,240,100)
    shape.elasticity=0.9
    shape.friction=0.5
    space.add(body,shape)
    return shape

def create_swinging_ball(space):
    rotation_center_body=pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position=(300,300)
    body=pymunk.Body()
    body.position=(300,300)
    line=pymunk.Segment(body,(0,0),(150,0),5)
    circle=pymunk.Circle(body,40,(150,0))
    line.friction=1
    line.mass=8
    circle.mass=8
    circle.friction=1
    circle.elasticity=0.45
    rotation_center_joint=pymunk.PinJoint(body,rotation_center_body,(0,0))
    space.add(circle,line,body,rotation_center_joint)