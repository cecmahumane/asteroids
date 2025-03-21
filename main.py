import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    AsteroidField.containers = (updatables,)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    Shot.containers = (shots_group, updatables, drawables)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    # shot = Shot()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)
        for single_asteroid in asteroids:
            if player.check_for_collision(single_asteroid):
                print("Game over!")
                sys.exit()
            
            for shot in shots_group:
                if single_asteroid.check_for_collision(shot):
                    shot.kill()
                    single_asteroid.split()
                else:
                    pass
                

        screen.fill('black')
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        # Limit framerate to 60 FPS
        dt = (clock.tick(60))/1000
        










if __name__ == "__main__":
    main()