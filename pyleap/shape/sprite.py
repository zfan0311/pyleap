import pyglet

from pyleap.util import rss
from pyleap.window import window
from pyleap.shape.rectangle import Rectangle


cache_images = {}


class Sprite(Rectangle):
    """ Sprite """

    def __init__(self, src, x=300, y=200, w=None, h=None):
        """
        默认位置： 300, 200
        """
        self.src = src
        w = w or self._sprite.width
        h = h or self._sprite.height
        super().__init__(x, y, w, h)
        # self.collision_scale = 0.8


    @property
    def w(self):
        return self._sprite.width
    
    @w.setter
    def w(self, w):
        self._sprite.scale_x =  w / self.img.width

    @property
    def h(self):
        return self._sprite.height
    
    @h.setter
    def h(self, h):
        self._sprite.scale_y =  h / self.img.height

    @property
    def src(self):
        return self._src
    
    @src.setter
    def src(self, src):
        if src not in cache_images:
              img = pyglet.image.load(rss.get(src))
              self.center_image(img)
              cache_images[src] = img

        self._src = src
        self.img = cache_images[src]
        self._sprite = pyglet.sprite.Sprite(img=self.img)

    @property
    def x(self):
        return self._sprite.x

    @x.setter
    def x(self, x):
        self._sprite.x = x

    @property
    def y(self):
        return self._sprite.y

    @y.setter
    def y(self, y):
        self._sprite.y = y

    @property
    def opacity(self):
        return self._sprite.opacity / 255

    @opacity.setter
    def opacity(self, opacity):
        self._sprite.opacity = int(opacity * 255)

    def center_image(self, img):
        """Sets an image's anchor point to its center"""
        img.anchor_x = img.width // 2 # int
        img.anchor_y = img.height // 2 # int

    def update_points(self):
        min_x = self.x - self.w/2
        min_y = self.y - self.h/2
        max_x = self.x + self.w/2
        max_y = self.y + self.h/2
        self.points = (min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y)

    def draw(self):
        self.update_all()
        self._sprite.draw()

    def delete(self):
        self._sprite.delete()
