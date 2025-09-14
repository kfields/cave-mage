import sys
import os

import arcade

import cave_mage.globe
from cave_mage.constants import *
from cave_mage.assets import asset

from cave_mage.physics.dynamic import DynamicPhysicsEngine
from cave_mage.physics.kinematic import KinematicPhysicsEngine
from cave_mage.scene_layer import SceneLayer
from cave_mage.objects.barrier import BarrierLayer
from cave_mage.background import BackgroundLayer

from cave_mage.tile import TileLayer, TileFactory 

from cave_mage.characters.factory import CharacterFactory
from cave_mage.characters import Avatar

from cave_mage.objects.flag import FlagFactory
from cave_mage.characters.butterfly import ButterflyFactory
from cave_mage.effects.firework import Firework
from cave_mage.obstacle import ObstacleFactory
from cave_mage.objects.coin import CoinFactory

from cave_mage.level import StickerLevel

class Sandbox(StickerLevel):
    @classmethod
    def produce(self):
        level = Sandbox('sandbox')
        level.create()
        return level
        
    #next level
    def get_next_level(self):
        import cave_mage.scenes.level2
        return cave_mage.scenes.level2.Level2

    def do_setup(self):
        super().do_setup()

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.add_layer(BarrierLayer(self, 'barrier'))

        self.parallax_layer = self.add_layer(TileLayer(self, 'parallax'))

        self.background_layer = self.add_layer(TileLayer(self, 'background'))

        self.ground_layer = self.add_layer(TileLayer(self, 'ground', TileFactory))

        self.ground_layer = self.add_layer(TileLayer(self, 'foreground'))

        self.castle_layer = self.add_layer(TileLayer(self, 'castle'))

        self.castledeco_layer = self.add_layer(TileLayer(self, 'castledeco'))

        self.shading_layer = self.add_layer(TileLayer(self, 'shading'))

        #self.light_layer = self.add_layer(TileLayer(self, 'light'))
        self.light_layer = None

        self.obstacle_layer = self.add_layer(TileLayer(self, 'obstacle', ObstacleFactory))

        #self.flag_layer = flag_layer = self.add_animated_layer(TileLayer(self, 'flags', FlagFactory))
        self.flag_layer = None

        #self.ladder_layer = self.add_layer(TileLayer(self, 'ladder'))
        self.ladder_layer = None

        self.coin_layer = coin_layer = self.add_layer(TileLayer(self, 'coin', CoinFactory))

        #self.butterfly_layer = self.add_animated_layer(TileLayer(self, 'butterfly', ButterflyFactory))

        self.spark_layer = self.add_layer(SceneLayer(self, 'spark'))

        self.character_layer = character_layer = self.add_animated_layer(TileLayer(self, 'game', CharacterFactory))

        self.above_layer = self.add_layer(TileLayer(self, 'above'))
                
        # --- Other stuff
        # Set the background color
        if self.map.background_color:
            arcade.set_background_color(self.map.background_color)

        self.physics_engine.create()
