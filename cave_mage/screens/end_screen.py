from crunge import imgui

from crunge.engine import Renderer, Scheduler

import cave_mage.globe
from cave_mage.constants import *
from cave_mage.level import Level

from .scene_screen import SceneScreen

class EndScreen(SceneScreen):
    def __init__(self, scene: Level):
        super().__init__(scene)

    def _draw(self):
        imgui.begin("Main")

        if imgui.button("Start"):
            cave_mage.globe.game.show_channel("level1")

        if imgui.button("Quit"):
            #exit()
            Scheduler().schedule_once(lambda dt: exit(), 0)

        imgui.end()
        super()._draw()
