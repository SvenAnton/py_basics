"""""See on süvapythoni Jänguru lahendus1."""

import timeit

start = timeit.default_timer()

"""""See on süvapythoni Jänguru lahendus1."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):

    speed1 = jump_distance1 / sleep1   # kiirus on liikumine ajahetke t kohta.
    speed2 = jump_distance2 / sleep2
    pos1 = pos1 + jump_distance1
    pos2 = pos2 + jump_distance2
    speed_differance = abs(speed1 - speed2)
    if speed_differance == 0:
        return -1
    if pos1 == pos2:
        return pos1

    probable_meeting_time_minus_one = round(abs(pos1 - pos2) / abs(speed1 - speed2))


    if probable_meeting_time_minus_one > sleep1 and sleep2:
        if sleep1 < sleep2:
            probable_meeting_time_minus_one = probable_meeting_time_minus_one - sleep2
        else:
            probable_meeting_time_minus_one = probable_meeting_time_minus_one - sleep1
    else:
        probable_meeting_time_minus_one -= probable_meeting_time_minus_one




    pos1 = (probable_meeting_time_minus_one // sleep1) * jump_distance1 + pos1
    pos2 = (probable_meeting_time_minus_one // sleep2) *jump_distance2 + pos2


    to_sleep1 = (probable_meeting_time_minus_one % sleep1)
    to_sleep2 = (probable_meeting_time_minus_one % sleep2)



    #print("alustan arvutusi nendelt positsioonidelt: ", pos1, pos2)
    #print("niipalju on nendelt positsioonidelt jäänud magada: ", to_sleep1, to_sleep2)
    #print("Võimalik kohtumisaeg miinus üks sleep: ", probable_meeting_time_minus_one)

    exit = 0
    count = 0

    if (pos1 < pos2 and speed1 <= speed2) or (pos2 < pos1 and speed2 <= speed1):
        return -1   # tagastan väärtuse, kui kohtumine on võimatu. Kohtumine on võimatu, kui mõlemad: nii
    else:
        while exit == 0:   # teen loop'i
            #print(f"Jõudsin loopi{pos1, pos2}, tegemist on {count} kordusega")
            #print(to_sleep1, to_sleep2)

            if pos1 == pos2:   # kontrollin, kas positsioonid kattuvad,
                return pos1    # tagastan positsiooni, kui jänesed on koos
                exit = 1   # ja väljun loop'ist exit väärtust muutes.

            if to_sleep1 > 0:
                to_sleep1 -= 1
                if to_sleep1 == 0:
                    pos1 += jump_distance1

            if to_sleep2 > 0:
                to_sleep2 -= 1
                if to_sleep2 == 0:
                    pos2 += jump_distance2

            if to_sleep1 == 0:
                if (count % sleep1) == 0:  # kui ei kattu, siis lisan positsiooni ajahetkel t2. Selleks
                    pos1 += jump_distance1

            if to_sleep2 == 0:
                if (count % sleep2) == 0:  # läbi siis, kui korduste jagub täpselt, st toimub momentaalne hüpe
                    pos2 += jump_distance2  #    ja positsiooni väärtus suureneb.

            count += 1

test1 = meet_me(1, 2, 1, 2, 1, 1)   # 3
test2 = meet_me(1, 2, 3, 4, 5, 5)   # -1
test3 = meet_me(10, 7, 7, 5, 8, 6)  # 45
test4 = meet_me(100, 7, 4, 300, 8, 6)   # 940
test5 = meet_me(1, 7, 1, 15, 5, 1)   # 50
test6 = meet_me(0, 1, 1, 1, 1, 1)   # -1

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)
stop = timeit.default_timer()

print('Time: ', stop - start)
