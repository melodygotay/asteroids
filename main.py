import pygame, sys, time
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *

def main():
    score = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    pygame.font.init()
    font = pygame.font.Font(None, 50)
    text_surface = font.render(f"Game over! You ended with a score of {score}", True, "white")
    text_place = text_surface.get_rect(center=(640, 360))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                text_surface = font.render(f"Game over! You ended with a score of {score}!", True, "white")
                text_place = text_surface.get_rect(center=(640, 360))
                screen.blit(text_surface, text_place)
                pygame.display.flip()
                time.sleep(3)
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    if asteroid.radius == 60:
                        score += 20
                    elif asteroid.radius == 40:
                        score += 40
                    else:
                        score += 60

                    shot.kill()
                    asteroid.split()

        # Update score surface after score changes
        score_surface = font.render(f"Score: {score}", True, "white")
        score_place = score_surface.get_rect(topleft=(20, 20))  # Position at top-left corner

        # Blit the score to the screen
        screen.blit(score_surface, score_place)

        player.draw_shots(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()