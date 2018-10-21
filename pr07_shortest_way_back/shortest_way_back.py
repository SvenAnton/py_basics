"""Find the shortest way back in a taxicab geometry."""

def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    liikumine = {"N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
    lat = 0
    long = 0
    way_back = ""

    for movement in path:
        if movement == "N":
            lat += liikumine["N"][0]
        if movement == "S":
            lat += liikumine["S"][0]
        if movement == "E":
            long += liikumine["E"][1]
        if movement == "W":
            long += liikumine["W"][1]

    while lat != 0 or long != 0:

        if lat > 0:
            way_back += "S"
            lat -= 1
        elif lat < 0:
            way_back += "N"
            lat += 1

        if long > 0:
            way_back += "W"
            long -= 1
        elif long < 0:
            way_back += "E"
            long += 1

    return way_back
