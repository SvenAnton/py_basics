"""""See on süvapythoni Jänguru lahendus1"""

def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    pos_after_jump1 = pos1 + jump_distance1
    pos_after_jump2 = pos2 + jump_distance2
    speed1 = jump_distance1 / sleep1
    speed2 = jump_distance2 / sleep2

    x = []
    y = []
    exit = 0

    if (pos1 < pos2 and speed1 <= speed2) or (pos2 < pos1 and speed2 <= speed1):
        return -1
    else:
        while exit == 0:
            x.append(pos_after_jump1)
            y.append(pos_after_jump2)
            if pos_after_jump1 == pos_after_jump2:
                return pos_after_jump1
                exit = 1
            if (len(x) % sleep1) == 0:
                pos_after_jump1 += jump_distance1
            if (len(y) % sleep2) == 0:
                pos_after_jump2 += jump_distance2
