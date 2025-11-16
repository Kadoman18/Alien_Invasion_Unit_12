"""
Laser entities for the Alien Invasion game.

Provides sprite loading, positioning logic, and screen drawing behavior
for the ships lasers. Integrates with the main AlienInvasion game
instance to access window dimensions, settings, and display surfaces.
"""

import pygame
import paths
from typing import TYPE_CHECKING

# Forward reference to avoid circular imports at runtime
if TYPE_CHECKING:
        from Lab12_kbreinholt1_v2 import AlienInvasion


class Laser(pygame.sprite.Sprite):
        """Houses the laser projectile surf, rect, and movement behavior."""

        def __init__(self, game: 'AlienInvasion') -> None:

                # Initialize sprite class
                super().__init__()

                # Basic references to AlienInvasion class and Settings class
                self.game = game
                self.settings = game.settings
                self.ship = game.ship

                # Main display surface and its bounding rectangle
                self.screen_image: pygame.Surface = game.screen
                self.screen_rect: pygame.Rect = game.screen_rect

                # Surf and rect for laser sprite
                self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(paths.Graphics.laser), self.settings.laser_size).convert_alpha()
                self.rect: pygame.Rect = self.image.get_rect(midtop = (self.ship.rect.midtop))

                # Set the lasers travel speed
                self.speed: int = self.settings.laser_speed


        def update(self) -> None:
                """Updates the lasers position."""

                # Lasers movement
                self.rect.y -= self.speed

                # Delete the laser when it leaves the screen
                if self.rect.y < -5:
                        self.kill()

