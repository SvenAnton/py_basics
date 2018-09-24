"""Check if given ID code is valid."""

def check_your_id(id_code: str):
    """"
    Funktsioon kontrollib teiste abifunktsioonide abil, kas isikukood on valiidne.

    """
    if (check_gender_number(int(id_code[0])) and
        check_year_number_two_digits(int(id_code[1:3:])) and
        check_month_number(int(id_code[3:5])) and
        check_day_number(int(id_code[1:3:]), int(id_code[3:5]), int(id_code[5:7])) and
        check_born_order(int(id_code[7:10])) and
        check_control_number(id_code) and
        len(id_code) < 12):
            return True
    else:
        return False


def check_gender_number(gender_number: int):
    """"
    Funktsioon kontrollib, kas number on võimalik sootunnus isikukoodil.

    """
    if gender_number == 0 or gender_number > 6:
        return False
    else:
        return True


def check_year_number_two_digits(year_number: int):
    """"
    Funktsioon kontrollib, kas aastaarv on number 1-99.

    """
    if year_number == 0:
        return False

    if len(str(year_number)) == 2:
        return True
    else:
        return False


def check_month_number(month_number: int):
    """"
    Funktsioon kontrollib, kas kuu nr on arv 1-12.

    """
    if month_number > 12 or month_number == 0:
        return False
    else:
        return True


def check_day_number(year_number: int, month_number: int, day_number: int):
    """"
    Funktsioon kontrollib, kas kuupäeva number on tegelikult olemasolev kuupäeva number.

    Selleks on kasutatud kontrolli kuu numbri ja veebruarikuu puhul liigaasta järgi.
    """
    if day_number == 0 or day_number > 31:
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
    """"
    Funktsioon kontrollib, kas tegemist on liig-aastaga.

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
    """"
    Funktsioon kontrollin, kas sünnijärjekord on arv 1-999.

    """
    if born_order < 1000:
        return True
    else:
        return False



def check_control_number(id_code: str):
    """"
    Funktsioon arvutab kontrollnumbri ja kontrollib, kas see on õige antud isikukoodi arvestades.

    Kontrollnumber1 arvutab kontrollnumbri esimese arvutuse järgi.
    Kui jääk on 10, siis arvutatakse
    kontrollnumber 2
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
    """"
    Funktsioon tagastab info isikukoodi põhjal.

    """
    if check_your_id(id_code):
        return f"This is a {get_gender(int(id_code[0]))} born on {id_code[5:7]}.{id_code[3:5]}.{get_full_year(id_code[0], id_code[1:3])}"
    else:
        return "Given invalid ID code!"

def get_gender(gender_number: int):
    """"
    Funktsioon tagastab sisestatud numbri järgi soo.

    """
    if gender_number in (1, 3, 5):
        return "male"
    else:
        return "female"


def get_full_year(gender_number: int, year: int):
    """"
    Funktsioon teeb isikukoodis antud aastaarvu numbrist tegeliku aasta.

    """
    if gender_number in (1,2):
        year = 1800 + year
    if gender_number in (3,4):
        year = 1900 + year
    if gender_number in (5,6):
        year = 2000 + year
    return year
