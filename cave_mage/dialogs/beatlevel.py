import os

import cave_mage.level_controller

from cave_mage.scene import Scene
import cave_mage.dialog


class Controller(cave_mage.level_controller.LevelController):
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            cave_mage.app.scene.close_dialog()


class BeatLevelDialog(cave_mage.dialog.Dialog):
    def __init__(self, next_level=None):
        super().__init__("beatlevel")
        self.next_level = next_level
        self.width = cave_mage.app.game.width
        self.height = cave_mage.app.game.height
        self.half_width = self.width / 2
        self.half_height = self.height / 2
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def add_buttons(self):
        width = 200
        height = 50
        next_button = gui.UIFlatButton(0, 0, width, height, "Next")

        @next_button.event("on_click")
        def submit(x):
            cave_mage.app.scene.close_dialog()
            cave_mage.app.game.show_scene(self.next_level)

        quit_button = gui.UIFlatButton(0, 0, width, height, "Quit")

        @quit_button.event("on_click")
        def submit(x):
            import cave_mage.globe

            cave_mage.globe.scene.close_dialog()
            import cave_mage.scenes.start

            cave_mage.globe.game.show_scene(cave_mage.scenes.start.StartScene)

        self.ui_manager.add(
            gui.UIAnchorLayout(
                children=[gui.UIBoxLayout(children=[next_button, quit_button], space_between=20)]
            )
        )

    def _create(self):
        super()._create()
        self.add_buttons()

    def draw(self):
        super().draw()
        arcade.draw_text(
            "BadWing",
            self.center_x,
            self.center_y + 100,
            arcade.color.WHITE,
            60,
            font_name="Verdana",
            align="center",
            width=300,
        )
