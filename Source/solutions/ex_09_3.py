def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark * 2) * 0.5

marks = {}
while True:
    name = input('Name: ')
    if name == 'exit':
        break
    points = input('Points: ')
    max_points = input('Max Points: ')
    marks[name] = calculate_mark(points, max_points)

for (name, mark) in marks.items():
    if mark >= 4:
        print(name + ' has passed with ' + str(mark))
    else:
        print(name + ' has failed with ' + str(mark))
print('Bye bye')