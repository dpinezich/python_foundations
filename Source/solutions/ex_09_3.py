def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark * 2) * 0.5

marks = {}
while True:
    points = input('Points: ')
    if points == 'exit':
        break
    max_points = input('Max Points: ')
    marks[name] = calculate_mark(points, max_points)

for (name, mark) in marks.items():
        print(name + ' has a ' + str(mark))
print('Bye bye')