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
                """------------------
|  time | items  |
------------------
| No items found |
------------------""")

    # teen vasakpoolse serva joondamise muutuja
    set_length = set()
    for key, value in schedule.items():
        set_length.add(len(' ,'.join(value)))

    left_line = max(set_length)

    # teen tabeli p2ise
    items_string = "items"
    table.append("-" * (left_line + 15))
    table.append(f"|     time | {items_string:<{left_line}} |")
    table.append("-" * (left_line + 15))

    # teen dictionarist nõutud tabeli
    # sordib kõigepealt AM/PM järgi ja siis edasi vastava koha numbrite järgi.
    for time in sorted(schedule, key=lambda x: (x[6], x[0], x[1], x[3], x[4])):
        if int(time.split(":")[0]) == 0:
            table.append(
                f"| {time.replace(' ', '', 1).replace('0', '12', 1)} | {', '.join(sorted(schedule[time])):<{left_line}} |")
        else:
            table.append(f"| {time} | {', '.join(sorted(schedule[time])):<{left_line}} |")

    # tabeli alumine serv
    table.append("-" * (left_line + 15))
    return "\n".join(table)
