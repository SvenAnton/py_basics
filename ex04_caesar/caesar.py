"""Encode and decode Caesar cipher."""


def renumber(index: int, alphabet: str):
    """"Aitab taandada olukordi juhul, kui shift v6i shiftitav number on suuremad t2hestikust v6i alla nulli."""
    if (index - 1) < 0:
        return len(alphabet) - abs(index) % len(alphabet)
    elif (index - 1) > (len(alphabet)):
        return index % len(alphabet)
    else:
        return index


def check_if_coded(shift: int, alphabet: str):
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
    message_list = list(message)

    for i in range(len(message_list)):
        if str(message_list[i]).upper() in alphabet.upper():
            if str(message_list[i]).isupper():
                message_list[i] = alphabet[renumber(alphabet.upper().find(message[i]) + shift, alphabet)].upper()
            else:
                message_list[i] = alphabet[renumber(alphabet.find(message[i]) + shift, alphabet)]
        else:
            message_list[i]
    return "".join(message_list)


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
    message_list = list(message)

    for i in range(len(message_list)):
        if str(message_list[i]).upper() in alphabet.upper():
            if str(message_list[i]).isupper():
                message_list[i] = alphabet[renumber(alphabet.upper().find(message[i]) - shift, alphabet)].upper()
            else:
                message_list[i] = alphabet[renumber(alphabet.find(message[i]) - shift, alphabet)]
        else:
            message_list[i]
    return "".join(message_list)


if __name__ == "__main__":
    # simple tests
    print(encode("hello", -27))  # ifmmp
    print(decode("hello", 27))  # hello
