from park import Park

class art(Park):
    def __init__(self) -> None:
        super().__init__()
    def make_art(self,x,y,z):
        self.build_foundation(x,y,z)
        #self.mc.setBlocks(x+3,y,z+7,x+11,y+15,z+7,self.stone)
    
park = art()    
x,y,z = park.player_position()
park.make_art(x,y,z)
        