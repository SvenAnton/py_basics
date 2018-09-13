"""Triangle info."""


from math import sqrt

def find_triangle_info(a, b, c):
    """
    Write a function which finds perimeter, area and type(eg: isosceles right triangle) of triangle
    based on given side lengths. (Note: a <= b <= c).

    The function should print "{type_by_length} {type_by_angle} triangle with perimeter of {perimeter}
    units and area of {area} units". IE: sides 3, 4, 5 should print "Scalene right triangle with perimeter
    of 12.0 units and area of 6.0 units".
    :return: None
    """
    perimeter = round((a + b + c), 2)
    p = perimeter / 2
    area = round(sqrt((p * (p - a) * (p - b) * (p - c))), 2)

    if (a*a + b*b) < c*c:
        type_by_angle = "Obtuse"
    elif (a*a + b*b) > c*c:
        type_by_angle = "Acute"
    else:
        type_by_angle = "Right"

    if a == b == c:
        type_by_length = "Equilateral"
    elif a == b or b == c or a == c:
        type_by_length = "Isosceles"
    else:
        type_by_length = "Scalene"

    print(f"{type_by_length} {type_by_angle} triangle with perimeter of {perimeter} units and area of {area} units")
