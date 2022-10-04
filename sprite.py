import pygame, screen_utils, math


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, pos):
        super().__init__()
        self.orig_image = image
        self.image = self.orig_image
        self.x = pos[0]
        self.y = pos[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.dir = 0

    def rotate_cw(self, degrees):
        self.dir += degrees
        old_rect = self.rect
        self.image = pygame.transform.rotate(self.orig_image, -self.dir)
        new_rect = self.image.get_rect()
        new_rect.center = old_rect.center
        self.rect = new_rect

    def move(self, dist):
        dir_radians = math.radians(self.dir)
        x = self.speed * math.sin(dir_radians)
        y = -self.speed * math.cos(dir_radians)

        self.x += x
        self.y += y

        (self.x, self.y) = screen_utils.fence_to_screen((self.x, self.y))
        self.rect.center = (self.x, self.y)
