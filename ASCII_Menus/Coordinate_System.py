COORD_Z = 0
COORD_Y = 1
COORD_X = 2


def coordinate_system(input_user: str, last_coord: list[int], limit_coord: list[int]):
    if input_user.upper() == "W":
        add_coord = (0, -1, 0)
    elif input_user.upper() == "S":
        add_coord = (0, 1, 0)
    elif input_user.upper() == "A":
        add_coord = (0, 0, -1)
    elif input_user.upper() == "D":
        add_coord = (0, 0, 1)
    else:
        coord_add = last_coord
        return coord_add

    for n in range(len(last_coord)):
        last_coord[n] += add_coord[n]

    last_coord[COORD_X] %= limit_coord[COORD_X]

    if last_coord[COORD_Y] < 0 or last_coord[COORD_Y] >= limit_coord[COORD_Y]:
        last_coord[COORD_Z] += add_coord[COORD_Y]

    last_coord[COORD_Y] %= limit_coord[COORD_Y]
    last_coord[COORD_Z] %= limit_coord[COORD_Z]

    return last_coord