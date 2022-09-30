import pygame

screen_rect = pygame.rect.Rect(0,0,0,0)

scale = 1

def init(screen, scale_arg):
  global screen_rect, scale
  screen_rect = screen
  scale = scale_arg

def fence_to_screen(pos):
  if pos[0] < 0:
    pos = (0, pos[1])
  if pos[1] < 0:
    pos = (pos[0], 0)
  if pos[0] > screen_rect.width:
    pos = (screen_rect.width, pos[1])
  if pos[1] > screen_rect.height:
    pos = (pos[0], screen_rect.height)
  return pos