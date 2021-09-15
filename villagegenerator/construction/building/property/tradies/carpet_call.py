from tradies.tradie import Tradie

class CarpetCall(Tradie):
    trade = 'carpeting'
    def __init__(self):
        pass

# TESTING

if __name__ == '__main__':
    carpet_guy = CarpetCall()
    print(carpet_guy.msg)