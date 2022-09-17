import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self, scale, pos):
    super().__init__()
    self.image = pygame.image.load('images/P1_4.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (15 * scale, 13 * scale))
    self.rect = self.image.get_rect()
    self.rect.center = pos