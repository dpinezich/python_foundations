import maths

def distance(x1, y1, x2, y2):
    return maths.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def volume_from_radius(radius):
    return 4.0/3 * maths.pi * radius ** 3

def volume_from_points(x1, y1, x2, y2):
    radius = distance(x1, y1, x2, y2)
    return volume_from_radius(radius)