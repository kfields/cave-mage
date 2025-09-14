from crunge.engine.factory import ClassFactory

from crunge.engine.channel import PhysicsSceneChannel
from crunge.engine.d2.physics import DynamicPhysicsEngine

from ..cave_mage import CaveMage
from ..scenes.start import StartScene
from ..screens.start_screen import StartScreen


class StartChannel(PhysicsSceneChannel):
    def __init__(self):
        super().__init__(
            ClassFactory(StartScreen),
            ClassFactory(StartScene),
            ClassFactory(DynamicPhysicsEngine),
            "start",
            "Start",
        )


def install(app: CaveMage):
    app.add_channel(StartChannel())
