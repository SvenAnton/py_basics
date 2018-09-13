"""""See on süvapythoni Jänguru lahendus1."""


"""""See on süvapythoni Jänguru lahendus1."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """"Funktsiooni kasutan täiendavaid muutujaid.

    Need on kiiruse mõõtmiseks (speed1 ja speed2), while loop'ist väljumiseks (exit) ja loop-korduste
    lugemiseks (count). Funktsiooni esimeses osas küsin if-funktsiooniga võimatud olukorrad ja tagastan
    nende väärtuse -1. Teises osas jätkan võimalike juhtumitega ja alustan kontrolli jäneste kohtumise osas.
    Kontrollin mõlemaid jäneseid korraga samadel ajahetkedel.
    """
    speed1 = jump_distance1 / sleep1   # kiirus on liikumine ajahetke t kohta.
    speed2 = jump_distance2 / sleep2
    exit = 0
    count = -1   # kordused alustan miinus ühest, sest siis on esimene kordus 0 ja vastab ajahetkele t0.


    if (pos1 < pos2 and speed1 <= speed2) or (pos2 < pos1 and speed2 <= speed1):
        return -1   # tagastan väärtuse, kui kohtumine on võimatu. Kohtumine on võimatu, kui mõlemad: nii
    else:
        pos_difference = abs(pos1 - pos2)
        speed_difference = abs(speed1 - speed2)
        pos1 = round((pos_difference / speed_difference) * speed1 + pos1)
        pos2 = round((pos_difference / speed_difference) * speed2 + pos2)
        #print(pos1)
        #print(pos2)
        while exit == 0:   # teen loop'i
            if pos1 == pos2:   # kontrollin, kas positsioonid kattuvad,
                return pos1    # tagastan positsiooni, kui jänesed on koos
                exit = 1   # ja väljun loop'ist exit väärtust muutes.
            if (count % sleep1) == 0:   # kui ei kattu, siis lisan positsiooni ajahetkel t2. Selleks
                pos1 += jump_distance1  # kontrollin kõigepealt, kas magamise aeg on läbi. Magamise aeg on
            if (count % sleep2) == 0:   # läbi siis, kui korduste jagub täpselt, st toimub momentaalne hüpe
                pos2 += jump_distance2  # ja positsiooni väärtus suureneb.
            count += 1   # korduste lugeja väärtus suureneb.
