"""Create schedule from the given file."""

import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(output_filename, "w") as output_file:
        with open(input_filename, "r") as input_file:
            output_file.write(create_schedule_string(input_file.read()))


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    # teen dictionary sisse antud tekstist.
    table = []
    schedule = {}

    for match in re.finditer(r"( +|\n)([0-1]\d|[2][0-3]|\d)(\D)([0-5]\d|\d)( +|\n +)([a-zA-Z]+)", input_string):
        if int(match.group(4)) < 10:
            minutes = f"0{int(match.group(4))}"
        else:
            minutes = f"{int(match.group(4))}"

        hour = int(match.group(2))

        if hour < 12:  # eristab AM ja PM tunni j2rgi
            time = f"{hour:>2}:{minutes} AM"
        else:
            time = f"{hour - 12:>2}:{minutes} PM"

        schedule.setdefault(time, set())
        schedule[time].add(match.group(6).lower())

    if bool(schedule) is False:
        return(
            "------------------\n"
            "|  time | items  |\n"
            "------------------\n"
            "| No items found |\n"
            "------------------")

    # teen parempoolse serva joondamise  muutuja
    length_right = set()
    for key, value in schedule.items():
        length_right.add(len(' ,'.join(value)))
    right_line = max(length_right)

    # teen vasakpoolse serva joonduse
    length_left = set()
    for key, value in schedule.items():
        length_left.add(len(key.strip()))
    left_line = max(length_left)

    # teen tabeli p2ise
    items_string = "items"
    time_string = "time"
    table.append("-" * (right_line + left_line + 7))
    table.append(f"|{time_string:>{left_line + 1}} | {items_string:<{right_line + 1}}|")
    table.append("-" * (right_line + left_line + 7))

    # teen dictionarist nõutud tabeli
    # sordib kõigepealt AM/PM järgi ja siis edasi vastava koha numbrite järgi.
    for time in sorted(schedule, key=lambda x: (x[6], x[0], x[1], x[3], x[4])):
        if int(time.split(":")[0]) == 0:
            table.append(
                f"|{time.replace('0', '12', 1):>{left_line + 1}} | {', '.join(schedule[time]):<{right_line + 1}}|")
        else:
            table.append(f"|{time:>{left_line + 1}} | {', '.join(schedule[time]):<{right_line + 1}}|")

    # tabeli alumine serv
    table.append("-" * (right_line + left_line + 7))
    return "\n".join(table)
