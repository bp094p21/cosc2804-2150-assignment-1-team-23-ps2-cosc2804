from mcpi import vec3 as v

if __name__ == '__main__':
    from tradie import Tradie      
else:
    from tradies.tradie import Tradie

class Roofer(Tradie):
    trade = 'roofing'
    roofs = []
    def build_component(self, roof, mc):
        self.roofs.append(roof)
        self._build_roof(self.roofs[-1], mc)
    def _build_roof(self, roof, mc):
        x_difference = int(roof.roof_v3['end'].x - roof.roof_v3['start'].x)
        z_difference = int(roof.roof_v3['end'].z - roof.roof_v3['start'].z)
        id = roof.stair_block.id
        slab = roof.slab_block
        cube = roof.cube_block
        abs(x_difference)
        abs(z_difference)
        for i in range(x_difference + 3):
            move_up_x = roof.roof_v3['start'].x - 1 + i
            if z_difference % 2 == 0:
                for j in range(int(z_difference / 2) + 1):
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z - 1 + j, id, 2)
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + 1 + z_difference - j, id, 3)
                    mc.setBlock(roof.roof_v3['start'].x - 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, id, 7)
                    mc.setBlock(roof.roof_v3['start'].x - 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, id, 6)   
                    mc.setBlock(roof.roof_v3['end'].x + 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, id, 7)
                    mc.setBlock(roof.roof_v3['end'].x + 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, id, 6)
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y + (z_difference / 2), roof.roof_v3['start'].z + (z_difference / 2), slab)       # SLAB
                    mc.setBlocks(roof.roof_v3['start'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, roof.roof_v3['start'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, cube)   # CUBE
                    mc.setBlocks(roof.roof_v3['end'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, roof.roof_v3['end'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, cube)        # CUBE
                    mc.setBlock(roof.roof_v3['start'].x - 1, roof.roof_v3['start'].y + (z_difference / 2) - 1, roof.roof_v3['start'].z + (z_difference / 2), id, 4)  
                    mc.setBlock(roof.roof_v3['end'].x + 1, roof.roof_v3['start'].y + (z_difference / 2) - 1, roof.roof_v3['start'].z + (z_difference / 2), id, 5)         
            else:
                for j in range(int(z_difference // 2) + 2):
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z - 1 + j, id, 2)
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + 1 + z_difference - j, id, 3)
                    mc.setBlock(roof.roof_v3['start'].x - 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, id, 7)
                    mc.setBlock(roof.roof_v3['start'].x - 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, id, 6)   
                    mc.setBlock(roof.roof_v3['end'].x + 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, id, 7)
                    mc.setBlock(roof.roof_v3['end'].x + 1, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, id, 6)
                    mc.setBlocks(roof.roof_v3['start'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, roof.roof_v3['start'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, cube)   # CUBE
                    mc.setBlocks(roof.roof_v3['end'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, roof.roof_v3['end'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, cube)        # CUBE
                               
class Freddie(Roofer):
    name = 'Freddie'
    pass

if __name__ == '__main__':

    import sys
    sys.path.append('../property')
    from components import roof as r
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    start_v3 = mc.player.getPos()
    end_v3 = v.Vec3(start_v3.x + 3, start_v3.y, start_v3.z+ 3)
    roof = r.Roof(start_v3, end_v3)
    roof_guy = Freddie()
    roof_guy.build_component(roof, mc)
    print(dir())

