""""Kodune ülesanne EX_02."""


from math import cos, sin, pi, atan, degrees, radians, sqrt


def convert_polar_to_cartesian(r, phi):
    """"funktsioon.

    See teeb polaarkoordinaadid ristkoordinaatideks.
    """
    phi = radians(phi)   # teen fii radiaanideks
    x = round(r * cos(phi), 2)  # arvutan x-i mat valemi järgi
    y = round(r * sin(phi), 2)  # arvutan y-i mat valemi järgi
    return (x, y)  # tagastan x ja y koordinaadid ennikuna


def convert_cartesian_to_polar(x, y):
    """Funktsioon.

    See teebristkoordinaadid polaarkoordinaatideks.
    """
    r = round(sqrt(x * x + y * y), 2)   # arvutan raadiuse Pythagorase teoreemi järgi
    if x > 0:   # alustan x- ja y- koordinaatide kontrolli fii arvutamiseks
        phi = atan(y / x)   # iga tingimuse järel on arvutus vastavalt mat tabelile
    elif x < 0 and y >= 0:
        phi = atan(y / x) + pi
    elif x < 0 and y < 0:
        phi = atan(y / x) - pi
    elif x == 0 and y > 0:
        phi = pi / 2
    elif x == 0 and y < 0:
        phi = -pi / 2
    elif x == 0 and y == 0:
        phi = 0
    phi = round(degrees(phi), 2)    # ümardan fii
    return (r, phi)     # tagastan raadiuse ja fii ennikuna
