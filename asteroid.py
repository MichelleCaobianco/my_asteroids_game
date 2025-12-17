import pygame
from circleshape import CircleShape
from logger import log_event
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)   
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = vel1 * 1.2
            asteroid2.velocity = vel2 * 1.2
             

