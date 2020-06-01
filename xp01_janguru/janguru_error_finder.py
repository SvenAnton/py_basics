"""
Syva python janguru error finder
Autor: Timo Loomets

Selle koodi peamine eesmärk on leida edge case'id mille puhul sinu programm ei tööta.
See kood kasutab suvaliselt genereeritud teste ja nende korrektseid vastuseid,
et leida testid millega sinu kood saab vale vastuse. Kood ei kontrolli timeout
errorit. Kokku on kontrollib kood 100000 testi. Soovitatavalt kasutada koodi koos
jang_debug.txt failiga. Test andmetes olevad vastused põhinevad koodil, mis saavutas
100% ja on kaitstud.

Kontrollija kasutamine:
1. Kopeeri "jang_debug.txt" ja "janguru_error_finder.py" oma koodiga samasse kausta.
2. Kontrolli, et sinu kood oleks failis "janguru.py"
3. Kontrolli, et sul oleks olemas funktsioon meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2).
4. Käivita kood "janguru_error_finder.py" või funktsioon find_errors().
5. Väljastatakse test andmed ja vastused millega sinu kood failis.
6. Profit!!!!!!!

Disclaimer:
Tegu on vaid abi programmiga ja kasutamine ning usaldamine on omal vastutusel.
See kood ei asenda Ago tarkusi ja oma aju kasutamist.
"""


def find_errors():
    from xp01_janguru.janguru import meet_me
    
    tests = open("jang_debug.txt", "r+")

    for current_line in tests:
        if '\n' == current_line[-1]:
            values =  list(map(int, current_line.split(", ")))
            your_answer = meet_me(values[0], values[1], values[2], values[3], values[4], values[5])
            if your_answer != values[6]:
                print("failed: ", values[0:6])
                print("your answer: ", your_answer)
                print("correct answer: ", values[6])
                print()

if __name__ == '__main__':
    find_errors()
