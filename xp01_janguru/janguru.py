"""""See on süvapythoni Jänguru lahendus1."""


def hopless_cases(start_pos1, jump_distance1, speed1, start_pos2, jump_distance2, speed2):
    """"Välistab lootusetud juhtumid. Muutujad on selgitatud põhifuntsioonis."""
    if start_pos1 == start_pos2:
        return start_pos1
    elif (start_pos1 < start_pos2 and jump_distance1 == 0) or (start_pos2 < start_pos1 and jump_distance2 == 0):
        return -1
    elif (start_pos1 < start_pos2 and speed1 <= speed2) or (start_pos2 < start_pos1 and speed2 <= speed1):
        return -1


def new_start_position(start_pos1, start_pos2, speed1, speed2, sleep1, sleep2, jump_distance1, jump_distance2):
    """"See arvutab uue ja kaugema kohtumiskoha. Lähemalt vt põhifuntksioon."""
    probable_meeting_place_minus = round(abs(start_pos1 - start_pos2) / abs(speed1 - speed2))
    if probable_meeting_place_minus > ((2 * sleep1) or (2 * sleep2)):
        if sleep1 < sleep2:
            return probable_meeting_place_minus - sleep2 * jump_distance2
        else:
            return probable_meeting_place_minus - sleep1 * jump_distance1
    else:
        return probable_meeting_place_minus - 1



def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """"See on ülesande põhifuntksioon.

    Kasutan muutujaid lineaarse kiiruse arvtamiseks: speed1 ja speed2.
    Samuti olen eraldi arvutanud stardipositsioonid välja: start_pos1 ja start_pos2.
    Muutuja: probable_meeting_place_minus on lineaarse kiiruse põhjal arvestatud võimalik kohtumispaik,
    millest olen lahutanud sleep'i ja võimaliku kohtumispaiga suhte järgi kas lihtsalt arvu 1 või
    avaldise sleep*distance - seda selleks, et lineaarne kohtumispaik võib olla sõltuvalt sleepi
    või distance'i tõttu oluliselt rohkem ees tegelikust kohtumispaigast. Korrutis võimaldab võtta
    tagasi mõlemat muutujat arvestades, kuid kaotab oluliselt koodi kiirust.
    Muutujad to_sleep on arvutus sellest, palju on jänestel jäänud magada kohas probable_meeting_place_minus.
    Esimene if-klauslite rida välistab võimatud olukorrad ja välistab -1. Eelkontroll ei saada lootusetuid
    juhtumeid loop'i.
    Loop'is kontrollitakse iga korduse järel, kas positsioonid kattuvad. Kui ei, siis korratakse jäneste
    liikumist arvestades nende magada jäänud päevi ja hüppe pikkust. Kui jänesel on veel magada vaja, siis
    hüpet ei toimu. Loop'i sees on kontroll ka selle kohta, et ega kiirem jänes, kes alguses oli küll maas teisest,
    ei ole vahepeal mööda läinud. Kui on, siis muutub kohtumine võimatuks ja  väljastatakse -1.
    """
    speed1 = jump_distance1 / sleep1   # kiirus on liikumine ajahetke t kohta.
    speed2 = jump_distance2 / sleep2
    start_pos1 = pos1 + jump_distance1
    start_pos2 = pos2 + jump_distance2
    hopless_cases(start_pos1, jump_distance1, speed1, start_pos2, jump_distance2, speed2)

    probable_meeting_place_minus = new_start_position(start_pos1, start_pos2, speed1, speed2, sleep1, sleep2)

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
        if ((start_pos1 < start_pos2) and (pos2 < pos1)) or ((start_pos2 < start_pos1) and (pos1 < pos2)):
            if abs(pos1 - pos2) > sleep1 * (jump_distance1 or sleep2 * jump_distance2):
                return -1
