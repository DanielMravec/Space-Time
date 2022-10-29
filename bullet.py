import sprite, screen_utils


class Bullet(sprite.Sprite):

    def __init__(self, speed, pos, dir):
        super().__init__(
            screen_utils.load_image('images/bullets/B_bullet_r120x120.png',
                                    (3, 3)), pos, 'bullet')
        self.speed = speed
        self.dir = dir

    def update(self, *args):
        self.move(self.speed)
        if screen_utils.is_touching_screen_edge((self.x, self.y)):
            sprite.sprites.remove(self)
