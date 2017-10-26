def calculate_mark(points, max_points):
    mark = (float(points) * 5.0 / float(max_points)) + 1
    return round(mark * 2) * 0.5


print(calculate_mark(32, 40))
print(calculate_mark(39, 40))
print(calculate_mark(18, 40))