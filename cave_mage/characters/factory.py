from loguru import logger
import glm

from cave_mage.characters import Avatar
from cave_mage.characters import Skateboard

# from cave_mage.characters import Blob
# from cave_mage.characters import Skeleton
from cave_mage.characters import Robot


kinds = {
    "PlayerCharacter": Avatar,
    "Skateboard": Skateboard,
    "Robot": Robot,
    # "hero": PlayerCharacter,
    #'blob': Blob,
    #'enemy': Skeleton,
    #'skeleton': Skeleton,
}
