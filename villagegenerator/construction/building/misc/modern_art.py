from misc import Misc

class Art(Misc):
    def __init__(self) -> None:
        super().__init__()
    def build(self,x,y,z):
        self.build_foundation(x,y,z)
        #self.mc.setBlocks(x+3,y,z+7,x+11,y+15,z+7,self.stone)
    
park = Art()    
x,y,z = park._player_position()
park.build(x,y,z)
        