"""
Module providing the main Alien Invasion game loop using pygame.
Includes the core game window initialization.
"""

import pygame
from settings import Settings
from ship import Ship
from laser import Laser


class AlienInvasion:

        """
        Main game controller for the Alien Invasion application.
        """

        def __init__(self) -> None:

                pygame.init()
                self.settings = Settings()

                self.screen = pygame.display.set_mode((self.settings.screen_size))

                self.screen_rect = self.screen.get_rect(
                        midbottom=(
                                self.settings.ScreenSize.x // 2,
                                self.settings.ScreenSize.y
                        )
                )

                pygame.display.set_caption(self.settings.name)
                pygame.display.set_icon(pygame.image.load(self.settings.icon))

                self.sky_image = pygame.transform.scale(
                        pygame.image.load(self.settings.background).convert(),
                        self.settings.screen_size
                )
                self.sky_rect = self.sky_image.get_rect()

                # Create the player's ship (sprite)
                self.ship = Ship(self)

                # Create the ship sprite
                self.ship_group = pygame.sprite.GroupSingle()
                self.ship_group.add(self.ship)

                # Create the lasers
                self.lasers = pygame.sprite.Group()

                self.running = True
                self.clock = pygame.time.Clock()


        def _fire_laser(self) -> None:
                now = pygame.time.get_ticks()

                if not hasattr(self, "last_shot_time"):
                        self.last_shot_time = 0

                if self.ship.firing and (now - self.last_shot_time >= self.settings.ship_base_fire_rate):
                        laser = Laser(self)
                        self.lasers.add(laser)
                        self.last_shot_time = now

                elif self.ship.firing and self.ship.firing_rapid and (now - self.last_shot_time >= self.settings.ship_rapid_fire_rate):
                        laser = Laser(self)
                        self.lasers.add(laser)
                        self.last_shot_time = now


        def _event_listener(self) -> None:

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                self.running = False
                                pygame.quit()
                                exit()

                        elif event.type == pygame.KEYDOWN:
                                self._key_down_event(event)

                        elif event.type == pygame.KEYUP:
                                self._key_up_event(event)


        def _key_down_event(self, event):
                if event.key == pygame.K_a:
                        self.ship.moving_left = True
                elif event.key == pygame.K_d:
                        self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                elif event.key == pygame.K_SPACE:
                        self.ship.firing = True
                elif event.key == pygame.K_LSHIFT:
                        self.ship.firing_rapid = True
                elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        exit()


        def _key_up_event(self, event) -> None:

                if event.key == pygame.K_a:
                        self.ship.moving_left = False
                elif event.key == pygame.K_d:
                        self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                elif event.key == pygame.K_SPACE:
                        self.ship.firing = False
                elif event.key == pygame.K_LSHIFT:
                        self.ship.firing_rapid = False


        def _update_screen(self) -> None:

                self.screen.blit(self.sky_image, (0, 0))

                # >>> DRAW SHIP USING SPRITE GROUP <<<
                self.ship_group.draw(self.screen)

                # Lasers
                self.lasers.draw(self.screen)

                pygame.display.flip()


        def run_game(self) -> None:

                while True:

                        self._event_listener()

                        # >>> UPDATE SHIP USING SPRITE GROUP <<<
                        self.ship_group.update()

                        self._fire_laser()

                        self.lasers.update()

                        self._update_screen()

                        self.clock.tick(self.settings.fps)


if __name__ == '__main__':
        AlienInvasion().run_game()
