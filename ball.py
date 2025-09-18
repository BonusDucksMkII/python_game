import arcade
import physics

class Ball(physics.physicsObject):
    def __init__(self, sprite, x, y):
        super().__init__(self, x, y)
        self.current_sprite = arcade.Sprite(filename=sprite, center_x=x, center_y=y)

    # Further methods here