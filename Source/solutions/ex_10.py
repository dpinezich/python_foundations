import random

#Generate the random number that the user has to guess
random_number = random.randrange(1,100)

#The first guess is initialized to zero. We know that this is not equal to the random number, as the random number lies between 1 and 100
guessed_number = 0

#Initialize the counter
counter = 1

#While the correct number has not been guessed we play
while random_number != guessed_number:

	#Ask the user for her/his guess
    guessed_number = int(input('Guessed number: '))

    #Handle the different cases: correct guess, too low, too high
    if guessed_number == random_number:
        print('Yeah! The random number is ' + str(random_number))
        print('It took you ' + str(counter) + ' rounds')
    elif guessed_number < random_number:
        print('Sry, too low!')
    else:
        print('Sry, too high!')

    #Before each new guess, we increment the counter by 1    
    counter += 1