if __name__ == '__main__':
    from tradie import Tradie      
else:
    from tradies.tradie import Tradie

class Decorator(Tradie):
    trade = 'decorating'
    def build_component(self, component, mc):
        if component.type == 'bed':
            self._build_bed(component, mc)
    def _build_bed(self, bed, mc):
        self._one_block(bed.v3, bed.block, mc)