def recursive_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using recursion.
    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    if len(numbers) == 1:
        return numbers[0] if (numbers[0] % 2) == 0 else 0
    return numbers[0] + recursive_sum(numbers[1:]) if (numbers[0] % 2) == 0 else 0 + recursive_sum(numbers[1:])



def loop_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using loops.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number
    return sum


def loop_reverse(s: str) -> str:
    """Reverse a string using a loop.

    :param s: string
    :return: reverse of s
    """
    reversed_s = ""

    for index in range(len(s)):
        reversed_s += s[index - 1 - 2 * index]

    return reversed_s



def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    :param s: string
    :return: reverse of s
    """
    if len(s) == 1:
        return s
    return recursive_reverse(s[1:]) + s[0]
