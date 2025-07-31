import pygame
import json
from core.ball import Ball
from core.platform import Platform
from core.battle import Battle
from core.renderer import export_video
from core.voice import generate_voice

with open("config.json", "r") as f:
    config = json.load(f)

WIDTH, HEIGHT, FPS = config["width"], config["height"], config["fps"]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36, bold=True)

# Левая и правая зоны
balls = [
    Ball(config["balls"][0]["name"], tuple(config["balls"][0]["color"]), config["balls"][0]["speed"], config["balls"][0]["damage"], config["balls"][0]["clones"], config["balls"][0]["type"], 300),
    Ball(config["balls"][1]["name"], tuple(config["balls"][1]["color"]), config["balls"][1]["speed"], config["balls"][1]["damage"], config["balls"][1]["clones"], config["balls"][1]["type"], 780)
]

platforms = [
    Platform(config["platform_health"], 300),
    Platform(config["platform_health"], 780)
]

battle = Battle(balls, platforms, font)
voice_file = generate_voice(f"{balls[0].name} vs {balls[1].name}, who will win?")

running = True
while running:
    running = battle.update(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
export_video(battle.frames, FPS, voice_file)
