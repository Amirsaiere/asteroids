import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        velocity_one,velocity_two = self.velocity.rotate(rand_angle),self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_one = Asteroid(self.position.x,self.position.y,new_radius)
        split_asteroid_one.velocity = velocity_one * 1.2
        split_asteroid_two = Asteroid(self.position.x,self.position.y,new_radius)
        split_asteroid_two.velocity = velocity_two * 1.2

        
