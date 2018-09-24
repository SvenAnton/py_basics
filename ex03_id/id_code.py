"""Check if given ID code is valid."""


import re

def check_your_id(id_code: str):
    """"
    Funktsioon kontrollib teiste abifunktsioonide abil, kas isikukood on valiidne.

    """
    if re.search(r"[a-zA-Z]", id_code) == None:
        return True
    else:
        return False

    if (check_gender_number(int(id_code[0])) and
        check_year_number_two_digits(int(id_code[1:3:])) and
        check_month_number(int(id_code[3:5])) and
        check_day_number(int(id_code[1:3:]), int(id_code[3:5]), int(id_code[5:7])) and
        check_born_order(int(id_code[7:10])) and
        check_control_number(id_code) and
        len(id_code) == 11):
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

if __name__ == '__main__':
    print("Overall ID check::")
    print(check_your_id("49808270244"))  # -> True
    personal_id = input()  # type your own id in command prompt
    print(check_your_id(personal_id))  # -> True
    print(check_your_id("12345678901"))  # -> False
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {check_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(check_year_number_two_digits(100))  # -> False
    print(check_year_number_two_digits(50))  # -> true
    print("\nMonth number:")
    print(check_month_number(2))  # -> True
    print(check_month_number(15)) # -> False
    print("\nDay number:")
    print(check_day_number(5, 12, 25))  # -> True
    print(check_day_number(10, 8, 32))  # -> False
    print(check_leap_year(1804))  # -> True
    print(check_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(check_day_number(96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(check_day_number(99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(check_day_number(8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(check_day_number(22, 4, 31))  # -> False (April contains max 30 days)
    print(check_day_number(18, 10, 31))  # -> True
    print(check_day_number(15, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(check_born_order(0))  # -> True
    print(check_born_order(850))  # -> True
    print("\nControl number:")
    print(check_control_number("49808270244"))  # -> True
    print(check_control_number("60109200187"))  # -> False, it must be 6
