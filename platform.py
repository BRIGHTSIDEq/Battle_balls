import pygame

class Platform:
    def __init__(self, health, x):
        self.max_health = health
        self.health = health
        self.x = x
        self.y = 1500
        self.width = 400
        self.height = 50

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def draw(self, screen):
        # Платформа с прогресс-баром
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (200, 0, 0), (self.x - 200, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 200, 0), (self.x - 200, self.y, int(self.width * health_ratio), self.height))

        # Разделительные уровни (1000, 5000, 10000)
        font = pygame.font.SysFont("Arial", 30, bold=True)
        for i, lvl in enumerate([1000, 5000, 10000]):
            line_y = self.y - (i * 150)
            pygame.draw.line(screen, (0, 0, 0), (self.x - 200, line_y), (self.x + 200, line_y), 4)
            txt = font.render(f"{lvl:,}", True, (0, 0, 0))
            screen.blit(txt, (self.x - 50, line_y - 20))
