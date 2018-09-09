"""See on esimese ülesande EX01 lahendus. 1. osa on
nime küsimine. 2. osa on kehamassiindex"""

name = input("What's your name?")   # Küsin kasutajalt nime
while True:   # Küsin kuni kasutaja sisestab nime.
    if name == "":   # Kui väärtus on tühi string,
        name = input("Name was not inserted!") # küsi uuesti.
    else:   # Kui sisestatakse nimi, siis..
        school = input("Where do you study?")   # küsi kooli kohta...
        while True:   # niikaua kuni sisestatakse kool.
            if school == "":   # Kui kool on tühi,
                school = input("School was not inserted!")   # siis uuesti
            else:   # Kui kool sisestatud,
                break   # siis lõpeta tsükkel
        print(f"{name}, welcome to {school}")   # ja prindi tulemus.
        break   # lõpeta algne tsükkel.

"""Siia tuleb esimese ülesande teine osa. Teen kõigepealt funktsiooni,
mis arvutab kehamassiindeksi (bmi) ja seejärel sellest lähtuvalt
kehatüübi."""""

def body_values(mass, heigth):
    bmi = mass/(heigth*heigth)   # arvutan kehamassiindeksi.
    if bmi < 18.5:   # alakaalulisuse tingimuse kontrollimine.
        body_type = "Alakaaluline"
    elif bmi < 24.9:   # normaalkaalu tinimuste kontroll
        body_type = "Normaalkaal"
    else:
        body_type = "Ülekaal"   # Ülejäänud juhud on ülekaal.
    return bmi, body_type    # tagastan kehamassiindeksi ja kehatüübi.

mass = float(input("Insert your weigth in kilograms."))    #küsin massi.
heigth = float(input("Insert your heigth meters."))   # küsin pikkuse.
print(body_values(mass, heigth))    #prindin tulemuse.






