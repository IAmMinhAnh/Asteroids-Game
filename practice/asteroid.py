import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return 
        else:
            log_event("asteroid_split")
            direct = random.uniform(20, 50)
            direct_1 = self.velocity.rotate(direct)
            direct_2 = self.velocity.rotate(-direct)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = direct_1 * 1.2
            asteroid_2.velocity = direct_2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt 