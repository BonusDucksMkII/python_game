import arcade

class tile:
    def __init__(self, sprite, position):
        self.sprite = arcade.Sprite(filename=sprite, center_x=position.x, center_y=position.y)
        # access 1st and 3rd elements of hitbox PointList
        self.sprite.hit_box