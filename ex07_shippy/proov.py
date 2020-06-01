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


if __name__ == '__main__':
    space_list1 = [
        "#www-",
        "wXw#-",
    ]
    flight_plan1 = ["N", "E", "E", "S", "E"]
    print("\n".join(simulate(space_list1, flight_plan1)))
    print(list_to_dictionary_converter(flight_plan1))

    # #---X
    # w-w#-

    assert simulate(space_list1, flight_plan1) == ["#---X", "w-w#-"]

    print()

    space_list2 = [
        "WWWW",
        "-wwW",
        "X-#W",
    ]

    flight_plan2 = ["N", "N", "E", "E", "S", "W", "W", "S", "E", "E"]
    print("\n".join(simulate(space_list2, flight_plan2)))

    # wwwW
    # ---W
    # -X#W

    assert simulate(space_list2, flight_plan2) == ["wwwW", "---W", "-X#W"]

    assert list_to_dictionary_converter(["-"]) == ({(0, 0): "-"}, 0, 0)
    assert list_to_dictionary_converter(['W#', '-X']) == ({(0, 0): 'W', (0, 1): '#', (1, 0): '-', (1, 1): '-'}, 1, 1)

    assert list_to_dictionary_converter(
        world_map=space_list1
    ) == ({(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): '-', (1, 2): 'w',
           (1, 3): '#', (1, 4): '-'}, 1, 1)

    assert dictionary_to_list_converter(
        {(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): 'X', (1, 2): 'w',
         (1, 3): '#', (1, 4): '-'}, 5, 2) == space_list1

    assert dictionary_to_list_converter({(0, 0): "X"}, 1, 1) == ["X"]
