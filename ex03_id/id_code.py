"""Check if given ID code is valid."""

import re


def check_your_id(id_code: str):
    """"Funktsioon kontrollib teiste abifunktsioonide abil, kas isikukood on valiidne.

    Kõigepealt välistan isikukoodid, mis üldse ei sobi, st koodid, mis sisaldavad tähti
    ja koodid, mis ei ole pikkusega 11. Seejärel kontrollin koodi valiidsust teiste
    funktsioonide abil.
    """
    if (re.search(r"[a-zA-Z]", id_code) is not None) or (len(id_code) != 11):
        return False

    if check_gender_number(int(id_code[0])) and \
            check_year_number_two_digits(int(id_code[1:3:])) and \
            check_month_number(int(id_code[3:5])) and \
            check_day_number(int(id_code[1:3:]), int(id_code[3:5]), int(id_code[5:7])) and \
            check_born_order(int(id_code[7:10])) and \
            check_control_number(id_code):
        return True
    else:
        return False


def check_gender_number(gender_number: int):
    """"Funktsioon kontrollib, kas number on võimalik sootunnus isikukoodil.

    Kontrollin ega antud number ei ole null või suurem kui 7, sest 1-6 on
    aktsepteeritav.
    """
    if gender_number != 0 and gender_number < 7:
        return True
    else:
        return False


def check_year_number_two_digits(year_number: int):
    """"Funktsioon kontrollib, kas aastaarv on number 1-99.

    Kontrollin ega antud number ei ole suurem, kui 100 (üle kahe koha) või null.
    """
    if (year_number < 100) and (year_number != 0):
        return True
    else:
        return False


def check_month_number(month_number: int):
    """"Funktsioon kontrollib, kas kuu nr on arv 1-12.

    Kuu number peab olema väiksem kui 13 ja ei tohi olla 0.
    """
    if month_number < 13 and month_number != 0:
        return True
    else:
        return False


def check_day_number(year_number: int, month_number: int, day_number: int):
    """"Funktsioon kontrollib, kas kuupäeva number on tegelikult olemasolev kuupäeva number.

    Selleks on kasutatud kontrolli kuu numbri ja veebruarikuu puhul liigaasta järgi.
    """
    if day_number == 0 or day_number >= 32:
        return False

    if month_number in (1, 3, 5, 7, 8, 10, 12):
        if day_number <= 31:
            return True
        else:
            return False

    if month_number in (4, 6, 9, 11):
        if day_number <= 30:
            return True
        else:
            return False

    if month_number == 2:
        if check_leap_year(year_number):
            if day_number <= 29:
                return True
            else:
                return False
        elif day_number <= 28:
            return True
        else:
            return False


def check_leap_year(year_number: int):
    """"Funktsioon kontrollib, kas tegemist on liig-aastaga.

    Koostan if funktsioonide pesa vastavalt ülesandes antud arvutusele.
    """
    if year_number % 4 == 0:
        if year_number % 100 == 0:
            if year_number % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def check_born_order(born_order: int):
    """"Funktsioon kontrollin, kas sünnijärjekord on arv 1-999.

    Born order ei saa olla suurem, kui 1000 või võrdne nulliga.
    """
    if born_order < 1000:
        return True
    else:
        return False


def check_control_number(id_code: str):
    """"Funktsioon arvutab kontrollnumbri ja kontrollib, kas see on õige antud isikukoodi arvestades.

    Kontrollnumber1 arvutab kontrollnumbri esimese arvutuse järgi.
    Kui jääk on 10, siis arvutatakse kontrollnumber 2. Kontrollnumber
    arvutatakse isikukoodi esimese kümne numbri korrutamist kordajaga vastavalt
    arvu postisioonile. Saadud korrutised liidetakse. Nt esimene number
    korrutatakse esimese kordajaga, teine teisega jne. Tulemused liidetakse.
    Esimesed kordajad on 1, 2, 3, 4, 5, 6, 7, 8, 9, 1
    Teised kordajad on 3, 4, 5, 6, 7, 8, 9, 1, 2, 3
    """
    kontrollnumber1 = 0

    for i in range(10):
        if i > 8:
            kontrollnumber1 += int(id_code[i:i + 1:])
        else:
            kontrollnumber1 += (i + 1) * int(id_code[i:i + 1:])

    kontrollnumber2 = 0
    for i in range(10):
        if i > 6:
            kontrollnumber2 += (i - 6) * int(id_code[i:i + 1:])
        else:
            kontrollnumber2 += (i + 3) * int(id_code[i:i + 1:])
    kontrollnumber1 = kontrollnumber1 % 11
    kontrollnumber2 = kontrollnumber2 % 11

    if kontrollnumber1 % 11 == 10:
        if kontrollnumber2 % 11 == 10:
            if int(id_code[10]) == 0:
                return True
            else:
                return False
        elif kontrollnumber2 % 11 == int(id_code[10]):
            return True
        else:
            return False
    elif kontrollnumber1 % 11 == int(id_code[10]):
        return True
    else:
        return False


def get_data_from_id(id_code: str):
    """"Funktsioon tagastab info isikukoodi põhjal.

    Tagastab laused vajaliku infoga.
    """
    if check_your_id(id_code):
        return f"This is a {get_gender(int(id_code[0]))} born on {id_code[5:7]}.{id_code[3:5]}.{get_full_year(int(id_code[0]), int(id_code[1:3]))}"
    else:
        return "Given invalid ID code!"


def get_gender(gender_number: int):
    """"Funktsioon tagastab sisestatud numbri järgi soo.

    Kontrollib isikukoodi esimese numbri põhjal, kas tegu on mehe või naisega.
    """
    if gender_number in (1, 3, 5):
        return "male"
    else:
        return "female"


def get_full_year(gender_number: int, year: int):
    """"Funktsioon teeb isikukoodis antud aastaarvu numbrist tegeliku aasta.

    Võtab isikukoodi esimese numbri järgi sajandi ja seejärel liidab
    otsa õige aastaarvu numbri isikukoodi 2-3 arvu järgi.
    """
    if gender_number in (1, 2):
        year = 1800 + year
    if gender_number in (3, 4):
        year = 1900 + year
    if gender_number in (5, 6):
        year = 2000 + year
    return year
