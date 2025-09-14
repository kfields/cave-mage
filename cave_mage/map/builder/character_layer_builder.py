from loguru import logger

import crunge.engine.loader.tiled.builder as tiled_builder
from crunge.engine.loader.tiled.builder import DefaultObjectBuilder

from cave_mage.characters import Avatar
from cave_mage.characters import Skateboard

# from cave_mage.characters import Blob
# from cave_mage.characters import Skeleton
from cave_mage.characters import Robot


class CharacterLayerBuilder(tiled_builder.DefaultObjectGroupBuilder):
    def __init__(self, context: tiled_builder.BuilderContext):
        def create_node_cb(position, rotation, scale, sprite, properties: dict):
            logger.debug(f"create_node_cb: {position}, {sprite}, {properties}")
            kind = properties.get("type")
            if not kind:
                logger.debug(f"kind not found: {kind}")
                return
            node = kinds[kind].produce(position)
            logger.debug(f"node: {node}")
            return node


        super().__init__(context, object_builder=DefaultObjectBuilder(context, create_node_cb=create_node_cb))

kinds = {
    "PlayerCharacter": Avatar,
    "Skateboard": Skateboard,
    "Robot": Robot,
    # "hero": PlayerCharacter,
    #'blob': Blob,
    #'enemy': Skeleton,
    #'skeleton': Skeleton,
}
