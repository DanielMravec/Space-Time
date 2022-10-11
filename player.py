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

    def update(self, pressed_keys, movement):
        if self.keys['right'] in pressed_keys:
            self.rotate_cw(movement['turn_speed'])
        if self.keys['left'] in pressed_keys:
            self.rotate_cw(-movement['turn_speed'])
        if self.keys['forward'] in pressed_keys:
            self.speed += movement['acceleration']
        if self.keys['backward'] in pressed_keys:
            self.speed -= movement['acceleration']

        if self.speed > movement['top_speed']:
            self.speed = movement['top_speed']
        if self.speed < movement['slow_speed']:
            self.speed = movement['slow_speed']

        self.speed *= movement['slowdown_percent'] / 100

        self.move(self.speed)\
