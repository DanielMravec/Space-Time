import pygame

#Not only for the screen

screen_rect = pygame.rect.Rect(0, 0, 0, 0)

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

def is_touching_screen_edge(pos):
    return pos[0] < 1 or \
           pos[1] < 1 or \
           pos[0] > screen_rect.width - 1 or \
           pos[1] > screen_rect.height - 1

def load_image(img_path, size):
    global scale
    image = pygame.image.load(img_path).convert_alpha()
    image = pygame.transform.smoothscale(image,
                                         (size[0] * scale, size[1] * scale))
    return image
