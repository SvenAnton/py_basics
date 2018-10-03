"""Encode and decode Caesar cipher."""


def renumber(index: int, alphabet: str):
    """"Aitab taandada olukordi juhul, kui shift v6i shiftitav number on suuremad t2hestikust v6i alla nulli."""
    max_index = len(alphabet)

    if index < 0:
        if abs(index) % max_index == 0:
            return 0
        else:
            return max_index - abs(index) % max_index
    elif index >= max_index:
        return index % max_index
    else:
        return index


def check_if_coded(shift: int, alphabet: str):
    """"Kontrollin, kas tekst on yldse kodeeritud. Kui alphabet v6i shif on 0, siis v2ljastab sama teksti."""
    if alphabet == "" or shift == 0:
        return True


def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    if check_if_coded(shift, alphabet):
        return message

    shift = shift % len(alphabet)
    message = list(message)


    for i in range(len(message)):
        if str(message[i]).upper() in alphabet.upper():
            if str(message[i]).isupper():
               # print(
                  #  f"{message[i]} t2hestikus {alphabet.find(message[i])}. kohal. Pluss shift {shift} ja saame {alphabet.find(message[i]) + shift} tekib {renumber(alphabet.find(message[i]) + shift, alphabet)}")
                message[i] = alphabet[renumber(alphabet.upper().find(message[i]) + shift, alphabet)].upper()
            else:
                message[i] = alphabet[renumber(alphabet.find(message[i]) + shift, alphabet)]
        else:
            message[i]
    return "".join(message)


def decode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    if check_if_coded(shift, alphabet):
        return message

    renumber(shift, alphabet)
    message = list(message)

    for i in range(len(message)):
        if str(message[i]).upper() in alphabet.upper():
            if str(message[i]).isupper():
                print(
                  f"{message[i]} t2hestikus {alphabet.upper().find(message[i])}. kohal. Miinus shift {shift} v6rdub "
                  f"{alphabet.upper().find(message[i]) - shift} ja renumereerimisel {renumber(alphabet.upper().find(message[i]) - shift, alphabet)}")
                message[i] = alphabet[renumber(alphabet.upper().find(message[i]) - shift, alphabet)].upper()
            else:
                message[i] = alphabet[renumber(alphabet.find(message[i]) - shift, alphabet)]
        else:
            message[i]
    return "".join(message)
