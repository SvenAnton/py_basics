"""Simulation."""
from typing import Tuple


def simulate(world_map: list, flight_plan: list) -> list:
    """
    Simulate a flying space ship fighting space pirates.

    :param world_map: A list of strings indicating rows that make up the space map.
                 The space map is always rectangular and the minimum given size is 1x1.
                 Space pirate free zone is indicated by the symbol ('-'), low presence by ('w') and high presence by ('W').
                 The ship position is indicated by the symbol ('X'). There is always one ship on the space map.
                 Asteroid fields are indicated by the symbol ('#').

    :param flight_plan: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the ship out of bounds or crash it into an asteroid field.

    :return: A list of strings indicating rows that make up the space map. Same format as the given wmap.

    Pirates under Shippy's starting position are always eliminated ('-').
    If Shippy fights pirates in high presence area, it first turns into low presence ('w')
     and then from low presence into no presence area ('-').
    """
    start_pos_y = list_to_dictionary_converter(world_map)[1]
    start_pos_x = list_to_dictionary_converter(world_map)[2]
    space_dict = list_to_dictionary_converter(world_map)[0]

    set_y_cord = set()
    set_x_cord = set()

    for key in space_dict.keys():
        set_y_cord.add(key[0])
        set_x_cord.add(key[1])

    width = max(set_x_cord) + 1
    height = max(set_y_cord) + 1

    for direction in flight_plan:
        try:
            if direction == "N":
                if space_dict[(start_pos_y - 1, start_pos_x)] != '#':
                    start_pos_y -= 1
            elif direction == "S":
                if space_dict[(start_pos_y + 1, start_pos_x)] != '#':
                    start_pos_y += 1
            elif direction == "E":
                if space_dict[(start_pos_y, start_pos_x + 1)] != '#':
                    start_pos_x += 1
            elif direction == "W":
                if space_dict[(start_pos_y, start_pos_x - 1)] != '#':
                    start_pos_x -= 1
            else:
                continue
        except KeyError:
            continue

        if space_dict[(start_pos_y, start_pos_x)] == 'w':
            space_dict.update({(start_pos_y, start_pos_x): "-"})

        if space_dict[(start_pos_y, start_pos_x)] == 'W':
            space_dict.update({(start_pos_y, start_pos_x): "w"})

    space_dict.update({(start_pos_y, start_pos_x): "X"})

    return dictionary_to_list_converter(space_dict, width, height)

def list_to_dictionary_converter(world_map: list) -> Tuple[dict, int, int]:
    space_dict = {}
    ship_y = 0
    ship_x = 0

    for y_cord, row in enumerate(world_map):
        for x_cord, col in enumerate(row):
            if col == "X":
                ship_y = y_cord
                ship_x = x_cord
                col = "-"
            space_dict[y_cord, x_cord] = col
    return space_dict, ship_y, ship_x


def dictionary_to_list_converter(space_map: dict, width: int, height: int) -> list:
    space_list = []
    row_length = width - 1
    row = ""

    for cords, map_object in space_map.items():
        row += map_object
        if cords[1] == row_length:
            space_list.append(row)
            row = ""

    return space_list
