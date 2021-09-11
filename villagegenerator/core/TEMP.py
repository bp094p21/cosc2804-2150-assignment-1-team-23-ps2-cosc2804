import numpy as np


def generate_fixed_ordinates(max_z: int, max_x: int, x_coord: int, y_coord: int, z_coord: int) -> list:
    temp = []
    for z in range(0, max_z + 1):
        for x in range(0, max_x + 1):
            temp.append((x_coord + x * 15, y_coord, z_coord + z * 15))

    return temp


FIXED_ORDINATES = generate_fixed_ordinates(12, 6, *(4, 5, 6))

if __name__ == '__main__':
    # generate the grid ordinates
    # for z in range(0, 13):
    #     for x in range(0, 7):
    #         print('(X + ' + str(x * 15) + ', Y, Z + ' + str(z * 15) + ')', end=', ')
    #
    #     print()

    print(FIXED_ORDINATES)
