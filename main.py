import pygame, sys, player
from pygame.locals import QUIT

pygame.init()

screen_info = pygame.display.Info()
(screen_width, screen_height) = (int(screen_info.current_w), int(screen_info.current_h))
scale = screen_width / 480

screen = pygame.display.set_mode((screen_width, screen_width / 480 * 360))
screen_rect = screen.get_rect()

p1 = player.Player(scale, (200 * scale, 200 * scale))

def main():
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    screen.fill((255,255,255))
    screen.blit(p1.image, p1.rect)
    
    pygame.display.update()

if __name__ == '__main__':
  main()