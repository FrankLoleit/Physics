import pygame
import pymunk
import random

windowWidth = 800
windowHeight = 800


def draw(objs):
    for obj in objs:
        pos_x = int(obj.body.position.x)
        pos_y = int(obj.body.position.y)
        pygame.draw.circle(screen, (0, 0, 255), (pos_x, pos_y), 20)

def createBall(space, behaviour, x, y):
        if behaviour == 'static':
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
        elif behaviour == 'dynamic':
            body = pymunk.Body(100, 10, body_type=pymunk.Body.DYNAMIC)
        body.position = (x, y)
        shape = pymunk.Circle(body, 20)
        space.add(body, shape)
        return shape



clock = pygame.time.Clock()

bgColor = (220, 220, 220)
(windowWidth, windowHeight) = (windowWidth, windowHeight)

screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Frank's pygame-Example")


space = pymunk.Space()
space.gravity = (0, 300)

objs = []
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))
objs.append(createBall(space, 'dynamic', random.randint(0,700), random.randint(0,350)))



objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))
objs.append(createBall(space, 'static', random.randint(0,700), random.randint(400,700)))




run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(bgColor)

    draw(objs)
    space.step(1/60)
    
    pygame.display.flip()
    clock.tick(60)
