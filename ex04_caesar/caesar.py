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

    for i in range(len(message)):
        if message[i].upper() in alphabet.upper():
            if message[i].isupper():
                message = message.replace(message[i], alphabet[
                    renumber(alphabet.upper().find(message[i]) + shift, alphabet)].upper(), 1)
            else:
                message = message.replace(message[i], alphabet[renumber(alphabet.find(message[i]) + shift, alphabet)],
                                          1)
        else:
            message
    return message


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    renumber(shift, alphabet)

    for i in range(len(message)):
        if message[i].upper() in alphabet.upper():
            if message[i].isupper():
                message = message.replace(message[i], alphabet[
                    renumber(alphabet.upper().find(message[i]) - shift, alphabet)].upper(), 1)
            else:
                message = message.replace(message[i], alphabet[renumber(alphabet.find(message[i]) - shift, alphabet)],
                                          1)
        else:
            message
    return message
