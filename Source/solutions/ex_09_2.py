def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark * 2) * 0.5

while True:
    exit = input('exit?: ')
    if exit == 'yes':
        break
    points = input('Points: ')
    max_points = input('Max Points: ')
    print(calculate_mark(points, max_points))

print('Bye bye')
