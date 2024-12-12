import pygame
from constants import * 
from player import Player

pygame.init()

def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_time = pygame.time.Clock()

    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y)

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()

        for object in updatable:
            object.update(dt)
        
        
        
        dt = game_time.tick(60)/1000

if __name__ == "__main__":
    main()