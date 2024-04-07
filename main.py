import arcade
import ball
import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'test'

TILE_SIZE = 128
TILE_CENTER = int(TILE_SIZE / 2)

class newGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.scene = None
        self.player_sprite = None

        self.player = None

        self.physics_engine = None

        arcade.set_background_color((80, 160, 255))

    def rotation(angle):
        theta = np.radians(angle)
        rotation = np.array((
                    (np.cos(theta), -np.sin(theta)), 
                    (np.sin(theta), np.cos(theta))
                    ))
        print(rotation)

    def test(self):
        self.coordinate_list = []
        self.delta_x, self.delta_y = 1024.0, 0.0
        for x in range(0.0, self.delta_x, float(TILE_SIZE)):
            self.coordinate_list.append([x, 0.0])
            print(self.coordinate_list) 

    def setup(self):
        # set up game variables here
        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        # Use spatial hash for collision?
        self.scene.add_sprite_list("Tiles", use_spatial_hash=True)

        self.player = ball.Ball(40, TILE_SIZE + 32, "assets/ball/ball1.png", (0.0, 0.0))

        self.angle = 0
        # Number of tiles to draw (will work out to be this multiplied by size of tiles)
        self.magnitude = 16

        # self.scene.add_sprite("Player", self.player.current_sprite)

        """
        TODO:
        1. Create calculations for tiles to fall along a line at center point of tiles
            Need a vector, or line??
        2. Override physics_engine class methods to create step along, or calculations for slope velocity
            Learn the math for that
        """
        self.test()

        for x in range(0, self.magnitude, 1):
            self.tile = arcade.Sprite(filename="assets/tiles/tile.png")
            # Forward half a tile
            self.tile.center_x = (x * TILE_SIZE) + TILE_CENTER
            self.tile.center_y = TILE_CENTER
            self.scene.add_sprite("Tiles", self.tile)

    def on_draw(self):
        # render viewport
        self.clear()
        
        self.scene.draw()
    
    def on_key_press(self, key, key_modifiers):

        pass

    def on_key_release(self, key, key_modifiers):
        pass

def main():
    # print(TILE_SIZE)
    game = newGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()