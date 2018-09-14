"""""See on süvapythoni Jänguru lahendus1."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):

    speed1 = jump_distance1 / sleep1   # kiirus on liikumine ajahetke t kohta.
    speed2 = jump_distance2 / sleep2

    start_pos1 = pos1 + jump_distance1
    start_pos2 = pos2 + jump_distance2


    if start_pos1 == start_pos2:
        return start_pos1
    elif (start_pos1 < start_pos2 and jump_distance1 == 0) or (start_pos2 < start_pos1 and jump_distance2 == 0):
        return -1
    elif (start_pos1 < start_pos2 and speed1 <= speed2) or (start_pos2 < start_pos1 and speed2 <= speed1):
        print("lootusetu üritus")
        return -1


    probable_meeting_place_minus = round(abs(start_pos1 - start_pos2) / abs(speed1 - speed2))

    if probable_meeting_place_minus > ((2*sleep1) or (2*sleep2)):
        if sleep1 < sleep2:
            probable_meeting_place_minus = probable_meeting_place_minus - sleep2*jump_distance2
        else:
            probable_meeting_place_minus = probable_meeting_place_minus - sleep1*jump_distance1
    else:
        probable_meeting_place_minus = probable_meeting_place_minus - 1

    pos1 = (probable_meeting_place_minus // sleep1) * jump_distance1 + start_pos1
    pos2 = (probable_meeting_place_minus // sleep2) *jump_distance2 + start_pos2
    to_sleep1 = sleep1 - (probable_meeting_place_minus % sleep1)
    to_sleep2 = sleep2 - (probable_meeting_place_minus % sleep2)

    #print("alustan arvutusi nendelt positsioonidelt: ", pos1, pos2)
    #print(f"niipalju on magada algpositsioonilt: {to_sleep2}, {to_sleep1}")
    #print("Võimalik kohtumiskoht miinus üks sleep: ", probable_meeting_place_minus)
    #print(abs(speed1 - speed2), abs(start_pos1 - start_pos2))

    while True:   # teen loop'i
        print(f"Esimene jänes: {pos1} [{to_sleep1}] Teine jänes:   {pos2} [{to_sleep2}] ")

        if pos1 == pos2:   # kontrollin, kas positsioonid kattuvad,
            return pos1    # tagastan positsiooni, kui jänesed on koos

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
                print(start_pos1, start_pos2, pos1, pos2)
                print("Hüppas mööda")
                return -1

#test1 = meet_me(1, 2, 1, 2, 1, 1)   # 3
#test2 = meet_me(1, 2, 3, 4, 5, 5)   # -1
#test3 = meet_me(10, 7, 7, 5, 8, 6)  # 45
#test4 = meet_me(100, 7, 4, 300, 8, 6)   # 940
#test5 = meet_me(1, 7, 1, 15, 5, 1)   # 50
#test6 = meet_me(0, 1, 1, 1, 1, 1)   # -1

#print(test1)
#print(test2)
#print(test3)
#print(test4)
#print(test5)
#print(test6)

#t1 = meet_me(918674, 5527, 5704, 1919, 2763, 2833) # => 16159432
#print(t1)

#t16 = meet_me(3, 11, 4, 91, 19, 7)  # => 6152 - tuleb 7197


#print(t16 , t17)
