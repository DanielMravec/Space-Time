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

ship_configs = [
    ShipConfig(name='borg',
               top_speed=5,
               slow_speed=-2,
               acceleration=3,
               turn_speed=3,
               slowdown_percent=95.65,
               costumes=[
                   CostumeConfig(path='images/player_imgs/P1_4.png',
                                 size=(15, 13)),
                   CostumeConfig(path='images/player_imgs/P1_4.png',
                                 size=(15, 13))
               ]),
    ShipConfig(name='titan',
               top_speed=2,
               slow_speed=-1,
               acceleration=1.5,
               turn_speed=1.25,
               slowdown_percent=95.75,
               costumes=[
                   CostumeConfig(path='images/player_imgs/P1_2.png',
                                 size=(21, 17)),
                   CostumeConfig(path='images/player_imgs/P1_2.png',
                                 size=(21, 17))
               ]),
    ShipConfig(name='glider',
               top_speed=10,
               slow_speed=-3,
               acceleration=4,
               turn_speed=5,
               slowdown_percent=98,
               costumes=[
                   CostumeConfig(path='images/player_imgs/P1_3.png',
                                 size=(15, 11)),
                   CostumeConfig(path='images/player_imgs/P2_3.png',
                                 size=(15, 11))
               ]),
    ShipConfig(name='zero_inertia',
               top_speed=5,
               slow_speed=-2,
               acceleration=3,
               turn_speed=3,
               slowdown_percent=50,
               costumes=[
                   CostumeConfig(path='images/player_imgs/P1_1.png',
                                 size=(11, 9)),
                   CostumeConfig(path='images/player_imgs/P1_1.png',
                                 size=(11, 9))
               ])
]

p1_config = PlayerConfig(
    player_index=0,
    keys=PlayerKeysConfig(
        left=pygame.K_a,
        right=pygame.K_d,
        forward=pygame.K_w,
        backward=pygame.K_s,
    ),
)

p2_config = PlayerConfig(
    player_index=1,
    keys=PlayerKeysConfig(
        left=pygame.K_LEFT,
        right=pygame.K_RIGHT,
        forward=pygame.K_UP,
        backward=pygame.K_DOWN,
    ),
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

p1 = player.Player((100 * scale, 100 * scale), p1_config, ship_configs[0])
p2 = player.Player((300 * scale, 300 * scale), p2_config, ship_configs[3])

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
