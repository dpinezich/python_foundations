def is_between(x, y, z):
    return x <= y <= z

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

print(is_between(x, y, z))