import maths

def volume_from_radius(radius):
    return 4.0/3 * maths.pi * radius ** 3

radius = int(input('Radius: '))

print(volume_from_radius(radius))