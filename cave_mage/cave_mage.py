import sys
import os

import importlib.resources

from loguru import logger

from crunge import imgui
from crunge.engine import Renderer
from crunge.engine import App
from crunge.engine.resource.resource_manager import ResourceManager

from cave_mage import __version__
import cave_mage.globe
from cave_mage.player import Player


class CaveMage(App):
    def __init__(self, debug=False):
        super().__init__(title="BadWing")
        cave_mage.globe.game = self
        self.debug = debug
        self.scene = None
        self.player = Player()

    def install(self, name):
        logger.debug(f"Installing: {name}")
        import importlib.util

        spec = importlib.util.find_spec(name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module, install = module, module.install
        install(self)
    
    def update(self, delta_time: float):
        self.player.update(delta_time)
        super().update(delta_time)


def main(debug=False, levelname="start"):
    resource_root = importlib.resources.path("cave_mage.resources", "")

    ResourceManager().add_path_variable("resources", resource_root)

    game = CaveMage(debug=debug)
    game.install("cave_mage.channels.start")
    game.install("cave_mage.channels.level1")
    game.show_channel(levelname)
    game.run()


if __name__ == "__main__":
    main()
