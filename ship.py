import pygame
import paths
from typing import TYPE_CHECKING

if TYPE_CHECKING:
        from Lab12_kbreinholt1_v2 import AlienInvasion

class Ship:
        def __init__(self, game: 'AlienInvasion') -> None:
                self.game: object = game
                self.settings: object = game.settings
                self.screen: pygame.Surface = game.screen
                self.screen_rect: pygame.Rect = game.screen_rect
                self.surf: pygame.Surface = pygame.transform.scale(pygame.image.load(paths.Graphics.ship1), self.settings.ship_size).convert_alpha()
                self.rect: pygame.Rect = self.surf.get_rect(midbottom = (
                        self.screen_rect.midbottom[0], self.screen_rect.midbottom[1] - (self.screen_rect.midbottom[1] // 100)
                        ))
