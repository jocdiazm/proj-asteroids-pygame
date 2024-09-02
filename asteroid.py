import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def collisions_with(self, other):
        return super().collisions_with(other)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vec_1 = self.velocity.rotate(random_angle)
            vec_2 = self.velocity.rotate(-1 * random_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(
                self.position.x, self.position.y, new_asteroid_radius
            )
            new_asteroid_2 = Asteroid(
                self.position.x, self.position.y, new_asteroid_radius
            )
            new_asteroid_1.velocity = vec_1 * 1.2
            new_asteroid_2.velocity = vec_2
