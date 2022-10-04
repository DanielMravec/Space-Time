import pygame, screen_utils, sprite


class Player(sprite.Sprite):
    def __init__(self, pos, size, image_path, keys):
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.smoothscale(
            image, (size[0] * screen_utils.scale, size[1] * screen_utils.scale))
        image = pygame.transform.rotate(image, 90)
      
        super().__init__(image, pos)
      
        self.speed = 0
        self.keys = keys

    def update(self, pressed_keys):
        if self.keys['right'] in pressed_keys:
            self.rotate_cw(5)
        if self.keys['left'] in pressed_keys:
            self.rotate_cw(-5)
        if self.keys['forward'] in pressed_keys:
            self.speed += 0.3
        if self.keys['backward'] in pressed_keys:
            self.speed -= 0.3

        if self.speed > 5:
            self.speed = 5
        if self.speed < -2:
            self.speed = -2

        self.speed *= 0.95

        self.move(self.speed)
