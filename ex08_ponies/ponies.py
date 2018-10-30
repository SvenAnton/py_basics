"""EX08"""


import base64
import re


def decode(line: str) -> str:
    """Decodes given text to utf-8 format string type text."""
    return str(base64.b64decode(line)).replace("b", "", 1).replace("'", "")


def extract_information(line: str) -> dict:
    """Takes decoded line and returns it as a dictionary with structured info."""
    line = re.sub(" +", " ", line)
    pony_dict = {"name": " ".join(line.split(" ")[0:2]), "kind": str(line.split(" ")[2]),
                 "coat_color": str(line.split(" ")[3]), "mane_color": str(line.split(" ")[4]),
                 "eye_color": str(line.split(" ")[5]), "location": " ".join(line.split(" ")[6:])}
    return  pony_dict


def read(read_file: str) -> list:
    """Reads in given file, decodes lines and returns every line as a dictionary. Returns lines as a list."""
    ponies_list = []
    try:
        with open(read_file, "r") as input_file:
            for line in input_file:
                if "NAME" in decode(line):
                    continue
                elif "-" in decode(line):
                    continue
                else:
                    ponies_list.append(extract_information(decode(line)))
    except FileNotFoundError:
        print("File not found!")
        raise

    return ponies_list


def filter_by_location(ponies: list) -> list:
    """Filters out lines, where location is "None'."""
    return [pony for pony in ponies if not (pony["location"] == "None")]


def filter_by_kind(ponies: list, kind: str) -> list:
    """Filters ponies from list by given "kind" value as a string."""
    return [pony for pony in ponies if (pony["kind"] == kind)]


def get_points_for_color(color: str) -> int:
    """Returns points by given color nr. First color gives 10 points, 2nd 9 etc. Points under 5 are returend as None"""
    colors = [
        'magenta', 'pink', 'purple', 'orange', 'red', 'yellow', 'cyan', 'blue', 'brown', 'green'
    ]
    for col_nr, col in enumerate(colors):
        if col == color:
            points = 10 - col_nr
            if points < 5:
                return None
            else:
                return points


def add_points(pony: dict) -> dict:
    """Evaluates ponies by location and returns new dictionary with points added"""
    evaluation_locations = {
        'coat_color': ['Town Hall', 'Theater', 'School of Friendship'],
        'mane_color': ['Schoolhouse', 'Crusaders Clubhouse', 'Golden Oak Library'],
        'eye_color': ['Train station', 'Castle of Friendship', 'Retirement Village']
    }
    if pony["location"] in evaluation_locations["coat_color"]:
        pony["points"] = get_points_for_color(pony["coat_color"])
    elif pony["location"] in evaluation_locations["mane_color"]:
        pony["points"] = get_points_for_color(pony["mane_color"])
    elif pony["location"] in evaluation_locations["eye_color"]:
        pony["points"] = get_points_for_color(pony["eye_color"])
    else:
        return None

    return pony


def evaluate_ponies(ponies: list) -> list:
    """Adds evaluation points to list on pony dictionary"""
    for pony in ponies:
        add_points(pony)
    return ponies


def sort_by_name(ponies: list) -> list:
    return sorted(ponies, key=lambda pony: pony["name"])


def sort_by_points(ponies: list) -> list:
    ponies_list = []
    for pony in ponies:
        if pony["points"] == None:
            continue
        else:
            ponies_list.append(pony)

    return sorted(ponies_list, key=lambda p: p["points"], reverse=True)


def format_line(pony: dict, place: int) -> str:
    return f"{place:<10}{pony['points']:<10}{pony['name']:<20}{pony['kind']:<20}{pony['coat_color']:<20}" \
           f"{pony['mane_color']:<20}{pony['eye_color']:<20}{pony['location']}"


def write(input_file: str, kind: str):
    place_table = "PLACE"
    points_table = "POINTS"
    name_table = "NAME"
    kind_table = "KIND"
    coat_color = "COAT COLOR"
    mane_color = "MANE COLOR"
    eye_color = "EYE COLOR"
    location = "LOCATION"
    line = "-"

    ponies_list = sort_by_points(
        sort_by_name(evaluate_ponies(filter_by_kind(filter_by_location(read(input_file)), kind))))
    ponies_string = ""
    for place, pony in enumerate(ponies_list):
        ponies_string += f"{format_line(pony, place + 1)}\n"
    ponies_string = ponies_string.strip()


    with open(input_file, "r"):
        with open(f"results_for_{kind}.txt", "w") as output_file:
            output_file.write(f"{place_table:<10}{points_table:<10}{name_table:<20}{kind_table:<20}{coat_color:<20}"
                              f"{mane_color:<20}{eye_color:<20}{location}\n")
            output_file.write(f"{128 * line}\n")
            output_file.write(ponies_string)


if __name__ == '__main__':
    read("ponies1.txt")













