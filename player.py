import pygame, math

class Player(pygame.sprite.Sprite):
  def __init__(self, scale, pos):
    super().__init__()
    self.image = pygame.image.load('images/P1_4.png').convert_alpha()
    self.image = pygame.transform.smoothscale(self.image, (15 * scale, 13 * scale))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.dir = 90
    self.speed = 0

  def update(self, pressed_keys):
    if pygame.K_d in pressed_keys:
      self.dir += 5
    if pygame.K_a in pressed_keys:
      self.dir -= 5
    if pygame.K_w in pressed_keys:
      self.speed += 0.1
    if pygame.K_s in pressed_keys:
      self.speed -= 0.1

    if self.speed > 20:
      self.speed = 20
    if self.speed < -10:
      self.speed = -10
    
    dir_radians = math.radians(self.dir)
    x = self.speed * math.sin(dir_radians)
    y = -self.speed * math.cos(dir_radians)

    self.rect.move_ip((x, y))

    if self.rect.center[0] < 0:
      self.rect.center = (0, self.rect.center[1])
    if self.rect.center[1] < 0:
      self.rect.center = (self.rect.center[0], 0)
    