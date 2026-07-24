import objects

BLUE=(76, 201, 240,100)
DARKBLUE=(67, 97, 238,100)

def house(space,initial_pos):
    objects.create_rect(space,initial_pos[0],initial_pos[1],40,100,BLUE)
    objects.create_rect(space,initial_pos[0]+280,initial_pos[1],40,100,BLUE)
    objects.create_rect(space,initial_pos[0]+150,initial_pos[1]-60,350,40,DARKBLUE)
    objects.create_rect(space,initial_pos[0]+150,initial_pos[1]+60,350,40,DARKBLUE)