import pygame

screen_rect = pygame.rect.Rect(0,0,0,0)

def init(screen):
  global screen_rect
  screen_rect = screen

def fence_to_screen(sprite_rect):
  print(str(sprite_rect), str(screen_rect))
  rect = sprite_rect.copy()
  if rect.center[0] < 0:
    rect.center = (0, rect.center[1])
  if rect.center[1] < 0:
    rect.center = (rect.center[0], 0)
  if rect.center[0] > screen_rect.width:
    rect.center = (screen_rect.width, rect.center[1])
  if rect.center[1] > screen_rect.height:
    rect.center = (rect.center[0], screen_rect.height)
  return rect