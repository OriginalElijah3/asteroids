import pygame
import sys
from constants import * 

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()

def main():    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_time = pygame.time.Clock()

    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    player = Player(x, y)
    asteroid_field = AsteroidField()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for object in drawable:
            object.draw(screen)
        
        for object in updatable:
            object.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                running = False
                sys.exit("Game Over!")
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        
        dt = game_time.tick(60)/1000

if __name__ == "__main__":
    main()