import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
