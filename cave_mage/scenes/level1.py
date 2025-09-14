from cave_mage.level import TileLevel

class Level1(TileLevel):
    '''
    @classmethod
    def produce(self):
        level = Level1('level1')
        return level
    ''' 
    def get_next_level(self):
        import cave_mage.scenes.end
        return cave_mage.scenes.end.EndScene
