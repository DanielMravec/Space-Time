import pygame, sys, player, screen_utils
from pygame.locals import QUIT

pygame.init()

clock = pygame.time.Clock()

screen_info = pygame.display.Info()
(screen_width, screen_height) = (int(screen_info.current_w),
                                 int(screen_info.current_h))

scale = min(screen_height / 360, screen_width / 480)

screen = pygame.display.set_mode((480 * scale, scale * 360), pygame.NOFRAME)
screen_rect = screen.get_rect()

screen_utils.init(screen_rect, scale)

p1 = player.Player(
    (100 * scale, 100 * scale), (15, 13), 'images/P1_4.png', {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'forward': pygame.K_w,
        'backward': pygame.K_s,
    })
p2 = player.Player(
    (300 * scale, 300 * scale), (18, 15), 'images/P2_2.png', {
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'forward': pygame.K_UP,
        'backward': pygame.K_DOWN,
    })

pressed_keys = {}


def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                pressed_keys[event.key] = True

            if event.type == pygame.KEYUP:
                del pressed_keys[event.key]

        p1.update(
            pressed_keys, {
                'top_speed': 5,
                'slow_speed': -2,
                'acceleration': 3,
                'turn_speed': 3,
                'slowdown_percent': 95.65
            })
        p2.update(
            pressed_keys, {
                'top_speed': 2.5,
                'slow_speed': -1,
                'acceleration': 1.5,
                'turn_speed': 1.25,
                'slowdown_percent': 95.75
            })

        screen.fill((255, 255, 255))
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
