import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)

    player_one = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            if ast.collide(player_one):
                print("GAME OVER")
                sys.exit()
            for bullet in shots:
                if bullet.collide(ast):
                    bullet.kill()
                    ast.split()
                    break

        screen.fill(color=(0,0,0))

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
