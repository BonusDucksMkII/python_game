import arcade
import arcade.key
import pyglet.math as math
import pyglet.canvas as canvas
import pyglet.font as font

import ball
import physics

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'test'

TILE_SIZE = 128
TILE_CENTER = int(TILE_SIZE / 2)

ROTATION_SPEED = 2

class newGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.scene = None
        self.player_sprite = None
  
        self.player = None

        self.physics_engine = None

        self.right_press= False
        self.left_press = False


        arcade.set_background_color((80, 160, 255))

    def test(self):
        x = 0.0
        self.coordinate_list = []
        self.delta_x, self.delta_y = 1024.0, 0.0
        while x <= 1024.0:
            self.coordinate_list.append([x, 0.0])
            x += 128.0

    def draw_stage(self):
        for co in self.coordinate_list: 
            self.tile = arcade.Sprite(filename="assets/tiles/tile.png")
            # Forward half a tile
            self.tile.center_x = co[0] + TILE_CENTER
            self.tile.center_y = co[1] + TILE_CENTER
            self.scene.add_sprite("Tiles", self.tile)
        self.clear()

    def setup(self):
        # set up game variables here
        self.scene = arcade.Scene()

        self.player = ball.Ball("assets/ball/ball1.png", math.Vec2(32, TILE_SIZE + 32), 8)

        self.physicsObjectList = [self.player]
        
        # Use spatial hash for collision?
        self.stage = arcade.SpriteList(use_spatial_hash=True, spatial_hash_cell_size=TILE_SIZE)

        self.scene.add_sprite_list("Tiles", self.stage)

        arcade.load_font("assets/fonts/Arcadepix_Plus.ttf")
        try:
            self.debug = arcade.Text(
                text="",
                start_x=10, start_y=784,
                color=arcade.color.WHITE,
                font_size=16,
                width=0,
                align="left",
                font_name="Arcadepix_Plus.ttf",
                anchor_x="left",
                anchor_y="top"
            )
        except:
            self.debug = arcade.Text(
                text="",
                start_x=-640, start_y=400,
                color=arcade.color.WHITE,
                font_size=16,
                width=0,
                align="left",
                font_name="arial.ttf",
                anchor_x="left",
                anchor_y="top"
            )

        """
        TODO:
        1. Create calculations for tiles to fall along a line at center point of tiles
            Need a vector, or line??
        2. Override physics_engine class methods to create step along, or calculations for slope velocity
            Learn the math for that
        """
        self.test()
        self.draw_stage()

    def on_draw(self):
        # render viewport
        self.clear()
        self.scene.draw()
        self.player.sprite.draw()
        self.debug.draw()

    def on_update(self, delta_time):
        self.collided = arcade.check_for_collision_with_list(self.player.sprite, self.stage, 1)
        if self.player.sprite in self.collided:
            print("true")

        if self.right_press: self.player.accel(math.Vec2(0.1, 0))
        if self.left_press: self.player.accel(math.Vec2(-0.1, 0))

        physics.update_objects(self.physicsObjectList)
        self.debug.text = f'{self.player._velocity.x:.2f}'
    
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.right_press = True
        if key == arcade.key.LEFT:
            self.left_press = True
        if key == arcade.key.R:
            self.player.position = math.Vec2(32, TILE_SIZE + 32)
            self.player.set_velocity(math.Vec2(0, 0))

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.right_press = False
        if key == arcade.key.LEFT:
            self.left_press = False

def main():
    # print(TILE_SIZE)
    # display = canvas.get_display()
    # screen = display.get_screen()
    # screen.width, screen.height
    game = newGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()