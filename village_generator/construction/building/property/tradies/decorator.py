if __name__ == '__main__':
    from tradie import Tradie      
else:
    from tradies.tradie import Tradie

class Decorator(Tradie):
    trade = 'decorating'