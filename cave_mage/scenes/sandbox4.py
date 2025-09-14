from cave_mage.level import StickerLevel

class Sandbox(StickerLevel):
    @classmethod
    def produce(self):
        level = Sandbox('sandbox4')
        level.create()
        return level
        
    #next level
    def get_next_level(self):
        import cave_mage.scenes.level2
        return cave_mage.scenes.level2.Level2
