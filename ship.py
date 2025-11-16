"""
Ship entity for the Alien Invasion game.
"""

import pygame
import paths
from typing import TYPE_CHECKING

# Forward reference to avoid circular imports at runtime
if TYPE_CHECKING:
        from Lab12_kbreinholt1_v2 import AlienInvasion


class Ship(pygame.sprite.Sprite):

        """Represents the player's ship in the game world."""

        def __init__(self, game: 'AlienInvasion') -> None:
                super().__init__()      # REQUIRED for Sprite class

                self.game = game
                self.screen = game.screen
                self.settings = game.settings
                self.screen_rect = game.screen_rect

                # Load image
                self.image = pygame.image.load(paths.Graphics.ship1).convert_alpha()
                self.image: pygame.Surface = pygame.transform.scale(
                        pygame.image.load(paths.Graphics.ship1),
                        self.settings.ship_size
                ).convert_alpha()

                # Rect for sprite
                self.rect = self.image.get_rect()

                # Position ship centered horizontally and slightly above the bottom
                self.rect.midbottom = (
                        self.screen_rect.midbottom[0],
                        self.screen_rect.midbottom[1]
                        - (self.screen_rect.midbottom[1] // 75)
                )

                # Movement flags
                self.moving_right = False
                self.moving_left = False

                # Firing flags
                self.firing = False
                self.firing_rapid = False


        def update(self) -> None:

                """Update ship position based on movement flags."""

                # Padding to make the transition from side to side quicker
                buffer = 15

                # Firing slows ship
                self.speed = self.settings.ship_speed
                if self.firing and self.firing_rapid:
                        self.speed = self.settings.ship_rapid_firing_speed
                elif self.firing:
                        self.speed = self.settings.ship_base_firing_speed

                # Rightward movement and wrapping
                if self.moving_right:
                        self.rect.x += self.speed
                        if self.rect.left > self.settings.screen_size[0] - buffer:
                                self.rect.right = buffer

                # Leftward movement and wrapping
                if self.moving_left:
                        self.rect.x -= self.speed
                        if self.rect.right < buffer:
                                self.rect.left = self.settings.screen_size[0] - buffer


        def draw(self) -> None:
                """Draw the ship."""
                self.screen.blit(self.image, self.rect)
