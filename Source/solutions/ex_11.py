min = 1
max = 100
counter = 1
while True:
    guessed_number = int((min + max) / 2)
    print('Guessed number: ' + str(guessed_number))
    answer = input("Answer: ")
    if answer == '=':
        print('The number is ' + str(guessed_number))
        print('It took me ' + str(counter) + ' rounds.')
        break
    elif answer == '<':
        min = guessed_number + 1
    else:
        max = guessed_number - 1
    counter += 1