import pygame

class Battle:
    def __init__(self, balls, platforms, font):
        self.balls = balls
        self.platforms = platforms
        self.frames = []
        self.font = font
        self.damages = [[], []]  # отдельные ленты урона для каждого шара
        self.winner = None

    def draw_ui(self, screen):
        # Имена шаров сверху
        for i, ball in enumerate(self.balls):
            name_txt = self.font.render(ball.name, True, ball.color)
            screen.blit(name_txt, (ball.x - 100, 50))
            stats = self.font.render(f"Speed: {ball.speed:.1f} | Damage: {ball.damage}", True, (0, 0, 0))
            screen.blit(stats, (ball.x - 150, 100))

        # Урон
        for idx, dmg_list in enumerate(self.damages):
            for j, dmg in enumerate(dmg_list):
                dmg_txt = self.font.render(str(dmg), True, (255, 0, 0))
                screen.blit(dmg_txt, (self.balls[idx].x - 150 + j * 20, 20))

        # Если есть победитель
        if self.winner:
            win_txt = self.font.render(f"{self.winner} WINS!", True, (0, 200, 0))
            screen.blit(win_txt, (500, 200))

    def update(self, screen):
        screen.fill((240, 230, 210))

        for i, (ball, platform) in enumerate(zip(self.balls, self.platforms)):
            platform.draw(screen)
            prev_y = ball.y
            ball.move(platform.y)
            ball.draw(screen)

            if prev_y < platform.y - 50 <= ball.y:
                platform.take_damage(ball.damage)
                self.damages[i].append(ball.damage)
                if len(self.damages[i]) > 15:
                    self.damages[i].pop(0)

                if platform.health <= 0 and not self.winner:
                    self.winner = ball.name

        self.draw_ui(screen)
        frame = pygame.surfarray.array3d(screen).swapaxes(0, 1)
        self.frames.append(frame)
        return self.winner is None
