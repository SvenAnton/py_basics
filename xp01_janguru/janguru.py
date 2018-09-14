"""""See on süvapythoni Jänguru lahendus1."""


"""""See on süvapythoni Jänguru lahendus1."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):

    speed1 = jump_distance1 / sleep1   # kiirus on liikumine ajahetke t kohta.
    speed2 = jump_distance2 / sleep2
    pos1 = pos1 + jump_distance1
    pos2 = pos2 + jump_distance2
    speed_differance = abs(speed1 - speed2)

    if pos1 == pos2:
        return pos1
    elif jump_distance1 == 0 or jump_distance2 == 0:
        #print("not jumping")
        return -1
    elif speed_differance == 0:
        #print("Ei liigu edasi")
        return -1

    probable_meeting_time_minus_one = round(abs(pos1 - pos2) / abs(speed1 - speed2))


    if probable_meeting_time_minus_one > ((2*sleep1) or (2*sleep2)):
        if sleep1 < sleep2:
            probable_meeting_time_minus_one = probable_meeting_time_minus_one - sleep2
        else:
            probable_meeting_time_minus_one = probable_meeting_time_minus_one - sleep1
    else:
        probable_meeting_time_minus_one = probable_meeting_time_minus_one - 1



    pos1 = (probable_meeting_time_minus_one // sleep1) * jump_distance1 + pos1
    pos2 = (probable_meeting_time_minus_one // sleep2) *jump_distance2 + pos2


    to_sleep1 = sleep1 - (probable_meeting_time_minus_one % sleep1)
    to_sleep2 = sleep2 - (probable_meeting_time_minus_one % sleep2)

    #print("alustan arvutusi nendelt positsioonidelt: ", pos1, pos2)
    #print(f"niipalju on magadaalgpositsioonilt: {to_sleep2}, {to_sleep1}")
    #print("Võimalik kohtumisaeg miinus üks sleep: ", probable_meeting_time_minus_one)

    exit = 0

    if (pos1 < pos2 and speed1 <= speed2) or (pos2 < pos1 and speed2 <= speed1):
        return -1   # tagastan väärtuse, kui kohtumine on võimatu. Kohtumine on võimatu, kui mõlemad: nii

    while exit == 0:   # teen loop'i
        #print(f"Esimene jänes: {pos1} [{to_sleep1}] Teine jänes:   {pos2} [{to_sleep2}] ")
        #print(f" magada jäänud {sleep2 - to_sleep2}  magada jäänud: {sleep1 - to_sleep1}")

        if pos1 == pos2:   # kontrollin, kas positsioonid kattuvad,
            return pos1    # tagastan positsiooni, kui jänesed on koos
            exit = 1   # ja väljun loop'ist exit väärtust muutes.

        if to_sleep1 == 0:
            pos1 += jump_distance1
            to_sleep1 = sleep1
        if to_sleep2 == 0:
            pos2 += jump_distance2
            to_sleep2 = sleep2

        to_sleep1 -= 1
        to_sleep2 -= 1
