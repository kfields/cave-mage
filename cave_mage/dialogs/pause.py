import cave_mage.globe
import cave_mage.level_controller
import cave_mage.dialog


class Controller(cave_mage.level_controller.LevelController):
    def on_key_press(self, key, modifiers):
        pass


class PauseDialog(cave_mage.dialog.Dialog):
    def __init__(self):
        super().__init__("pause")
        self.width = cave_mage.globe.game.width
        self.height = cave_mage.globe.game.height
        self.half_width = self.width / 2
        self.half_height = self.height / 2
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def add_buttons(self):
        width = 200
        height = 50
        resume_button = gui.UIFlatButton(0, 0, width, height, "Resume")

        @resume_button.event("on_click")
        def submit(x):
            cave_mage.globe.scene.close_dialog()

        quit_button = gui.UIFlatButton(0, 0, width, height, "Quit")

        @quit_button.event("on_click")
        def submit(x):
            self.close()
            import cave_mage.scenes.start

            cave_mage.app.game.show_scene(cave_mage.scenes.start.StartScene)

        self.ui_manager.add(
            gui.UIAnchorLayout(
                children=[
                    gui.UIBoxLayout(
                        children=[resume_button, quit_button], space_between=20
                    )
                ]
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
        )
