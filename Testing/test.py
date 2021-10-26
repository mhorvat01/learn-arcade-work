import arcade

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800


def background():
    """ Draw the background """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.AQUA)
    arcade.draw_circle_filled(120, 600, 100, arcade.csscolor.ORANGE_RED)
    arcade.draw_circle_filled(800, 700, 70, arcade.csscolor.DARK_SLATE_GRAY)
    arcade.draw_circle_filled(1200, 700, 50, arcade.csscolor.YELLOW)
def star(x,y):
    """ This will draw stars """
    arcade.draw_circle_filled(0 + x, 0 + y, 10, arcade.csscolor.WHITE)

def space_ship(x, y):
    """ This is a spaceship drawing, it will print a spaceship. """

    # Body of Ship
    arcade.draw_circle_filled(100 + x, 400 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_arc_filled(100 + x, 300 + y, 300, 200, arcade.csscolor.GRAY, 0, 180)
    arcade.draw_arc_filled(100 + x, 280 + y, 380, 150, arcade.csscolor.GREEN, 0, 180)
    # Windows of Ship
    arcade.draw_circle_filled(100 + x, 315 + y, 30, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(20 + x, 315 + y, 20, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(180 + x, 315 + y, 20, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(-60 + x, 315 + y, 15, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(260 + x, 315 + y, 15, arcade.csscolor.WHITE)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()
    background()
    star(900, 750)
    star(1000, 550)
    star(1200, 600)
    star(200, 400)
    star(400, 700)
    star(600, 600)
    star(300, 500)
    space_ship(on_draw.space_ship1_x, 1)
    on_draw.space_ship1_x += 3

on_draw.space_ship1_x = 1


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()


