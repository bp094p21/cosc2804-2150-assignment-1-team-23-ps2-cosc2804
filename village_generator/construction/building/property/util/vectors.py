from mcpi import vec3 as v

def orientate(v3, orientation=0, z_offset=0, x_offset=0):
    """Returns new Vec3 object with absolute positioning for specified orientation"""
    orientated_v3 = None
    if orientation == 0:
        orientated_v3 = v.Vec3(v3.x + x_offset, v3.y, v3.z + z_offset)
    elif orientation == 1:
        orientated_v3 = v.Vec3(v3.x - z_offset, v3.y, v3.z + x_offset)
    elif orientation == 2:
        orientated_v3 = v.Vec3(v3.x - x_offset, v3.y, v3.z - z_offset)
    elif orientation == 3:
        orientated_v3 = v.Vec3(v3.x + z_offset, v3.y, v3.z - x_offset)
    return orientated_v3