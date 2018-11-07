"""Make life easier whilst volunteering in a French language camp."""


def count_portions(number_of_participants: int, day: int) -> int:
    """
    Count the total of portions served to participants during the camp recursively.

    There are 4 meals in each day and we expect that every participant eats 1 portion
    per meal. At the end of each day one participant leaves the camp and is not ours to
    feed.

    We are only counting the participants' meals, the organisers and volunteers
    eat separately. In case of negative participants or days the number of meals is
    still 0.

    :param number_of_participants: the initial number of participants.
    :param day: the specified day.
    :return: a total of portions served during the camp at the end of the specified day.
    """
    if number_of_participants <= 0 or day <= 0:
        return 0
    if day == 1:
        return number_of_participants * 4

    return number_of_participants * 4 + count_portions(number_of_participants - 1, day - 1)


def names_to_be_eliminated(points_dict: dict, names: set = None, lowest_score: int = None) -> set:
    """
    Recursively find the names that are to be eliminated.

    When two or more people have the same lowest score, return a list in which every lowest
    scoring person is listed.

    :param points_dict: dictionary containing name strings as
                        keys and points integers as values.
    :param names: helper to store current names
    :param lowest_score: helper to store current lowest score
    :return: set of names of lowest scoring people.
    """
    if names is None:
        names = set()
    else:
        names = names

    if len(points_dict) == 0:
        return names

    if lowest_score is None:
        lowest_score = list(points_dict.values())[0]
        for name, points in points_dict.items():
            if points <= lowest_score:
                lowest_score = points
    else:
        lowest_score = lowest_score

    first_name_in_dict = list(points_dict.keys())[0]
    first_value_in_dict = list(points_dict.values())[0]

    if first_value_in_dict == lowest_score:
        names.add(first_name_in_dict)
    names_to_be_eliminated({i: points_dict[i] for i in points_dict if i != first_name_in_dict}, names, lowest_score)

    return "".join(names) if len(names) < 2 else list(names)


def people_in_the_know(hours_passed) -> int:
    """
    Return the number of people who know a rumor given the hours passed from the initial release.

    Every hour there is a recess where everybody can talk to everybody. Rumors always spread in
    the same fashion: everybody who are in the know are silent one recess after the recess they
    were told of the rumor. After that they begin to pass it on, one person per recess.

    people_in_the_know(0) == 0
    people_in_the_know(1) == 1
    people_in_the_know(2) == 1
    people_in_the_know(3) == 2
    people_in_the_know(4) == 3
    people_in_the_know(7) == 13

    :param hours_passed: the hours passed from the initial release.
    :param cache: helper to store already calculated results.
    :return: the number of people that have heard the rumor.
    """
    if hours_passed == 0:
        return 0
    elif hours_passed == 1:
        return 1

    return people_in_the_know(hours_passed - 1) + people_in_the_know(hours_passed - 2)
