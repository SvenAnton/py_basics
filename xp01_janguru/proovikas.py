"""""See on süvapythoni Jänguru lahendus1."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    start_pos1 = pos1 + jump_distance1
    start_pos2 = pos2 + jump_distance2

    if start_pos1 == start_pos2:
        return start_pos1

    if (start_pos1 < start_pos2 and jump_distance1 == 0) or (start_pos2 < start_pos1 and jump_distance2 == 0):
        return -1

    set1 = ()
    set2 = ()

    for i in set1:








print(meet_me(24, 28, 51, 24, 56, 82))

print(t1)


print(meet_me(1, 2, 1, 2, 1, 1)) #=> 3
print(meet_me(1, 2, 3, 4, 5, 5)) #=> -1
print(meet_me(10, 7, 7, 5, 8, 6)) #=> 45
print(meet_me(100, 7, 4, 300, 8, 6)) #=> 940
print(meet_me(1, 7, 1, 15, 5, 1)) #=> 50
print(meet_me(0, 1, 1, 1, 1, 1)) #=> -1
"""""
t1 = meet_me(941, 27, 47, 26, 17, 28)  # => 17060
t2 = meet_me(934, 22, 62, 82, 39, 34)  # => 1330
t3 = meet_me(901, 33, 85, 73, 60, 73)  # => 1693
meet_me(984, 29, 93, 69, 26, 68)  # => 4957
meet_me(940, 17, 77, 29, 22, 94)  # => 15781
meet_me(945, 2, 79, 26, 7, 62)  # => 1209
meet_me(90, 16, 19, 10, 16, 12)  # => 202
meet_me(75, 15, 6, 72, 18, 17)  # => 90
meet_me(25, 7, 18, 9, 6, 8)  # => 39
meet_me(97, 0, 3, 61, 1, 17)  # => 97
meet_me(72, 8, 19, 32, 12, 20)  # => 152
meet_me(37, 17, 14, 79, 11, 14)  # => 156
meet_me(65, 0, 11, 54, 11, 10)  # => 65
meet_me(3, 11, 4, 91, 19, 7)  # => 6152
meet_me(88, 4, 11, 90, 3, 18)  # => 96
meet_me(15, 5, 15, 39, 4, 18)  # => 95
""""
