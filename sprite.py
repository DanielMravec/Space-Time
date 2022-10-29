import pygame, screen_utils, math

sprites = []


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, pos, category):
        global sprites
        super().__init__()
        self.orig_image = image
        self.image = self.orig_image
        self.mask = pygame.mask.from_surface(self.image)
        self.x = pos[0]
        self.y = pos[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.dir = 0
        self.category = category
        sprites.append(self)

    def rotate_cw(self, degrees):
        self.dir += degrees
        old_rect = self.rect
        self.image = pygame.transform.rotate(self.orig_image, -self.dir)
        self.mask = pygame.mask.from_surface(self.image)
        new_rect = self.image.get_rect()
        new_rect.center = old_rect.center
        self.rect = new_rect

    def move(self, dist):
        dir_radians = math.radians(self.dir)
        x = dist * math.sin(dir_radians)
        y = -dist * math.cos(dir_radians)

        self.x += x
        self.y += y

        (self.x, self.y) = screen_utils.fence_to_screen((self.x, self.y))
        self.rect.center = (self.x, self.y)

    def is_touching_sprite(self, other_sprite):
        if not pygame.sprite.collide_mask(self, other_sprite) == None:
            return True
        else:
            return False
