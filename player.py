import pygame, screen_utils, sprite


class Player(sprite.Sprite):

    def __init__(self, pos, config):
        self.config = config
        self.ship_config = config.ships[0]
        self.keys = config.keys
        image = pygame.image.load(
            self.ship_config.costume.path).convert_alpha()
        image = pygame.transform.smoothscale(
            image, (self.ship_config.costume.size[0] * screen_utils.scale,
                    self.ship_config.costume.size[1] * screen_utils.scale))
        image = pygame.transform.rotate(image, 90)

        super().__init__(image, pos)

        self.speed = 0

    def update(self, pressed_keys):
        if self.keys.right in pressed_keys:
            self.rotate_cw(self.ship_config.turn_speed)
        if self.keys.left in pressed_keys:
            self.rotate_cw(-self.ship_config.turn_speed)
        if self.keys.forward in pressed_keys:
            self.speed += self.ship_config.acceleration
        if self.keys.backward in pressed_keys:
            self.speed -= self.ship_config.acceleration

        if self.speed > self.ship_config.top_speed:
            self.speed = self.ship_config.top_speed
        if self.speed < self.ship_config.slow_speed:
            self.speed = self.ship_config.slow_speed

        self.speed *= self.ship_config.slowdown_percent / 100

        self.move(self.speed)
