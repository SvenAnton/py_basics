"""""See on süvapythoni Jänguru lahendus1."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """"See on ülesande põhifuntksioon."""
    speed1 = jump_distance1 / sleep1   # kiirus on liikumine ajahetke t kohta.
    speed2 = jump_distance2 / sleep2
    start_pos1 = pos1 + jump_distance1
    start_pos2 = pos2 + jump_distance2

    if start_pos1 == start_pos2:
        return start_pos1
    elif (start_pos1 < start_pos2 and jump_distance1 == 0) or (start_pos2 < start_pos1 and jump_distance2 == 0):
        return -1
    elif (start_pos1 < start_pos2 and speed1 <= speed2) or (start_pos2 < start_pos1 and speed2 <= speed1):
        return -1

    probable_meeting_place_minus = round(abs(start_pos1 - start_pos2) / abs(speed1 - speed2))

    if probable_meeting_place_minus > ((2 * sleep1) or (2 * sleep2)):
        if sleep1 < sleep2:
            probable_meeting_place_minus = probable_meeting_place_minus - sleep2 * jump_distance2
        else:
            probable_meeting_place_minus = probable_meeting_place_minus - sleep1 * jump_distance1
    else:
        probable_meeting_place_minus = probable_meeting_place_minus - 1

    pos1 = (probable_meeting_place_minus // sleep1) * jump_distance1 + start_pos1
    pos2 = (probable_meeting_place_minus // sleep2) * jump_distance2 + start_pos2
    to_sleep1 = sleep1 - (probable_meeting_place_minus % sleep1)
    to_sleep2 = sleep2 - (probable_meeting_place_minus % sleep2)

    while True:
        if pos1 == pos2:
            return pos1

        if to_sleep1 == 0:
            pos1 += jump_distance1
            to_sleep1 = sleep1
        if to_sleep2 == 0:
            pos2 += jump_distance2
            to_sleep2 = sleep2

        to_sleep1 -= 1
        to_sleep2 -= 1

        if (((start_pos1 < start_pos2) and (pos2 < pos1)) or ((start_pos2 < start_pos1) and (pos1 < pos2))):
            if abs(pos1 - pos2) > sleep1 * (jump_distance1 or sleep2 * jump_distance2):
                return -1
