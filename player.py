from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.math.Vector2(x, y)
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.shots = []

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        for shot in self.shots[:]:
            if (shot.position.x < 0 or 
                shot.position.x > SCREEN_WIDTH or
                shot.position.y < 0 or
                shot.position.y > SCREEN_HEIGHT):
                self.shots.remove(shot)
            else:
                shot.position += shot.velocity * dt
                             
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, shot_velocity)
        self.shots.append(new_shot)

    def draw_shots(self, screen):
        for shot in self.shots:
            pygame.draw.circle(screen, "red", (shot.position.x, shot.position.y), SHOT_RADIUS)

class Shot(CircleShape):
    def __init__(self, positionx, positiony, radius, velocity):
        super().__init__(positionx, positiony, radius)
        self.radius = radius
        self.velocity = velocity