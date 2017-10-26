import maths


def distance(x1, y1, x2, y2):
    result = maths.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result



x1 = int(input('Point 1 x-cord: '))
y1 = int(input('Point 1 y-cord: '))
x2 = int(input('Point 2 x-cord: '))
y2 = int(input('Point 2 y-cord: '))

print(distance(x1, y1, x2, y2))
