import pygame

class Ball:
    def __init__(self, name, color, speed, damage, clones, ball_type, x):
        self.name = name
        self.color = color
        self.speed = speed
        self.damage = damage
        self.clones = clones
        self.type = ball_type
        self.x = x
        self.y = 200
        self.vy = speed
        self.history = [self.y] * clones

    def move(self, platform_y):
        self.vy += 0.5  # гравитация
        self.y += self.vy

        if self.y >= platform_y - 50:
            self.y = platform_y - 50
            self.vy = -self.speed  # отскок
            self.damage += 1
            if self.type == "speed_boost":
                self.speed += 0.3

        self.history.pop()
        self.history.insert(0, self.y)

    def draw(self, screen):
        for i in range(self.clones):
            pygame.draw.circle(screen, self.color, (self.x, int(self.history[i])), 30)
