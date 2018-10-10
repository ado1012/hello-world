import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Star Wars")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    bullets2 = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    alien = Alien(ai_settings, screen)
    bg_color = (255, 255, 255)
    play_button = Button(ai_settings, screen, "Press P to Play")
    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2, play_button)


    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, bullets2)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, bullets2)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bullets2, play_button)

run_game()
