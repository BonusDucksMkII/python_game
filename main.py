import arcade
import pyglet
import ball
import glob

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'test'

class newGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.scene = None
        self.player_sprite = None

        self.player = None

        self.physics_engine = None

        arcade.set_background_color((80, 160, 255))

    def setup(self):
        # set up game variables here

        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        # Use spatial hash for collision?
        self.scene.add_sprite_list("Tiles", use_spatial_hash=True)

        self.player = ball.Ball(40, 160, "assets/ball/ball1.png", (0.0, 0.0))

        self.delta = pyglet.math.Vec2(0.0, 0.0)

        # self.ball_sprites = glob.glob('assets/ball/*.png', recursive=True)
        # for sprite in self.ball_sprites:
       
        # self.scene.add_sprite("Player", self.player.current_sprite)

        """
        TODO:
        1. Create calculations for tiles to fall along a line at center point of tiles
            Need a vector, or line??
        2. Override physics_engine class to create step along, or calculations for slope velocity
            Learn the math for that
        """

        for x in range(64, 1088, 128):
            self.tile = arcade.Sprite(filename="assets/tiles/tile.png")
            self.tile.center_x = x
            self.tile.center_y = 64
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
    # print("Hello world!")
    game = newGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()