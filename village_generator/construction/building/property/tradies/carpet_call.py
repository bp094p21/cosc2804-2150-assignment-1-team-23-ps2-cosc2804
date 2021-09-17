from tradies.tradie import Tradie

class CarpetCall(Tradie):
    trade = 'carpeting'

# TESTING

if __name__ == '__main__':
    carpet_guy = CarpetCall()
    print(carpet_guy.msg)