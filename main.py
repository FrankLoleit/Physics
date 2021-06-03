import pygame
from circles import Circle
from gameObjects import GameObject
import random
import pymunk

print("Hello-print.") #delete this

windowWidth = 1000
windowHeight = 800

clock = pygame.time.Clock()

bgColor = (0, 0, 0)
(windowWidth, windowHeight) = (windowWidth, windowHeight)

screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Frank's pygame-Example")

for obj in range(16):
    circle = Circle(windowWidth, windowHeight, 20, 10)

def draw(surface):
    for obs in GameObject.objects:
        pos_x = int(obs.body.position.x)
        pos_y = int(obs.body.position.y)
        pygame.draw.circle(surface, (0,127,255), (pos_x, pos_y), 20, 10)
        

def updateSpace():
    for space in GameObject.spaces:
        space.step(1/60)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(bgColor)
    draw(screen)
    updateSpace()

    clock.tick(60)
    pygame.display.flip()
