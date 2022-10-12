import pygame, sys, player, screen_utils
from pygame.locals import QUIT
from config import PlayerConfig, ShipConfig, CostumeConfig, PlayerKeysConfig

pygame.init()

clock = pygame.time.Clock()

screen_info = pygame.display.Info()
(screen_width, screen_height) = (int(screen_info.current_w),
                                 int(screen_info.current_h))

scale = min(screen_height / 360, screen_width / 480)

screen = pygame.display.set_mode((480 * scale, scale * 360), pygame.NOFRAME)
screen_rect = screen.get_rect()

screen_utils.init(screen_rect, scale)

p1_config = PlayerConfig(
    keys=PlayerKeysConfig(
        left=pygame.K_a,
        right=pygame.K_d,
        forward=pygame.K_w,
        backward=pygame.K_s,
    ),
    ships=[
        ShipConfig(name='borg',
                   top_speed=5,
                   slow_speed=-2,
                   acceleration=3,
                   turn_speed=3,
                   slowdown_percent=95.65,
                   costume=CostumeConfig(path='images/player_imgs/P1_4.png',
                                         size=(15, 13)))
    ],
)

p2_config = PlayerConfig(
    keys=PlayerKeysConfig(
        left=pygame.K_LEFT,
        right=pygame.K_RIGHT,
        forward=pygame.K_UP,
        backward=pygame.K_DOWN,
    ),
    ships=[
        ShipConfig(name='titan',
                   top_speed=1.5,
                   slow_speed=-0.5,
                   acceleration=1.5,
                   turn_speed=1.25,
                   slowdown_percent=95.75,
                   costume=CostumeConfig(path='images/player_imgs/P1_2.png',
                                         size=(18, 15)))
    ],
)

# p1_images = {
#     'zero_inertia': 'images/player_imgs/P1_1.png',
#     'titan': 'images/player_imgs/P1_2.png',
#     'glider': 'images/player_imgs/P1_3.png',
#     'borg': 'images/player_imgs/P1_4.png',
#     'dart': 'images/player_imgs/P1_5.png',
#     'balanced': 'images/player_imgs/P1_6.png'
# }

# p2_images = {
#     'zero_inertia': 'images/player_imgs/P1_1.png',
#     'titan': 'images/player_imgs/P1_2.png',
#     'glider': 'images/player_imgs/P2_3.png',
#     'borg': 'images/player_imgs/P1_4.png',
#     'dart': 'images/player_imgs/P2_5.png',
#     'balanced': 'images/player_imgs/P2_6.png'
# }

p1 = player.Player((100 * scale, 100 * scale), p1_config)
p2 = player.Player((300 * scale, 300 * scale), p2_config)

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

        p1.update(pressed_keys)
        p2.update(pressed_keys)

        screen.fill((255, 255, 255))
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
