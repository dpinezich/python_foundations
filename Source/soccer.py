soccer_team = ['enrico', 'pedro', 'paulo', 'fabio', 'cristiano', 'frei', 'sam', 'tom', 'peter', 'tim', 'pete']
print(soccer_team)
print(len(soccer_team))

soccer_team.append('susie')
print(soccer_team)
print(len(soccer_team))

new_defenders = ['faber', 'tony', 'troy']
soccer_team = soccer_team + new_defenders
print(soccer_team)
print(len(soccer_team))

print(soccer_team[9])
del(soccer_team[9])

print(soccer_team)

print('')
sign = ' and '
print('Best players: ' + sign.join(soccer_team[7:10]))


index = 0
while index < len(soccer_team):
    name = soccer_team[index]
    print('number: ' + str(index + 1) + ' name: ' + name)
    index = index + 1

















