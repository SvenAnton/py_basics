"""""See on süvapythoni Jänguru lahendus1."""

""""Lahenduseks on funktsioon, mis loob mõlema jänese teekonna listina, kus listi indeks on üks ajaühik t ja
ja arvu suurus näitab distantsi kus viibitakse. t=0 on positsioon pärast esimest hüpet. Selleks olen teinud ka
eraldi muutujad pos_after_jump1 ja pos_after_jump2. Listid olen praegu mugavuse mõttes jätnud x ja y, vastavalt siis
1. jänes ja teine jänes. Olen arvutanud ka kiiruse selleks, et välistada olukorrad, kus kohtumist kunagi ei toimu.
Kui jänese algpositsioon ja kiirus on mõlemad väiksemad kui teisel jänesel, siis ei leia kohtumine kunagi aset, sest
teise hüppe ajaks on ka vahepealne magamisaeg läbitud.

Kui olukord ei ole võimatu, siis hakkangi looma listi, kus kõrvutan järjest listi vastavaid elemente. Võrdlen esimest
esimesega, teist teisega jne. Nii on tagatud olukord, kus jänesed on tõepoolest samal ajahetkel samal distantsil.

Hetkel on kood väga ressurssimahukas ja ma proovin seda parandada"""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """"See on funktsioon."""
    x = []
    y = []
    exit = 0
    if (pos1 + jump_distance1 < pos2 + jump_distance2 and jump_distance1 / sleep1 <= jump_distance2 / sleep2) or (
            pos2 + jump_distance2 < pos1 + jump_distance1 and jump_distance2 / sleep2 <= jump_distance1 / sleep1):
        return -1
    else:
        while exit == 0:
            x.append(pos1 + jump_distance1)
            y.append(pos2 + jump_distance2)
            if pos1 + jump_distance1 == pos2 + jump_distance2:
                return pos1 + jump_distance1
                exit = 1
            if (len(x) % sleep1) == 0:
                pos1 += jump_distance1
            if (len(y) % sleep2) == 0:
                pos2 += jump_distance2
