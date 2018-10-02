def renumber(length: int, alphabet: str):
    """"Aitab taandada olukordi juhul, kui shift v6i shiftitav number on suuremad t2hestikust v6i alla nulli."""
    if length < 0:
        return len(alphabet) - abs(length) % len(alphabet)
    elif length > len(alphabet):
        return length % len(alphabet)
    else:
        return length


def encode(message: str, shift: int, alphabet="abcdefghijklmnopqrstuvwxyz"):
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


if __name__ == "__main__":
    # simple tests
    print(encode("hello", 28))  # ifmmp
