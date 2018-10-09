"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    with open(file, 'r') as file:
        file_list = []
        for line in file:
            file_list.append(line)
        return file_list


def retrun_max_or_min_from_dict(file, dictionary, max_or_min: str):
    """"
    Tagastab minimaalse või maksimaalse väärtuse sõnastikust.

    :param file on sisseloatav .txt file
    :param dictionary on sõnastik, millest väärtust otsitakse
    :param min_or_max on funktsioon, mida kasutatakse. Väärtus tuleb anda stringina, sest ma ei
    osanud funktsiooni otse sisse kirjutada praegu. Väärtused on "max" või "min".
     """
    if max_or_min == "max":
        max_or_min_value = max(dictionary.values(), default=None)
    elif max_or_min == "min":
        max_or_min_value = min(dictionary.values(), default=None)
    else:
        return "max or min as a string not inserted properly"

    values_list = []
    for key in dictionary:
        if dictionary[key] == max_or_min_value:
            values_list.append(key)
    return values_list


def create_popular_hobbies_dict(file):
    """"Teeb populaarsetest hobidest sõnastiku.

    Tagastatava sõnastiku võti on hobi nimi ja väärtus hobi esinemise arv.
    Funktsioon võtab väärtusena sisseloetud faili.
    """
    hobbies_list = []
    for item in create_dictionary(file).values():
        for i in item:
            hobbies_list.append(i)

    hobbies_set = set(hobbies_list)
    hobbies_set_list = list(hobbies_set)

    hobbies_dict = {}
    for hb in hobbies_set_list:
        hobbies_dict[hb.rstrip()] = hobbies_list.count(hb)
    return hobbies_dict


def create_hobbies_per_person_nr_dict(file):
    """"Loob sõnastiku, kus iga inimese kohta on välja toodud tema hobid. Väärtusena võetakse fail."""
    hobbies_per_person = {}
    for key, val in create_dictionary(file).items():
        val = len(val)
        hobbies_per_person[key] = val
    return hobbies_per_person


def create_name_list(file):
    """"Loob nimede listi, kus nimed ei kordu. Võtab sisse loetava faili."""
    name_set = set()
    for i in create_list_from_file(file):
        name = i.split(":")[0]
        name_set.add(name)

    name_list = list(name_set)
    return name_list


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    file_dict = {}
    for name in create_name_list(file):
        dict_value = set()
        for line in create_list_from_file(file):
            if line.split(":")[0] == name:
                dict_value.add(line.split(":")[1].rstrip())
        file_dict[name] = list(dict_value)
    return file_dict


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    return retrun_max_or_min_from_dict(file, create_hobbies_per_person_nr_dict(file), "max")


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    return retrun_max_or_min_from_dict(file, create_hobbies_per_person_nr_dict(file), "min")


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    return retrun_max_or_min_from_dict(file, create_popular_hobbies_dict(file), "max")


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    return retrun_max_or_min_from_dict(file, create_popular_hobbies_dict(file), "min")


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        for key, value in sorted(create_dictionary(file).items()):
            writer.writerow([key, '-'.join(sorted(value))])
