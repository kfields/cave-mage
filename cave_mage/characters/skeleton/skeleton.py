import arcade

from cave_mage.model import KinematicModel
from cave_mage.assets import asset

class SkeletonSprite(arcade.Sprite):
    def __init__(self, position):
        super().__init__(asset('stickers/skeleton.png'), center_x=position[0], center_y=position[1])

class Skeleton(KinematicModel):
    @classmethod
    def produce(self, position=(0,0)):
        sprite = SkeletonSprite(position)
        return Skeleton(position, sprite)
