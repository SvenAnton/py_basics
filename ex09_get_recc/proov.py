

def traversable_coordinates(world_map: list, coord: tuple = (0, 0), traversable_coords: set = None) -> set:
    """
    Return the coordinates that are traversable by humans or adjacent to traversable coordinates.

    Given a two-dimensional list as a map, give the coordinates of traversable cells with the
    coordinates of cells which are adjacent to traversable cells with respect to the
    beginning coordinate.

    If there is not a traversable path from the beginning coordinate
    to the traversable cell, the traversable cell coordinate is not returned. Traversable
    cells are represented by empty strings. If the beginning coordinate cell is not traversable,
    return empty set.

    Coordinates are in the format (row, column). Negative coordinate values are considered invalid.
    world_map is not necessarily rectangular. Paths can be made through a diagonal.

    traversable_coordinates([]) == set()
    traversable_coordinates([[]]) == set()
    traversable_coordinates([["", "", ""]], (5, 2)) == set()
    traversable_coordinates([["1", "1", ""]], (-4, -9)) == set()
    traversable_coordinates([["1", [], "1"]], (0, 1)) == set()

    world = [["1", "1", "1", "1", "1"],
             ["1", "1", "1",  "", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1", "1", "1", "1"]]

    traversable = {(0, 2), (0, 3), (0, 4),
                   (1, 1), (1, 2), (1, 3), (1, 4),
                   (2, 1), (2, 2), (2, 3), (2, 4),
                   (3, 1), (3, 2), (3, 3),
                   (4, 1), (4, 2), (4, 3)}

    traversable_coordinates(world, (2, 2)) == traversable

    :param world_map: two-dimensional list of strings.
    :param coord: the (beginning) coordinate.
    :param traversable_coords: helper to store traversable coordinates.
    :return: set of traversable and traversable-adjacent cell
            coordinate tuples with respect to starting coord
    """
    pass
