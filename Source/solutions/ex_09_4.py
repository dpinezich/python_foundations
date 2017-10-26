def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark/0.5)*0.5

marks = {}
while True:
    name = input('Name: ')
    if name == 'exit':
        break
    points = input('Points: ')
    max_points = input('Max Points: ')
    marks[name] = calculate_mark(points, max_points)

avg = 0
for (name, mark) in marks.items():
    avg += mark
avg /= len(marks)
print('Average: ' + str(avg))
print('Bye bye')