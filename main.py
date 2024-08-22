import pygame, sys, time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        pygame.font.init()
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Game over!", True, "white")
        text_place = text_surface.get_rect(center=(640, 360))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collides_with(player):
                pygame.display.set_caption("Game over!")
                screen.blit(text_surface, text_place)
                pygame.display.flip()
                time.sleep(3)
                sys.exit()

        player.draw_shots(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()