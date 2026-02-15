from pytmx import TiledImageLayer

from crunge.engine.math import Bounds2

from crunge.engine.loader.tiled.builder import BuilderContext

from crunge.engine.loader.tiled.builder.image_layer_builder import ImageLayerBuilder
from cave_mage.background import BackgroundLayer


class BackgroundLayerBuilder(ImageLayerBuilder):
    def build(self, tmx_layer: TiledImageLayer):
        path = tmx_layer.get_image_path()
        layer = BackgroundLayer(
            "background", path
        )

        size = self.context.size
        layer.bounds = Bounds2(0, 0, size.x, size.y)
        self.context.push_layer(layer)
        super().build(tmx_layer)
        self.context.pop_layer()
        self.context.current_layer_group.add_layer(layer)
