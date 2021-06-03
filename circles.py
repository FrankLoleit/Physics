import pygame
from gameObjects import GameObject
import random
import pymunk

class Circle:
    def __init__(self, windowWidth, windowHeight, radius, thickness):
        self.__windowWidth = windowWidth
        self.__windowHeight = windowHeight
        self.__radius = radius
        self.__thickness = thickness
        
        #Pymunk Physics
        self.__space = pymunk.Space()
        self.__space.gravity = (1, 300)
        if random.choice([False, True]):
            self.__behaviour = "dynamic"
            self.__color = (0, 150, 255)
            self.__x = random.randint(0 + self.__radius, windowWidth - self.__radius)
            self.__y = random.randint(0 + self.__radius, windowHeight/2 - self.__radius)
        else:
            self.__behaviour = "static"
            self.__color = (255, 50, 80)
            self.__x = random.randint(0 + radius, windowWidth - self.__radius)
            self.__y = random.randint(0 + radius + windowHeight/2, windowHeight - self.__radius)

        self.__physicalShape = self.__createBall(self.__space, self.__behaviour)

        # Pass object to shared list that main loop will use to draw objects on screen
        GameObject.objects.append(self.__physicalShape)
        GameObject.spaces.append(self.__space)
        
            
    def __createBall(self, space, behaviour):
        if behaviour == 'static':
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
        elif behaviour == 'dynamic':
            body = pymunk.Body(100, 10, body_type=pymunk.Body.DYNAMIC)
        body.position = (self.__x, self.__y)
        shape = pymunk.Circle(body, self.__radius)
        self.__space.add(body, shape)
        return shape

    
    
    
        