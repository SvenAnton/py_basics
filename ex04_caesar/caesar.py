"""Encode and decode Caesar cipher."""


def renumber(length: int, alphabet: str):
    """"Aitab taandada olukordi juhul, kui shift v6i shiftitav number on suuremad t2hestikust v6i alla nulli."""
    if length < 0:
        return len(alphabet) - abs(length) % len(alphabet)
    elif length > len(alphabet):
        return length % len(alphabet)
    else:
        return length


def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    renumber(shift, alphabet)
    message_list = list(message)
    i = 0

    for char in message_list:
        if char.upper() in alphabet.upper():
            if char.isupper():
                message_list[i] = alphabet[renumber(alphabet.upper().find(char) + shift, alphabet)].upper()
            else:
                message_list[i] = alphabet[renumber(alphabet.find(char) + shift, alphabet)]
        else:
            message_list[i]
        i += 1
    return "".join(message_list)


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    renumber(shift, alphabet)
    message_list = list(message)
    i = 0

    for char in message_list:
        if char.upper() in alphabet.upper():
            if char.isupper():
                message_list[i] = alphabet[renumber(alphabet.upper().find(char) + shift, alphabet)].upper()
            else:
                message_list[i] = alphabet[renumber(alphabet.find(char) + shift, alphabet)]
        else:
            message_list[i]
        i += 1
    return "".join(message_list)
