import pygame, math, screen_utils


class Player(pygame.sprite.Sprite):

    def __init__(self, scale, pos):
        super().__init__()
        self.orig_image = pygame.image.load('images/P1_4.png').convert_alpha()
        self.orig_image = pygame.transform.smoothscale(
            self.orig_image, (15 * scale, 13 * scale))
        self.orig_image = pygame.transform.rotate(self.orig_image, 90)
        self.image = self.orig_image
        self.x = pos[0]
        self.y = pos[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.dir = 0
        self.speed = 0

    def update(self, pressed_keys):
        if pygame.K_d in pressed_keys:
            self.rotate_cw(5)
        if pygame.K_a in pressed_keys:
            self.rotate_cw(-5)
        if pygame.K_w in pressed_keys:
            self.speed += 0.1
        if pygame.K_s in pressed_keys:
            self.speed -= 0.1

        if self.speed > 5:
            self.speed = 5
        if self.speed < -2:
            self.speed = -2

        dir_radians = math.radians(self.dir)
        x = self.speed * math.sin(dir_radians)
        y = -self.speed * math.cos(dir_radians)

        self.x += x
        self.y += y

        (self.x, self.y) = screen_utils.fence_to_screen((self.x, self.y))
        self.rect.center = (self.x, self.y)

    def rotate_cw(self, degrees):
        self.dir += degrees
        old_rect = self.rect
        self.image = pygame.transform.rotate(self.orig_image, -self.dir)
        new_rect = self.image.get_rect()
        new_rect.center = old_rect.center
        self.rect = new_rect
