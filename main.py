import arcade
import pyglet
import ball

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

        arcade.set_background_color((0, 0, 0))

    def setup(self):
        # set up game variables here

        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        # Use spatial hash for collision?
        self.scene.add_sprite_list("Tiles", use_spatial_hash=True)

        self.player = ball.Ball(40, 160, "assets/ball/ball1.png", (0.0, 0.0))

        self.scene.add_sprite("Player", self.player.current_sprite)

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