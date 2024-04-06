import arcade
import pyglet.math

class Ball():
    def __init__(self, x, y, sprite, velocity):
        self.current_sprite = arcade.Sprite(filename=sprite, center_x=x, center_y=y)
        self.velocity = pyglet.math.Vec2(velocity)

    # Further methods here