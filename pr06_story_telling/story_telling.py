"""Collect story parts from a messy text."""


import re


def read_file(file) -> str:
    """
    Read the text from given file into string.

    :param file: file path
    :return: string
    """
    with open(file, "r") as file:
        return get_clean_text(file.read())


def get_clean_text(messy_text: str) -> str:
    """
    Process given text, remove unneeded symbols and retrieve a story.

    :param messy_text: string
    :return: clean string
    """
    for match in re.finditer(r"[1234567890&@#$%^()_+|><~]", messy_text):
        messy_text = list(messy_text)
        del_index = messy_text.index(match.group())
        del(messy_text[del_index])

    messy_text[0] = messy_text[0].upper()

    for index, char in enumerate(messy_text):
        try:
            if char == '.':
                messy_text[index + 2] = messy_text[index + 2].upper()
        except IndexError:
            continue

        if char == "*":
            messy_text[index] = '"'
            messy_text[index + 1] = messy_text[index + 1].upper()
        if char == "!":
            messy_text[index] = "?"
            messy_text[index + 2] = messy_text[index + 2].upper()
        if char == "?":
            messy_text[index] = "!"
            messy_text[index + 2] = messy_text[index + 2].upper()
        if char == "/":
            messy_text[index] = ","

    return "".join(messy_text)
