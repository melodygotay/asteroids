from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print(f"New asteroid created at {x}, {y} with radius {radius}")
        self.radius = radius
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(
            random.uniform(-50, 50), 
            random.uniform(-50, 50)
)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            rand_angle = random.uniform(20, 50)

            new_velocity1 = self.velocity.rotate(rand_angle)
            new_velocity2 = self.velocity.rotate(-rand_angle)

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = new_velocity2 * 1.2

            #asteroid1.add(*Asteroid.containers)
            #asteroid2.add(*Asteroid.containers)