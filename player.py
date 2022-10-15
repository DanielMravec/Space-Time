import pygame, screen_utils, sprite, bullet


class Player(sprite.Sprite):

    def __init__(self, pos, config, ship_config):
        self.config = config
        self.ship_config = ship_config
        self.keys = config.keys
        self.speed = 0
        self.bullet_fired_time = 0

        costume = self.ship_config.costumes[self.config.player_index]

        image = screen_utils.load_image(costume.path, costume.size)
        image = pygame.transform.rotate(image, 90)

        super().__init__(image, pos)

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

        if self.keys.fire in pressed_keys and \
                pygame.time.get_ticks() >= self.bullet_fired_time + 100:
            ammo = bullet.Bullet(10, (self.x, self.y), self.dir)
            ammo.move(10)
            self.bullet_fired_time = pygame.time.get_ticks()
