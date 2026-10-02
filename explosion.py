import pygame


class Explosion(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, position, duration=0.3):
        super().__init__(*self.containers)

        self.position = pygame.Vector2(position)
        self.duration = duration
        self.timer = 0.0
        self.max_radius = 35

    def update(self, dt):
        self.timer += dt

        if self.timer >= self.duration:
            self.kill()

    def draw(self, screen):
        progress = self.timer / self.duration

        radius = int(self.max_radius * progress)
        width = max(1, int(6 * (1 - progress)))

        pygame.draw.circle(
            screen,
            "orange",
            self.position,
            radius,
            width=width
        )