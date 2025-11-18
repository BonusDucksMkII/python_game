import arcade
import physics

class Ball(physics.physicsObject):
    def __init__(self, sprite, position, top_speed):
        self.sprite = arcade.Sprite(filename=sprite, center_x=position.x, center_y=position.y)
        super().__init__(position, top_speed)