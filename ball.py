import arcade
import physics

class Ball(physics.physicsObject):
    def __init__(self, sprite, x, y, top_speed):
        self.sprite = arcade.Sprite(filename=sprite, center_x=x, center_y=y)
        super().__init__(x, y, top_speed)