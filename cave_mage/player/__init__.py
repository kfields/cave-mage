import cave_mage.globe
import cave_mage.objects.coin
import cave_mage.characters.butterfly
import cave_mage.objects.flag

class Player:
    def __init__(self):
        cave_mage.globe.player = self
        self.score = 0
        self.on_next_level()
        
    def on_next_level(self):
        self.has_green_flag = False
        self.has_yellow_flag = False
        self.has_red_flag = False
        self.level_beat = False

    def update(self, dt):
        pass

    def collect(self, item):
        if isinstance(item, cave_mage.objects.coin.Coin):
            return self.collect_coin(item)
        if isinstance(item, cave_mage.characters.butterfly.Butterfly):
            return self.collect_butterfly(item)
        elif isinstance(item, cave_mage.objects.flag.Flag):
            return self.collect_flag(item)

    def collect_coin(self, item):
        self.score +=1
        return True

    def collect_butterfly(self, item):
        self.score +=1
        return True

    def collect_flag(self, flag):
        success = False
        if isinstance(flag, cave_mage.objects.flag.FlagGreen) and not self.has_green_flag:
            success = self.has_green_flag = flag.collect()
        elif isinstance(flag, cave_mage.objects.flag.FlagYellow) and self.has_green_flag:
            success = self.has_yellow_flag = flag.collect()
        elif isinstance(flag, cave_mage.objects.flag.FlagRed) and self.has_yellow_flag:
            success = self.has_red_flag = flag.collect()

        self.level_beat = self.has_red_flag

        return success