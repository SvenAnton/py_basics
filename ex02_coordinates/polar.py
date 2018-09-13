""""Kodune ülesanne EX_02."""


from math import cos, sin, pi, atan, degrees, radians, sqrt


def convert_polar_to_cartesian(r, phi):
    """"funktsioon, mis teeb polaarkoordinaadid
    ristkoordinaatideks."""
    phi = radians(phi)
    x = round(r*cos(phi), 2)
    y = round(r*sin(phi),2)
    return x, y


def convert_cartesian_to_polar(x, y):
    """Funktsioon, mis teen ristkoordinaadid
    polaarkoordinaatideks."""
    r = round(sqrt(x*x + y*y), 2)
    if x > 0:
        phi = atan(y/x)
    elif x < 0 and y >= 0:
        phi = atan(y/x) + pi
    elif x < 0 and y < 0:
        phi = atan(y/x) - pi
    elif x == 0 and y > 0:
        phi = pi/2
    elif x == 0 and y < 0:
        phi = -pi/2
    elif x == 0 and y == 0:
        phi = 0
    phi = round(degrees(phi), 2)
    return r, phi
