import pygame, random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        ast_1_direction = self.velocity.rotate(angle)
        ast_2_direction = self.velocity.rotate(-angle)
        ast_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, ast_radius)
        ast_2 = Asteroid(self.position.x, self.position.y, ast_radius)
        ast_1.velocity = ast_1_direction * 1.2
        ast_2.velocity = ast_2_direction * 1.2