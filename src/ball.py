import arcade
import physics
import pyglet.math as math

class Ball(physics.physicsObject):
    def __init__(self, sprite, position, top_speed):
        self.radius = 32
        self.sprite = arcade.Sprite(filename=sprite, center_x=position.x, center_y=position.y)
        super().__init__(position, top_speed)

    @property
    def radius(self):
        return self._radius

    @property
    def sdf(self):
        return self.position.mag - self.radius